# Grant 的 4 周 LLM / Agent 系统化学习计划（基于知识树）

> 适用对象：已经学过一遍 LLM / Agent，但感觉知识零散、掌握感弱，希望通过 **结构化复习 + 输出 + 小项目** 形成系统性知识的人。
>
> 学习节奏：
> - **周中**：每天 **早上 2 小时 + 晚上 2 小时 = 4 小时**
> - **周末**：每天 **8 小时**
> - **每周总计**：36 小时
> - **4 周总计**：144 小时

---

# 0. 为什么这 4 周要这样安排？

这 4 周的节奏不是按“框架名称”来排，而是严格按知识树的四层结构推进：

1. **模型层**：先搞清楚模型本身会什么、不会什么，特别是 prompt、structured output、tool calling 的边界。OpenAI 明确指出 function calling 的本质是：模型根据你定义的工具 schema 生成调用请求，你的应用负责执行工具并把结果再回传给模型。citeturn1search13
2. **增强层**：再去系统理解 RAG / Tools / Memory。Anthropic 把 retrieval、tools、memory 统称为 **augmented LLM** 的能力增强；LlamaIndex 则把 RAG 拆成 Loading / Indexing / Storing / Querying / Evaluation 五阶段，非常适合做系统化学习主线。citeturn1search1turn1search26
3. **编排层**：在增强层之上，再去分清 workflow 和 agent。Anthropic 非常强调：不是所有多步系统都应该做 agent，很多场景里固定流程的 workflow 更简单、更可控，而只有当步骤不可预测、需要模型动态决策时，agent 才合适。citeturn1search1
4. **生产层**：最后补上 tracing、eval、security、cost、deployment。OpenAI 建议从 traces 开始定位 agent 行为问题，再沉淀 graders、datasets 和 eval runs；Phoenix 强调没有 tracing 就是在“盲飞”；Azure 和 MCP 则分别强调企业 RAG / 工具调用必须纳入权限、安全和治理。citeturn1search54turn1search39turn1search33turn1search20

所以，这 4 周的目标不是“再看一遍内容”，而是：

> **每周打通一个认知闭环，每周形成一个可交付成果。**

---

# 1. 每天的固定学习节奏

## 1.1 周中（每天 4 小时）

### 早上 2 小时：输入 + 重建
- **30 分钟**：只看一个核心主题的关键资料
- **30 分钟**：闭眼重建（不看资料，自己写定义 / 画结构图）
- **60 分钟**：把内容填回知识树对应节点模板

### 晚上 2 小时：输出 + 实操
- **60 分钟**：做最小 demo / 小实验
- **30 分钟**：写失败案例 / bug 记录
- **30 分钟**：写一页纸总结（One Page）

---

## 1.2 周末（每天 8 小时）

### 建议时段
- **09:00–12:00**：专题深挖 + 总图整理
- **14:00–17:00**：做 mini project / 模块联调
- **19:00–21:00**：复盘 + 知识树整理 + 面试表达

---

# 2. 四周总路线图

## 第 1 周：模型层 + Tool Calling 基础
目标：建立“模型本体边界感”，并做出最小的 **LLM + Tool Calling** 闭环。OpenAI 对 function calling 的定义、Anthropic 对 augmented LLM 的解释，都说明工具调用是后面 agent 系统的最小基础单元。citeturn1search13turn1search1

## 第 2 周：RAG 系统
目标：把 RAG 从一个模糊概念拆成完整检索管道。LlamaIndex 的五阶段拆法和 Azure 对 hybrid search / semantic ranking / security trimming 的实践建议，是本周主线。citeturn1search26turn1search33

## 第 3 周：Workflow / Agent 编排层
目标：建立 workflow 与 agent 的边界感，学会用 Anthropic 的五种经典 workflow 模式去理解所有“看起来很复杂”的 Agent 系统。LangChain 的 agent harness / middleware / HITL / subagent 能帮助你把模式变成工程实现。citeturn1search1turn1search7

## 第 4 周：生产层 + 项目整合
目标：给系统加上 tracing、eval、guardrails、安全、成本意识，并完成一个能写进简历的原型项目。OpenAI 的 trace → dataset → eval 思路、Phoenix 的 tracing、Azure/MCP 的安全边界，都在这一周落地。citeturn1search54turn1search39turn1search33turn1search20

---

# 3. 第 1 周：模型层 + Tool Calling 基础

## 3.1 本周目标
- 建立“模型 / 工具 / 应用”的边界感。OpenAI 明确指出：模型不会真正执行函数，它只会生成一个 tool call 请求；工具执行和结果回填由应用来做。citeturn1search13
- 理解 Anthropic 所说的 **augmented LLM** 最小单元：LLM + tools（后面再加 retrieval / memory）。citeturn1search1
- 做出一个最小闭环 demo：
  - 用户输入
  - 模型选择工具
  - 应用执行工具
  - 回传结果
  - 模型生成最终答案

## 3.2 本周输出物
- 已填知识树节点：
  - `Tokens_Context_Window.md`
  - `Prompting.md`
  - `Structured_Output.md`
  - `Function_Calling_Basics.md`
  - `Tools/Tool_Schema_Design.md`
  - `Tools/Tool_Selection.md`
- 一个最小 demo：`LLM + 1~2 个工具 + 严格 schema`
- 一页纸：`One_Page_Tool_Calling.md`

---

## 3.3 每日计划

### Day 1（周一）
#### 早上 2h
- 写本周总图：模型做什么 / 工具做什么 / 应用做什么。函数调用的五步流程可以直接参考 OpenAI 的官方结构：定义工具 → 模型返回 tool call → 应用执行 → 回传结果 → 模型继续回答。citeturn1search13
- 填知识树节点：`Tokens_Context_Window.md`

#### 晚上 2h
- 做一个最小实验：
  - 同一个问题，分别给短上下文和很长上下文
  - 观察输出是否跑偏
- 记录：上下文预算不足时，哪些信息应该进 prompt，哪些应交给检索 / 工具

---

### Day 2（周二）
#### 早上 2h
- 填：`Prompting.md`
- 重点写清边界：
  - Prompt 主要解决“行为引导”，不是知识补充
  - Prompt 不是确定性程序

#### 晚上 2h
- 做一个 prompt 优化实验：
  - 原始 prompt → 改写 prompt → 对比输出差异
- 写一个 prompt 失败案例复盘

---

### Day 3（周三）
#### 早上 2h
- 填：`Structured_Output.md`
- 重点整理：
  - 为什么“请输出 JSON”不等于结构化输出
  - 为什么 schema / 校验更稳。OpenAI 推荐尽量通过严格 schema 提升输出稳定性；LangChain 也支持结构化 agent 输出。citeturn1search13turn1search7

#### 晚上 2h
- 做一个结构化输出 demo：
  - 模型返回 `summary / confidence / next_action`
- 用 Pydantic 或其他校验方式做格式检查

---

### Day 4（周四）
#### 早上 2h
- 填：`Function_Calling_Basics.md`
- 自己画一张 tool calling 流程图：
  - user → model → tool call → app execute → tool result → model

#### 晚上 2h
- 实现一个最小工具：
  - 例子：`get_table_schema(table_name)` 或 `search_docs(query)`
- 目标：让模型真实调用一次工具并拿结果回答

---

### Day 5（周五）
#### 早上 2h
- 填：`Tools/Tool_Schema_Design.md`
- 重点写：
  - clear name / description / parameters / strict mode / enum / required
- OpenAI 强调 schema 清晰度和 strict mode 对函数调用稳定性很关键，Anthropic 也指出工具说明质量往往比很多人想象中更重要。citeturn1search13turn1search1

#### 晚上 2h
- 优化昨天的工具 schema
- 对比：坏 schema vs 好 schema 的效果差异

---

### Day 6（周六，8h）
#### 上午 3h
- 回填模型层和工具层节点
- 画一张总图：`User -> LLM -> Tool -> Backend -> Result -> LLM`

#### 下午 3h
- 做 mini project v1：
  - “数据表说明助手” 或 “元数据小助手”
  - 用户提问 → 模型调用 `get_table_schema` → 返回解释

#### 晚上 2h
- 写 `One_Page_Tool_Calling.md`
- 列出本周至少 3 个失败案例

---

### Day 7（周日，8h）
#### 上午 3h
- 闭眼重建：什么是 tool calling？它和 agent 有什么区别？

#### 下午 3h
- 给 mini project 再加一个工具：
  - 例如 `search_owner(table_name)`
- 尝试控制工具边界（例如 allowed tools）citeturn1search13

#### 晚上 2h
- 周复盘：
  - 我能否脱稿讲 clear schema 的原则？
  - 我能否独立解释“模型与工具的边界”？

---

# 4. 第 2 周：RAG 系统

## 4.1 本周目标
- 按 LlamaIndex 的 RAG 五阶段，把 RAG 拆解为完整系统：Loading / Indexing / Storing / Querying / Evaluation。citeturn1search26
- 理解 Azure 在企业 RAG 中强调的内容：chunking、hybrid search、semantic ranking、安全过滤、token constraints、response time。citeturn1search33
- 做一个带来源引用的 mini RAG demo

## 4.2 本周输出物
- 已填节点：
  - `RAG/Loading.md`
  - `RAG/Chunking.md`
  - `RAG/Embeddings.md`
  - `RAG/Indexing.md`
  - `RAG/Retrieval.md`
  - `RAG/Rerank.md`
  - `RAG/Hybrid_Search.md`
  - `RAG/Security_Trimming.md`
  - `RAG/Evaluation.md`
- 一个 mini RAG demo：企业文档问答（带来源）
- 一页纸：`One_Page_RAG.md`

---

## 4.3 每日计划

### Day 8（周一）
#### 早上 2h
- 先画 RAG 总图：
  - Loading → Chunking → Embedding → Index → Retrieve → Rerank → Generate → Evaluate
- 填：`RAG/Loading.md`、`RAG/Indexing.md`

#### 晚上 2h
- 准备一个小语料库：
  - 10~20 篇文档
  - 尽量与你的元数据、数据治理、runbook 场景相关

---

### Day 9（周二）
#### 早上 2h
- 专门填：`RAG/Chunking.md`
- 对比不同 chunking 策略

#### 晚上 2h
- 做实验：
  - 固定大小切块 vs 按标题层级切块
  - 同一 query 比较召回质量

---

### Day 10（周三）
#### 早上 2h
- 填：`RAG/Embeddings.md`、`RAG/Indexing.md`
- 写清楚：embedding 解决的是语义相似问题，但 embedding 好不等于整个 RAG 就好。citeturn1search26

#### 晚上 2h
- 做最小索引检索 demo：
  - 输入 query
  - 返回 top-k chunks
- 暂时不接 LLM，只检视检索质量

---

### Day 11（周四）
#### 早上 2h
- 填：`RAG/Retrieval.md`、`RAG/Rerank.md`、`RAG/Hybrid_Search.md`
- 重点整理 hybrid search 与 semantic ranking 的作用。Azure 明确建议企业 RAG 使用 hybrid queries 和 semantic ranking 来提升 recall 与 relevance。citeturn1search33

#### 晚上 2h
- 做实验：
  - 纯向量检索 vs 关键词检索 vs hybrid
- 记录：哪些 query 上 hybrid 明显更稳

---

### Day 12（周五）
#### 早上 2h
- 填：`RAG/Security_Trimming.md`、`RAG/Evaluation.md`
- 重点写：
  - 企业 RAG 为什么必须考虑权限继承 / 过滤
  - RAG 应该评估哪些维度（召回、忠实性、成本、延迟）

#### 晚上 2h
- 建一个最小评测集：
  - 10 个问题
  - 标准来源 / 标准答案 / 边界情况

---

### Day 13（周六，8h）
#### 上午 3h
- 完成 mini RAG v1：
  - 文档入库
  - 检索 + 生成
  - 返回来源片段

#### 下午 3h
- 再加一层优化：
  - rerank / hybrid / query rewrite 三选一

#### 晚上 2h
- 写：`One_Page_RAG.md`
- 画一张完整 RAG 架构图

---

### Day 14（周日，8h）
#### 上午 3h
- 闭眼重建：
  - RAG 五阶段是什么？
  - 哪一阶段最容易失败？

#### 下午 3h
- 尝试把 RAG 与第 1 周的工具结合：
  - 检索不到时，允许调用一个辅助工具

#### 晚上 2h
- 周复盘：
  - 写 5 个 RAG 高频故障场景
  - 更新知识树节点

---

# 5. 第 3 周：Workflow / Agent 编排层

## 5.1 本周目标
- 建立 workflow / agent 边界感。Anthropic 明确区分：workflow 是预定义代码路径，agent 是模型动态决定流程和工具使用。citeturn1search1
- 学会用五种经典 workflow 模式去理解复杂系统：
  - Prompt Chaining
  - Routing
  - Parallelization
  - Orchestrator-Workers
  - Evaluator-Optimizer citeturn1search1
- 借助 LangChain 的 runtime 思维理解 memory、middleware、HITL、subagent 等工程能力。citeturn1search7

## 5.2 本周输出物
- 已填节点：
  - `Workflow_vs_Agent.md`
  - `Prompt_Chaining.md`
  - `Routing.md`
  - `Parallelization.md`
  - `Orchestrator_Workers.md`
  - `Evaluator_Optimizer.md`
  - `Agent_Loop.md`
  - `Multi_Agent.md`
  - `Human_in_the_Loop.md`
- 一个编排 demo：planner / researcher / reviewer
- 一页纸：`One_Page_Agent.md`

---

## 5.3 每日计划

### Day 15（周一）
#### 早上 2h
- 只做一件事：填完整 `Workflow_vs_Agent.md`
- 写清楚：
  - 固定步骤适合 workflow
  - 开放式、步骤不可预测问题才更适合 agent

#### 晚上 2h
- 画两张图：
  - workflow 路径图
  - agent loop 图

---

### Day 16（周二）
#### 早上 2h
- 填：`Prompt_Chaining.md`、`Routing.md`

#### 晚上 2h
- 做一个路由 demo：
  - FAQ → 小模型问答路径
  - 检索问题 → RAG 路径
  - 高风险问题 → 人工路径

---

### Day 17（周三）
#### 早上 2h
- 填：`Parallelization.md`、`Orchestrator_Workers.md`
- Anthropic 明确指出 parallelization 适合独立子任务或投票，orchestrator-workers 适合子任务类型 / 数量不可预测。citeturn1search1

#### 晚上 2h
- 做一个 orchestrator mini-demo：
  - planner 拆任务
  - 两个 worker 并行
  - 汇总输出

---

### Day 18（周四）
#### 早上 2h
- 填：`Evaluator_Optimizer.md`
- 理解：generator + evaluator loop 更适合质量优先任务。citeturn1search1

#### 晚上 2h
- 做实验：
  - 初稿 → 评审 → 修改一轮

---

### Day 19（周五）
#### 早上 2h
- 填：`Agent_Loop.md`、`Human_in_the_Loop.md`、`Multi_Agent.md`
- LangChain 把 human-in-the-loop 与 subagents 当作 runtime 的一部分，非常适合建立工程组织感。citeturn1search7

#### 晚上 2h
- 实现一个最小 agent loop
- 在高风险工具前加人工确认模拟

---

### Day 20（周六，8h）
#### 上午 3h
- 做 mini project v2：
  - 把前两周的工具 / RAG demo 先串成 workflow

#### 下午 3h
- 再升级一版：
  - planner / researcher / reviewer 三角色

#### 晚上 2h
- 写：`One_Page_Agent.md`
- 给 5 种 workflow 模式各写一个业务例子

---

### Day 21（周日，8h）
#### 上午 3h
- 闭眼重建：
  - 5 种 workflow 模式
  - agent loop 最小结构
  - 什么时候不用 agent

#### 下午 3h
- 回看你前两周做的东西：
  - 判断它们到底是 workflow 还是 agent
  - 如果升级成 agent，需要增加什么能力

#### 晚上 2h
- 周复盘：
  - 我以前把哪些东西误叫成 agent？
  - 我以后如何做架构取舍？

---

# 6. 第 4 周：生产层 + 项目整合

## 6.1 本周目标
- 建立 tracing / eval / guardrails / security / deployment 意识。OpenAI 的建议是：先 trace，再 graders，再 datasets 与 eval runs；Phoenix 强调 tracing 是 agent 调试与迭代的前提。citeturn1search54turn1search39
- 补齐 Azure / MCP 强调的安全边界：权限控制、用户同意、工具调用审批、数据治理。citeturn1search33turn1search20
- 完成一个可写进简历的最终项目

## 6.2 本周输出物
- 已填节点：
  - `Tracing.md`
  - `Evaluation.md`
  - `Datasets_and_Graders.md`
  - `Guardrails.md`
  - `Security_and_Governance.md`
  - `Cost_and_Latency.md`
  - `Deployment.md`
- 一个最终项目（推荐三选一）：
  - `Metadata_Copilot.md`
  - `SQL_Agent.md`
  - `Data_Quality_Agent.md`
- 项目文档：README、架构图、评测集、Postmortem

---

## 6.3 每日计划

### Day 22（周一）
#### 早上 2h
- 填：`Tracing.md`
- 明确你需要记录哪些事件：prompt、retrieval、tool call、tool output、final answer、latency、token。Phoenix 和 LangChain 都强调要看到 agent 每一步发生了什么。citeturn1search39turn1search7

#### 晚上 2h
- 给现有项目加 tracing 记录字段

---

### Day 23（周二）
#### 早上 2h
- 填：`Evaluation.md`、`Datasets_and_Graders.md`
- 写一套最小评测框架：
  - 输入
  - 预期行为
  - 实际行为
  - 评分

#### 晚上 2h
- 做 20 条最小评测样本

---

### Day 24（周三）
#### 早上 2h
- 填：`Guardrails.md`、`Security_and_Governance.md`
- MCP 强调用户知情与同意、工具调用安全；Azure 强调企业 RAG 必须纳入访问控制与权限继承。citeturn1search20turn1search33

#### 晚上 2h
- 给项目加两类 guardrails：
  - 敏感信息过滤
  - 高风险动作审批

---

### Day 25（周四）
#### 早上 2h
- 填：`Cost_and_Latency.md`、`Deployment.md`
- Anthropic 提醒 agentic systems 往往更贵、更慢；Azure 也把 token constraints / response time expectations 作为设计挑战。citeturn1search1turn1search33

#### 晚上 2h
- 画项目部署图：
  - API
  - 向量库 / 数据源
  - tracing / logs
  - config / secrets

---

### Day 26（周五）
#### 早上 2h
- 选最终项目题目（建议按背景优先选 `Metadata Copilot`）
- 新建项目文档节点

#### 晚上 2h
- 写项目设计初稿：
  - 需求
  - 架构
  - 能力拆分（RAG / Tools / Workflow / Agent / Eval / Security）

---

### Day 27（周六，8h）
#### 上午 3h
- 完成最终项目 v1：
  - 至少跑通：
    - RAG 或 Tool Calling
    - 一种编排（workflow / agent）
    - tracing
    - 最小 eval

#### 下午 3h
- 记录三类故障：
  - 模型层故障
  - 检索 / 工具故障
  - 编排 / 权限故障

#### 晚上 2h
- 写：`Postmortems.md`
- 输出 README + 架构图

---

### Day 28（周日，8h）
#### 上午 3h
- 回看整棵知识树：
  - 每层至少做 2 个节点的闭眼重建

#### 下午 3h
- 完成四份收口文档：
  - `One_Page_RAG.md`
  - `One_Page_Agent.md`
  - `One_Page_Tool_Calling.md`
  - `Interview_QA.md`

#### 晚上 2h
- 最终复盘：
  - 我现在最强的项目是什么？
  - 我还能讲清楚哪些能力？
  - 下一阶段应该补哪类节点？

---

# 7. 每周必须交付的成果

## 第 1 周交付
- 6 个知识树节点
- 1 个最小 tool calling demo
- 1 份 `One_Page_Tool_Calling.md`

## 第 2 周交付
- 9 个 RAG 节点
- 1 个最小 RAG demo
- 1 份 `One_Page_RAG.md`

## 第 3 周交付
- 9 个编排层节点
- 1 个 workflow / agent demo
- 1 份 `One_Page_Agent.md`

## 第 4 周交付
- 7 个生产层节点
- 1 个完整项目
- 1 套项目文档 + 失败案例 + Interview QA

---

# 8. 建议你选的最终项目

## 8.1 Metadata Copilot（最推荐）
这个项目最适合你的数据工程背景，因为它天然可以串起来：
- 文档 / 元数据检索（RAG）
- 查询 owner / 血缘 / 表结构（Tools）
- 多步解释流程（Workflow）
- 权限 / tracing / eval / 安全（Production）

## 8.2 SQL Agent
适合展示：
- schema-aware retrieval
- tool calling
- SQL 安全
- 执行前审批（HITL）
- 可解释性

## 8.3 Data Quality Agent
特别适合你过去的数据质量、数据管道、任务排障经验：
- 查日志 / 告警 / 指标 / runbook
- 检索历史 case
- 生成排障建议
- 高风险动作转人工

---

# 9. 这 4 周真正的目标

这份计划的目标不是“把所有内容看完”，而是每周都打通一个系统闭环：

- **第 1 周**：我能讲清 tool calling
- **第 2 周**：我能讲清 RAG
- **第 3 周**：我能讲清 workflow vs agent
- **第 4 周**：我能把它们做成一个有 tracing / eval / 安全意识的小系统

只要这 4 个闭环被打通，你的“学过一遍但没掌握”的状态就会明显改善。

---

# 10. 推荐执行方法（每天都遵守）

## 每天都问自己三个问题
1. 今天学的这个点，属于知识树哪一层？
2. 它解决什么问题，不解决什么问题？
3. 它最容易在哪些场景下失败？

## 每天都留下四类产物
- 一页纸总结
- 一张结构图
- 一个失败案例
- 一个最小 demo

---

> 最后提醒：
> 你现在最需要的，不是“更多内容”，而是“更强的结构化输出”。
> 这 4 周计划如果你认真执行，最大的变化不是你知道更多名词，而是你会真正开始拥有一张 **能解释、能复盘、能做项目、能面试表达** 的知识地图。
