# 1a · Course Overview: What Is an Agent?：课程笔记

状态：已学习。以下为记录模板，尚无课程内容总结。

## 核心问题与概念

### tool
可以在环境中执行的程序化函数,用来与环境交互.而每个时刻采取行动,行动会更新环境,进而改变agent所处的状态
#### tool definition
当于一个供模型调用的函数,需要有传参的结构化定义,以及自然语言的描述供模型进行理解
#### tool calls and results
工具调用
#### 借助工具模型就可以在环境中进行交互操作了

### reward
为了评估任务是否成功,需要一个分数来进行作为结果,可以使用llm做裁判对任务结果进行打分

### next token prediction
模型核心原理:预测token

### after-class assignments and
build a minimal ReAct loop from [mini-swe-agent](https://github.com/swe-agent/mini-swe-agent)

#### mini-swe-agent(源码查看)
优点:实现了coding agent领域一个标准基准(SWE-bench),对近期模型很有效且相当简洁

一开始会给模型一些消息,告知任务是什么.然后反复运行这个循环,agent会用所有过往消息向模型发起查询,这些消息包含了历史记录,
然后执行后放入历史再继续循环执行.执行动作->获取观察结果->返回

#### Example agent trajectory
[SWE-bench](https://www.swebench.com/) 数据集,他的测评任务和排行榜有个好处:提供了一些示例
##### Example01:GPT-OSS
check [gpt-oss-120b](https://docent.transluce.org/dashboard/4a0a2b2a-a65b-452a-88c7-bb5d99745c75) model,


## 方法与适用条件

无

## 课程与论文证据

[YouTube](https://www.youtube.com/watch?v=JQuI-0Yo1yw&t=1217s)

## 个人理解与疑问

### 标准基准(SWE-bench)是什么?

### ReAct是什么?


## 回顾与后续行动

无
