# Grant 的 LLM / Agent 知识树模板（和 4 周计划对齐版）

> 用法：每天学完后，只填当天计划指定的节点。每个节点最多一页，宁愿短，也要完整。
>
> 这版不是“资料收藏夹”，而是你的理解账本：定义、边界、流程、失败、demo、面试表达。

---

## 0. 和学习计划的关系

学习计划回答：“今天做什么？”

知识树回答：“今天学到的东西放哪里？”

每天流程：

1. 打开学习计划当天卡片。
2. 看“知识树落点”。
3. 在本文件对应节点复制模板。
4. 只填当天要求的栏位。
5. 周末再补面试表达、架构师问题和项目落点。

不要每天把所有栏都填满。你会累，而且会写虚。

---

## 1. 知识树目录

```text
knowledge_tree/
  00_System_Map/
    Four_Layers.md
    Learning_Index.md
    Parking_Lot.md

  01_Model_Layer/
    Prompting.md
    Structured_Output.md
    Function_Calling_Basics.md
    Hallucination_Boundaries.md
    Tokens_Context_Window.md

  02_Augmentation_Layer/
    RAG/
      RAG_Overview.md
      Loading.md
      Chunking.md
      Indexing.md
      Embeddings.md
      Retrieval.md
      Hybrid_Search.md
      Rerank.md
      Citation_and_Faithfulness.md
      Security_Trimming.md
      RAG_Failure_Modes.md
      Evaluation.md
    Tools/
      Tool_Schema_Design.md
      Tool_Selection.md
      Tool_Safety.md
      MCP.md
    Memory/
      Short_Term_Memory.md
      Long_Term_Memory.md
      Session_State.md

  03_Orchestration_Layer/
    Workflow_vs_Agent.md
    Prompt_Chaining.md
    Routing.md
    Parallelization.md
    Orchestrator_Workers.md
    Evaluator_Optimizer.md
    Agent_Loop.md
    Multi_Agent.md
    Human_in_the_Loop.md

  04_Production_Layer/
    Tracing.md
    Evaluation.md
    Datasets_and_Graders.md
    Guardrails.md
    Security_and_Governance.md
    Cost_and_Latency.md
    Deployment.md
    Production_Review.md
```

---

## 2. Day 1-28 对齐表

| Day | 学习主题 | 必填知识树节点 | 当天先填哪些栏 |
|---|---|---|---|
| 1 | LLM 应用四层地图 | `00_System_Map/Four_Layers.md`，`03_Orchestration_Layer/Workflow_vs_Agent.md` | 定义、四层职责、边界、什么时候不用 agent |
| 2 | Prompt 的作用和边界 | `01_Model_Layer/Prompting.md` | 定义、解决什么、不解决什么、流程、失败模式 |
| 3 | Structured Output | `01_Model_Layer/Structured_Output.md` | 定义、schema 参数、结构化输出边界、校验失败 |
| 4 | Function / Tool Calling | `01_Model_Layer/Function_Calling_Basics.md`，`02_Augmentation_Layer/Tools/Tool_Selection.md` | 五步流程、模型/应用边界、何时调用工具 |
| 5 | Tool Schema 设计 | `02_Augmentation_Layer/Tools/Tool_Schema_Design.md`，`Tool_Safety.md` | name/description/parameters/required、误用和安全边界 |
| 6 | Week 1 mini project | Week 1 所有节点 | 最小 demo、项目落点、架构师问题 |
| 7 | ADR + NFR 复盘 | `04_Production_Layer/Cost_and_Latency.md`，Week 1 面试表达 | 成本/延迟来源、30 秒表达 |
| 8 | RAG 总流程 | `02_Augmentation_Layer/RAG/RAG_Overview.md`，`Loading.md` | RAG 五步、文档对象、metadata/source |
| 9 | Chunking | `02_Augmentation_Layer/RAG/Chunking.md`，`Indexing.md` | chunk 参数、metadata、切分失败 |
| 10 | Embeddings + Retrieval | `Embeddings.md`，`Retrieval.md` | embedding 定义、top_k、score、召回失败 |
| 11 | Hybrid Search + Rerank | `Hybrid_Search.md`，`Rerank.md` | keyword/vector 融合、重排位置、权重失败 |
| 12 | RAG Answer + Citation | `Citation_and_Faithfulness.md` | 引用规则、拒答规则、faithfulness 失败 |
| 13 | RAG 权限和失败模式 | `Security_Trimming.md`，`RAG_Failure_Modes.md` | 权限过滤、越权风险、RAG 5 个失败模式 |
| 14 | Week 2 mini project | Week 2 RAG 所有节点，`RAG/Evaluation.md` | 项目落点、架构师问题、RAG 初版评估指标 |
| 15 | Workflow vs Agent | `03_Orchestration_Layer/Workflow_vs_Agent.md` | 判断表、控制权、可调试性、成本 |
| 16 | Prompt Chaining | `Prompt_Chaining.md` | chain 流程、gate/check、链条失败 |
| 17 | Routing | `Routing.md` | route 设计、误判成本、router 输出格式 |
| 18 | Parallelization | `Parallelization.md` | sectioning/voting、成本和延迟 trade-off |
| 19 | Orchestrator-Workers | `Orchestrator_Workers.md` | orchestrator/worker 职责边界、合并失败 |
| 20 | Evaluator-Optimizer | `Evaluator_Optimizer.md`，`04_Production_Layer/Evaluation.md` 初版 | rubric、阈值、生成-评估-改写循环 |
| 21 | Week 3 mini project | Week 3 所有节点，`Agent_Loop.md` 初版 | 项目落点、面试表达、为什么暂不用 agent loop |
| 22 | Tracing | `04_Production_Layer/Tracing.md` | span、latency、input/output、error、隐私边界 |
| 23 | Evaluation | `Evaluation.md`，`Datasets_and_Graders.md`，`RAG/Evaluation.md` | dataset、grader、pass/fail/reason、RAG 指标 |
| 24 | Guardrails + Security | `Guardrails.md`，`Security_and_Governance.md` | 输入/工具/输出防线、资产、入口、剩余风险 |
| 25 | Cost + Latency | `Cost_and_Latency.md` | token/retrieval/rerank/workflow/tool I/O 成本和延迟 |
| 26 | Deployment | `Deployment.md` | runtime topology、配置、密钥、上线 checklist |
| 27 | Final Architecture Review | `Production_Review.md`，生产层相关节点 | 五支柱风险、检测、降级、修复动作 |
| 28 | 最终打包 + 面试表达 | 所有核心节点 | 30 秒版、2 分钟版、项目例子 |

---

## 3. 每个节点通用模板

复制下面模板到每个主题文件里。

```markdown
# 主题名

## 1. 一句话定义

## 2. 它属于哪一层
- Model / Augmentation / Orchestration / Production:

## 3. 它解决什么问题
- 

## 4. 它不解决什么问题
- 

## 5. 核心流程
1.
2.
3.

## 6. 关键设计参数
- 参数 1:
- 参数 2:
- 参数 3:

## 7. 常见失败模式
- 失败 1:
- 失败 2:
- 失败 3:

## 8. 最小 demo
- 文件:
- 输入:
- 过程:
- 输出:
- 我验证了什么:

## 9. 架构师问题
- 如果规模扩大 10 倍，哪里先坏？
- 如果要上线，最小 NFR 是什么？
- 有没有更简单方案？
- 代价是什么？

## 10. 面试表达
- 30 秒版:
- 2 分钟版:

## 11. 我自己的项目落点
- 放在哪个 demo:
- 为什么放这里:
- 和其他节点怎么连起来:

## 12. 参考链接
- 
```

---

## 4. 今天打开链接后到底看什么

不要把链接当教材从头读到尾。每个链接只摘这 4 类信息：

```markdown
## 链接阅读摘录
- 定义：它是什么？
- 边界：它不解决什么？
- 流程：它怎么工作？
- 失败：它什么时候会坏？
```

每个链接最多摘 8 行。超过 8 行说明你在搬运，不是在理解。

---

## 5. 每层学习重点

### 5.1 Model Layer

你要学会回答：

- 模型本身能做什么，不能做什么？
- prompt、structured output、function calling 分别解决不同层面的问题。
- 为什么“让模型听话”不能只靠 prompt？

优先节点：

- `Prompting.md`
- `Structured_Output.md`
- `Function_Calling_Basics.md`

可以后补节点：

- `Tokens_Context_Window.md`
- `Hallucination_Boundaries.md`

### 5.2 Augmentation Layer

你要学会回答：

- 外部知识、工具、记忆分别怎么增强模型？
- RAG 的每一步在哪里可能坏？
- 工具越强，权限边界为什么越重要？

优先节点：

- `RAG/RAG_Overview.md`
- `RAG/Loading.md`
- `RAG/Chunking.md`
- `RAG/Embeddings.md`
- `RAG/Retrieval.md`
- `RAG/Hybrid_Search.md`
- `RAG/Citation_and_Faithfulness.md`
- `RAG/Security_Trimming.md`
- `Tools/Tool_Schema_Design.md`
- `Tools/Tool_Selection.md`
- `Tools/Tool_Safety.md`

可以后补节点：

- `Tools/MCP.md`
- `Memory/Short_Term_Memory.md`
- `Memory/Long_Term_Memory.md`
- `Memory/Session_State.md`

### 5.3 Orchestration Layer

你要学会回答：

- workflow 和 agent 的边界是什么？
- prompt chaining、routing、parallelization、orchestrator-workers、evaluator-optimizer 各适合什么任务？
- 为什么很多时候先做 workflow 比先做 autonomous agent 更稳？

优先节点：

- `Workflow_vs_Agent.md`
- `Prompt_Chaining.md`
- `Routing.md`
- `Parallelization.md`
- `Orchestrator_Workers.md`
- `Evaluator_Optimizer.md`

可以后补节点：

- `Agent_Loop.md`
- `Multi_Agent.md`
- `Human_in_the_Loop.md`

### 5.4 Production Layer

你要学会回答：

- 系统能跑以后，如何让它可观察、可评估、可治理？
- trace、eval、guardrails、security、cost、deployment 分别卡在哪里？
- 架构评审如何用 Reliability / Security / Cost / Operational Excellence / Performance 五支柱组织？

优先节点：

- `Tracing.md`
- `Evaluation.md`
- `Datasets_and_Graders.md`
- `Guardrails.md`
- `Security_and_Governance.md`
- `Cost_and_Latency.md`
- `Deployment.md`
- `Production_Review.md`

---

## 6. 关键节点填写提示

### 6.1 `00_System_Map/Four_Layers.md`

今天不要写成百科。写成你的系统地图：

```markdown
# Four Layers

## 1. 一句话定义
LLM 应用可以拆成模型层、增强层、编排层、生产层；越往后越接近真实系统风险。

## 2. 四层分别管什么
- Model:
- Augmentation:
- Orchestration:
- Production:

## 3. 每层不解决什么
- Model 不解决:
- Augmentation 不解决:
- Orchestration 不解决:
- Production 不解决:

## 4. 我的 4 周项目怎么落到四层
- Week 1:
- Week 2:
- Week 3:
- Week 4:
```

### 6.2 `01_Model_Layer/Prompting.md`

必须写清楚 prompt 的边界：

```markdown
## 不解决什么问题
- 不保证事实正确。
- 不替代权限控制。
- 不替代结构化 schema 和本地校验。
- 不替代 eval。
```

### 6.3 `01_Model_Layer/Structured_Output.md`

重点不是“JSON”，而是“schema + 校验”：

```markdown
## 关键设计参数
- 字段名是否明确:
- required 是否必要:
- enum 是否能缩小空间:
- 嵌套是否过深:
- 本地校验怎么做:
```

### 6.4 `01_Model_Layer/Function_Calling_Basics.md`

必须写这句话：

```markdown
模型不执行工具。模型只选择工具和参数；应用负责执行工具、处理错误、把结果回传给模型。
```

### 6.5 `02_Augmentation_Layer/Tools/Tool_Schema_Design.md`

必须写“什么时候不该调用”：

```markdown
## 不该调用工具的情况
- 用户只是问概念，不需要外部状态。
- 参数不完整，应该先追问。
- 工具没有权限或不是白名单。
- 工具结果无法改善答案。
```

### 6.6 `02_Augmentation_Layer/RAG/RAG_Overview.md`

RAG 五步必须固定：

```markdown
Load -> Chunk -> Embed/Index -> Retrieve -> Generate with citations
```

必须写边界：

```markdown
RAG 不保证文档是新的，不保证检索一定召回正确片段，也不自动解决权限和忠实性问题。
```

### 6.7 `02_Augmentation_Layer/RAG/Chunking.md`

必须写这 4 个失败：

- chunk 太大：召回不准、上下文浪费。
- chunk 太小：语义断裂。
- 切断表格或代码：答案错误。
- 丢 metadata：无法 citation 或权限过滤。

### 6.8 `02_Augmentation_Layer/RAG/Retrieval.md`

必须区分：

```markdown
keyword match 更擅长精确词、编号、人名、日期。
semantic similarity 更擅长意思相近但词不同的问题。
```

### 6.9 `02_Augmentation_Layer/RAG/Citation_and_Faithfulness.md`

必须写拒答规则：

```markdown
如果 top chunks 里没有支持答案的证据，就回答不知道，并说明缺少哪类资料。
```

### 6.10 `03_Orchestration_Layer/Workflow_vs_Agent.md`

必须有判断表：

| 问题 | 更适合 workflow | 更适合 agent |
|---|---|---|
| 步骤是否固定 | 固定 | 动态 |
| 是否需要模型规划下一步 | 不需要 | 需要 |
| 可调试性要求 | 高 | 可接受更复杂 |
| 成本预算 | 紧 | 可接受更高 |
| 失败风险 | 需要可控 | 可以探索 |

### 6.11 `03_Orchestration_Layer/Evaluator_Optimizer.md`

必须写适用条件：

- 有清楚评价标准。
- 迭代确实可能改善。
- 可以接受额外延迟和成本。
- 输出可被 rubric 判断。

### 6.12 `04_Production_Layer/Tracing.md`

必须写这些 span：

- request
- retrieval
- tool_call
- llm_call
- final_answer
- error

### 6.13 `04_Production_Layer/Evaluation.md`

必须写：

```markdown
Eval 不是“我感觉回答还行”，而是用固定 case、固定 grader、固定指标反复跑。
```

### 6.14 `04_Production_Layer/Guardrails.md`

必须把 guardrail 放到 3 个位置：

- 输入前：拦截危险请求或明显 prompt injection。
- 工具前：白名单、权限、参数校验。
- 输出后：引用检查、敏感信息检查。

### 6.15 `04_Production_Layer/Production_Review.md`

最终用五支柱填：

```markdown
# Production Review

## Reliability
- 最可能失败的组件:
- 检测方式:
- 降级方案:

## Security
- 最大越权风险:
- 缓解措施:
- 剩余风险:

## Cost
- 最贵步骤:
- 控制手段:
- 预算上限:

## Operational Excellence
- trace:
- eval:
- log:
- incident 定位:

## Performance
- P95 目标:
- 最慢步骤:
- 优化方式:
```

---

## 7. 每日学习日志模板

```markdown
# Dxx Learning Log

## 今日主题

## 今天必须弄懂的问题
1.
2.
3.

## 读了哪些链接
- 

## 我自己的 5 条理解
1.
2.
3.
4.
5.

## 今天更新了知识树哪个节点
- 

## 今天只填了哪些栏
- 

## 今天的最小 demo
- 文件:
- 输入:
- 输出:
- 证明了什么:

## 今天的失败 case

## 明天继续的问题
```

---

## 8. ADR 模板

```markdown
# ADR-00x: 决策标题

## Status
Proposed / Accepted / Superseded

## Context
现在遇到什么问题？约束是什么？

## Options
1. 方案 A
2. 方案 B
3. 方案 C

## Decision
最终选择什么？

## Why
为什么这个选择适合当前阶段？

## Trade-offs
- 得到什么:
- 牺牲什么:
- 哪些场景下以后要重选:

## Consequences
- 对代码:
- 对成本:
- 对安全:
- 对运维:
```

---

## 9. NFR 五支柱检查模板

```markdown
# Wx NFR Checklist

## Reliability
- 单点故障在哪里？
- 失败时如何降级？
- 是否有重试和超时？

## Security
- 用户能看到不该看的数据吗？
- 工具调用是否有权限边界？
- 日志是否会泄露敏感信息？

## Cost
- 单请求成本来自哪里？
- 哪一步最贵？
- 有没有预算上限？

## Operational Excellence
- 是否有 trace？
- 是否有 eval dataset？
- 出错后如何定位？

## Performance Efficiency
- P95 延迟目标是多少？
- 哪一步最慢？
- 是否能并行或缓存？
```

---

## 10. Failure Mode Analysis 模板

```markdown
# Failure Mode Analysis

| 组件 | 失败模式 | 影响 | 检测方式 | 降级方案 | 修复动作 |
|---|---|---|---|---|---|
| LLM | API 超时 | 用户无响应 | trace error | fallback model / 重试 | 限流与超时 |
| Retriever | 召回错误 | 答案不相关 | eval fail | 返回不知道 | 调 chunk / hybrid |
| Vector Store | 查询慢 | 延迟升高 | latency span | 降低 top_k | 索引优化 |
| Tool | 参数错误 | 执行失败 | tool error | 让模型重试一次 | schema 改清楚 |
| Logging | 泄露敏感信息 | 安全风险 | log scan | mask/redact | 日志脱敏 |
```

---

## 11. Threat Model 模板

```markdown
# Threat Model

## 1. 资产
- 用户数据:
- 文档内容:
- 工具权限:
- 日志与 trace:

## 2. 入口
- 用户输入:
- 检索文档:
- 工具返回:
- 外部 API:

## 3. 风险
| 风险 | 攻击路径 | 影响 | 缓解措施 | 剩余风险 |
|---|---|---|---|---|
| Prompt injection | 恶意文档影响回答 | 越权/误导 | 文档隔离 + 引用检查 | 中 |
| Sensitive disclosure | 日志保存原文 | 隐私泄露 | redact/mask | 低 |
| Excessive agency | 工具权限过大 | 误操作 | 工具白名单 + 人审 | 中 |
```

---

## 12. 面试表达模板

```markdown
# Interview QA - 主题

## 问题

## 30 秒版

## 2 分钟版

## 项目例子

## 常见追问
1.
2.
3.

## 容易说错的点
```

---

## 13. 官方链接按节点分配

### Prompting

- [OpenAI Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering)
- [Anthropic Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)

### Structured Output

- [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)

### Function / Tool Calling

- [OpenAI Function calling](https://developers.openai.com/api/docs/guides/function-calling)
- [Anthropic Tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- [Anthropic Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)

### RAG

- [LlamaIndex Introduction to RAG](https://developers.llamaindex.ai/python/framework/understanding/rag/)
- [LlamaIndex Querying](https://developers.llamaindex.ai/python/framework/module_guides/querying/)
- [OpenAI Embeddings](https://developers.openai.com/api/docs/guides/embeddings)
- [Azure AI Search: RAG overview](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)
- [Azure AI Search: Hybrid search](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview)
- [Azure AI Search: Semantic ranking](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview)
- [Azure AI Search: Security trimming](https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search)

### Workflow / Agent

- [Anthropic Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [OpenAI Agents SDK overview](https://developers.openai.com/api/docs/guides/agents)
- [LangChain Agents](https://docs.langchain.com/oss/python/langchain/agents)
- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)

### MCP

- [Model Context Protocol intro](https://modelcontextprotocol.io/docs/getting-started/intro)

### Tracing / Evaluation

- [OpenAI Evals](https://developers.openai.com/api/docs/guides/evals)
- [Phoenix Tracing overview](https://arize.com/docs/phoenix/tracing/llm-traces)
- [Phoenix Tracing how-to](https://arize.com/docs/phoenix/tracing/how-to-tracing)
- [Ragas metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)

### Architecture / Security

- [C4 model](https://c4model.com/)
- [ADR examples and templates](https://github.com/architecture-decision-record/architecture-decision-record)
- [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)
- [Azure AI workload documentation](https://learn.microsoft.com/en-us/azure/well-architected/ai/)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

---

## 14. 知识树维护原则

- 每个节点只保留自己的理解，不堆链接。
- 链接统一放到“参考链接”小节。
- 每个节点必须写边界和失败模式。
- 每天只填计划指定节点，不临时扩展新节点。
- 每周至少把一个 demo 反向链接到知识树节点。
- 任何新概念先放到 `00_System_Map/Parking_Lot.md`，周末再决定是否纳入知识树。
- 如果一个节点超过一页，删掉资料摘录，保留自己的判断。
