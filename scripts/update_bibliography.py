"""Sync paired arXiv/PDF links in the reference index to BibTeX (stdlib only)."""

import argparse
import os
from pathlib import Path
import re
import ssl
import sys
import tempfile
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ID = r"(?:\d{4}\.\d{4,5}|[a-zA-Z-]+(?:\.[A-Z]{2})?/\d{7})(?:v\d+)?"
ARXIV = re.compile(r"https?://(?:export\.)?arxiv\.org/(?:abs|pdf)/(" + ID + r")(?:\.pdf)?(?=$|[?#])")
LINK = re.compile(r"\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))\s*\)")


def base_id(value):
    return re.sub(r"v\d+$", "", value)


def extract_papers(readme):
    """One table row pairs exactly one arXiv ID with one existing local PDF."""
    papers = {}
    fenced = False
    for number, line in enumerate(readme.read_text(encoding="utf-8-sig").splitlines(), 1):
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
            continue
        if fenced or not line.lstrip().startswith("|"):
            continue
        ids, pdfs = set(), set()
        for match in LINK.finditer(line):
            target = match.group(1) or match.group(2)
            parsed = urllib.parse.urlsplit(target)
            arxiv = ARXIV.fullmatch(target)
            if arxiv:
                ids.add(arxiv.group(1))
            elif not parsed.scheme and not parsed.netloc and parsed.path.lower().endswith(".pdf"):
                pdfs.add((readme.parent / urllib.parse.unquote(parsed.path)).resolve())
        if not ids:
            continue
        if len(ids) != 1 or len(pdfs) != 1:
            raise ValueError(f"README line {number}: expected one arXiv link and one local PDF")
        paper_id, pdf = next(iter(ids)), next(iter(pdfs))
        if not pdf.is_relative_to(ROOT) or not pdf.is_file():
            raise ValueError(f"README line {number}: PDF missing or outside repository: {pdf}")
        old = papers.get(base_id(paper_id))
        if old and old != (paper_id, pdf):
            raise ValueError(f"Conflicting PDF paths or versions for {paper_id}")
        papers[base_id(paper_id)] = (paper_id, pdf)
    if not papers:
        raise ValueError("No paired arXiv/PDF links found in README table")
    return papers


def fetch_metadata(ids):
    query = urllib.parse.urlencode({"id_list": ",".join(ids), "max_results": len(ids)})
    request = urllib.request.Request(
        "https://export.arxiv.org/api/query?" + query,
        headers={"User-Agent": "cmu-ai-agents-study-bibliography/1.0"},
    )
    context = ssl.create_default_context()
    if sys.platform == "win32":
        # Include Windows intermediate certificates for Python/OpenSSL distributions.
        for store in ("ROOT", "CA"):
            for cert, encoding, trust in ssl.enum_certificates(store):
                if encoding == "x509_asn" and (trust is True or ssl.Purpose.SERVER_AUTH.oid in trust):
                    context.load_verify_locations(cadata=ssl.DER_cert_to_PEM_cert(cert))
    with urllib.request.urlopen(request, timeout=30, context=context) as response:
        return response.read()


def parse_metadata(xml):
    ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
    result = {}
    for entry in ET.fromstring(xml).findall("a:entry", ns):
        identity = entry.findtext("a:id", "", ns)
        match = ARXIV.fullmatch(identity)
        if not match:
            raise ValueError(f"Unexpected arXiv response entry: {identity}")
        title = " ".join(entry.findtext("a:title", "", ns).split())
        authors = [" ".join(a.findtext("a:name", "", ns).split()) for a in entry.findall("a:author", ns)]
        published = entry.findtext("a:published", "", ns)
        category = entry.find("x:primary_category", ns)
        if not title or not authors or not all(authors) or not re.match(r"\d{4}-", published) or category is None:
            raise ValueError(f"Incomplete arXiv metadata: {identity}")
        result[base_id(match.group(1))] = {
            "title": title, "author": " and ".join(escape_bib(a) for a in authors),
            "year": published[:4], "primaryClass": category.attrib["term"],
            "resolved_id": match.group(1),
        }
    return result


def split_top_level(text):
    """Split BibTeX commas outside braces/quotes, retaining nested TeX content."""
    depth, quoted, escaped, start = 0, False, False, 0
    for i, ch in enumerate(text):
        if escaped:
            escaped = False
            continue
        if ch == "\\":
            escaped = True
        elif ch == '"' and depth == 0:
            quoted = not quoted
        elif ch == "{" and not quoted:
            depth += 1
        elif ch == "}" and not quoted:
            depth -= 1
        elif ch == "," and depth == 0 and not quoted:
            yield text[start:i]
            start = i + 1
        if depth < 0:
            raise ValueError("Unbalanced BibTeX braces")
    if depth or quoted:
        raise ValueError("Unbalanced BibTeX braces or quotes")
    yield text[start:]


def bib_entries(text):
    """Read brace-delimited entries; refuse unsupported constructs before writing."""
    position = 0
    while match := re.search(r"(?m)^\s*@([A-Za-z]+)\s*([({])", text[position:]):
        start = position + match.start()
        opening = position + match.end() - 1
        if match.group(2) != "{":
            raise ValueError("Parenthesized BibTeX entries are unsupported; use braces")
        depth, escaped = 1, False
        end = opening + 1
        while end < len(text) and depth:
            ch = text[end]
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            end += 1
        if depth:
            raise ValueError("Unclosed BibTeX entry")
        kind = match.group(1)
        if kind.lower() not in {"comment", "preamble", "string"}:
            parts = list(split_top_level(text[opening + 1:end - 1]))
            key, fields = parts[0].strip(), {}
            for part in parts[1:]:
                if not part.strip():
                    continue
                field = re.fullmatch(r"\s*([\w-]+)\s*=\s*(.*?)\s*", part, re.S)
                if not field or field.group(1).lower() in fields:
                    raise ValueError(f"Unsupported or duplicate BibTeX field in {key}")
                fields[field.group(1).lower()] = (field.group(1), field.group(2))
            yield start, end, kind, key, fields
        position = end


def escape_bib(text):
    replacements = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "&": r"\&", "%": r"\%", "_": r"\_", "#": r"\#", "$": r"\$", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(replacements.get(ch, ch) for ch in text)


def merge_bibliography(existing, papers, metadata, output):
    entries = list(bib_entries(existing))
    keys = [e[3] for e in entries]
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate BibTeX citation keys")
    replacements, additions = [], []
    for identity, (requested_id, pdf) in papers.items():
        data = metadata.get(identity)
        if not data or (requested_id != identity and data["resolved_id"] != requested_id):
            raise ValueError(f"Missing or mismatched arXiv metadata: {requested_id}")
        matches = []
        for entry in entries:
            fields = entry[4]
            eprint = fields.get("eprint", ("", ""))[1].strip('{}" ')
            source = fields.get("url", ("", ""))[1].strip('{}" ')
            link = ARXIV.fullmatch(source)
            if base_id(eprint) == identity or (link and base_id(link.group(1)) == identity):
                matches.append(entry)
        if len(matches) > 1:
            raise ValueError(f"Multiple BibTeX entries for {identity}")
        fields = dict(matches[0][4]) if matches else {}
        key = matches[0][3] if matches else "arxiv" + re.sub(r"[^A-Za-z0-9]", "", identity)
        if not matches and key in keys:
            raise ValueError(f"Citation key collision: {key}")
        relative = Path(os.path.relpath(pdf, output.parent)).as_posix()
        managed = {
            "title": escape_bib(data["title"]), "author": data["author"],
            "year": data["year"], "eprint": requested_id, "archivePrefix": "arXiv",
            "primaryClass": data["primaryClass"], "url": "https://arxiv.org/abs/" + requested_id,
            "file": escape_bib(relative),
        }
        for name, value in managed.items():
            fields[name.lower()] = (name, "{" + value + "}")
        kind = matches[0][2] if matches else "misc"
        rendered = "@" + kind + "{" + key + ",\n" + ",\n".join(
            f"  {name} = {value}" for name, value in fields.values()) + "\n}"
        if matches:
            start, end = matches[0][:2]
            # Entry regex includes preceding whitespace; preserve it.
            prefix = existing[start:end].split("@", 1)[0]
            replacements.append((start, end, prefix + rendered))
        else:
            additions.append(rendered)
    for start, end, replacement in sorted(replacements, reverse=True):
        existing = existing[:start] + replacement + existing[end:]
    if additions:
        existing = existing.rstrip() + "\n\n" + "\n\n".join(additions) + "\n"
    return existing


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=ROOT / "references/README.md")
    parser.add_argument("--output", type=Path, default=ROOT / "references/bibliography.bib")
    parser.add_argument("--metadata-file", type=Path, help="Use a saved arXiv Atom XML response (offline)")
    parser.add_argument("--dry-run", action="store_true", help="Print proposed BibTeX without writing")
    args = parser.parse_args()
    try:
        papers = extract_papers(args.readme.resolve())
        xml = args.metadata_file.read_bytes() if args.metadata_file else fetch_metadata([p[0] for p in papers.values()])
        output = args.output.resolve()
        existing = output.read_text(encoding="utf-8-sig") if output.exists() else ""
        updated = merge_bibliography(existing, papers, parse_metadata(xml), output)
        if args.dry_run:
            print(updated, end="")
        elif updated == existing:
            print(f"Unchanged: {len(papers)} paper(s)")
        else:
            # All rows and metadata must validate before replacing the destination.
            temp = None
            try:
                with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=output.parent, delete=False) as handle:
                    temp = Path(handle.name)
                    handle.write(updated)
                temp.replace(output)
            finally:
                if temp and temp.exists():
                    temp.unlink()
            print(f"Updated {output}: {len(papers)} paper(s)")
    except (OSError, ValueError, ET.ParseError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
