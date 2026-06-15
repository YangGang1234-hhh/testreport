# Grant 的 4 周 LLM / Agent 系统化学习计划（知识树对齐执行版）

> 目标不是“看完很多链接”，而是 4 周后拿出一套可讲、可跑、可复盘的 AI 应用小型架构案例。
>
> 这版已经和知识树模板对齐：每天都写清楚要学什么、读链接时抓什么、填哪个知识树节点、demo 验证什么。

---

## 0. 这版怎么用

每天只按当天卡片做 5 件事：

1. 看“今天必须弄懂的问题”。
2. 打开 P0 链接，只找当天指定信息。
3. 写 `notes/Dxx_xxx.md` 学习日志。
4. 更新当天指定的 `knowledge_tree/...` 节点。
5. 做最小 demo 或架构产物。

不要从链接开始乱逛。先看当天问题，再去资料里找答案。

---

## 1. 时间安排

工作日 4 小时：

- 40 分钟：读 P0 链接，只回答当天问题。
- 25 分钟：闭眼重建，写 5 条自己的理解。
- 35 分钟：填写知识树节点，只填当天指定栏位。
- 20 分钟：回答当天架构师问题。
- 70 分钟：做最小 demo。
- 25 分钟：记录失败 case 或 bug。
- 25 分钟：写当天学习日志或更新 ADR/NFR/FMA。

周末 6 到 8 小时：

- 2 到 3 小时：整合本周 mini project。
- 1 到 2 小时：补架构图。
- 1 到 2 小时：写 ADR / NFR / FMA / Threat Model。
- 1 小时：周复盘和面试表达。

学不动的 90 分钟版本：

- 20 分钟：只读 P0 链接。
- 20 分钟：写 5 条闭眼重建。
- 30 分钟：做一个能跑的最小 demo 或伪代码。
- 20 分钟：填知识树节点的定义、边界、失败模式。

---

## 2. 目录和产物

建议目录：

```text
LLM-Agent-4Week/
  knowledge_tree/
    00_System_Map/
    01_Model_Layer/
    02_Augmentation_Layer/
    03_Orchestration_Layer/
    04_Production_Layer/
  notes/
  demos/
  architecture/
  adr/
  nfr/
  fma/
  security/
  eval/
```

每天至少有 2 个产物：

- 学习日志：`notes/Dxx_topic.md`
- 知识树节点：当天卡片里指定的 `knowledge_tree/...`

有 demo 的日子再加：

- demo 文件：`demos/Dxx_xxx.py`

周末整合日再加：

- 架构图、ADR、NFR、FMA、Threat Model 或最终 README。

---

## 3. 每天统一填法

### 3.1 学习日志填法

每天新建一个 `notes/Dxx_topic.md`，用这个结构：

```markdown
# Dxx - 主题

## 今天必须弄懂的问题
1.
2.
3.

## 我自己的 5 条理解
1.
2.
3.
4.
5.

## 今天更新的知识树节点
- 

## 今天的最小 demo
- 文件:
- 输入:
- 输出:
- 证明了什么:

## 今天的失败 case

## 明天继续追的问题
```

### 3.2 知识树节点填法

不是每天都要把节点全部填满。当天卡片会写“今天只填哪几栏”。

优先填这 6 栏：

- 一句话定义
- 解决什么问题
- 不解决什么问题
- 核心流程
- 常见失败模式
- 最小 demo 或项目落点

周末再补：

- 关键设计参数
- 架构师问题
- 面试表达
- 参考链接

### 3.3 每天读资料只抓 4 类信息

- 定义：它是什么？
- 边界：它不解决什么？
- 流程：它怎么工作？
- 失败：什么时候会坏？

每个链接最多摘 8 行，不复制长段原文。

---

## 4. 28 天总对齐表

| Day | 主题 | 知识树节点 | 当天核心产物 |
|---|---|---|---|
| 1 | LLM 应用四层地图 | `00_System_Map/Four_Layers.md`，`03_Orchestration_Layer/Workflow_vs_Agent.md` | `notes/D01_four_layers.md` |
| 2 | Prompt 的作用和边界 | `01_Model_Layer/Prompting.md` | `notes/D02_prompting.md` |
| 3 | Structured Output | `01_Model_Layer/Structured_Output.md` | `demos/D03_structured_output.py` |
| 4 | Function / Tool Calling | `01_Model_Layer/Function_Calling_Basics.md`，`02_Augmentation_Layer/Tools/Tool_Selection.md` | `demos/D04_tool_calling.py` |
| 5 | Tool Schema 设计 | `02_Augmentation_Layer/Tools/Tool_Schema_Design.md`，`02_Augmentation_Layer/Tools/Tool_Safety.md` | `notes/D05_tool_schema_design.md` |
| 6 | Week 1 mini project | 回填 Week 1 所有工具节点 | `demos/week1_tool_calling_assistant.py`，`architecture/W1_System_Context.md` |
| 7 | Week 1 复盘 + ADR | `04_Production_Layer/Cost_and_Latency.md`，Week 1 节点面试表达 | `adr/ADR-001-single-llm-tool-calling-first.md` |
| 8 | RAG 总流程 | `02_Augmentation_Layer/RAG/RAG_Overview.md`，`Loading.md` | `demos/D08_load_docs.py` |
| 9 | Chunking | `02_Augmentation_Layer/RAG/Chunking.md`，`Indexing.md` | `demos/D09_chunking.py` |
| 10 | Embeddings + Retrieval | `02_Augmentation_Layer/RAG/Embeddings.md`，`Retrieval.md` | `demos/D10_retrieval.py` |
| 11 | Hybrid Search + Rerank | `02_Augmentation_Layer/RAG/Hybrid_Search.md`，`Rerank.md` | `demos/D11_hybrid_search.py` |
| 12 | RAG Answer + Citation | `02_Augmentation_Layer/RAG/Citation_and_Faithfulness.md` | `demos/D12_rag_answer_citations.py` |
| 13 | RAG 权限和失败模式 | `02_Augmentation_Layer/RAG/Security_Trimming.md`，`RAG_Failure_Modes.md` | `fma/W2_RAG_Failure_Mode_Analysis.md` |
| 14 | Week 2 mini project | 回填 Week 2 RAG 节点 | `demos/week2_mini_rag.py`，`architecture/W2_Container_Diagram.md` |
| 15 | Workflow vs Agent | `03_Orchestration_Layer/Workflow_vs_Agent.md` | `demos/D15_workflow_basics.py` |
| 16 | Prompt Chaining | `03_Orchestration_Layer/Prompt_Chaining.md` | `demos/D16_prompt_chaining.py` |
| 17 | Routing | `03_Orchestration_Layer/Routing.md` | `demos/D17_routing.py` |
| 18 | Parallelization | `03_Orchestration_Layer/Parallelization.md` | `demos/D18_parallel_review.py` |
| 19 | Orchestrator-Workers | `03_Orchestration_Layer/Orchestrator_Workers.md` | `demos/D19_orchestrator_workers.py` |
| 20 | Evaluator-Optimizer | `03_Orchestration_Layer/Evaluator_Optimizer.md` | `demos/D20_evaluator_optimizer.py` |
| 21 | Week 3 mini project | 回填 Week 3 编排节点 | `demos/week3_agentic_workflow_reviewer.py` |
| 22 | Tracing | `04_Production_Layer/Tracing.md` | `demos/D22_trace_logger.py` |
| 23 | Evaluation | `04_Production_Layer/Evaluation.md`，`Datasets_and_Graders.md` | `eval/eval_cases.jsonl` |
| 24 | Guardrails + Security | `04_Production_Layer/Guardrails.md`，`Security_and_Governance.md` | `demos/D24_guardrails.py` |
| 25 | Cost + Latency | `04_Production_Layer/Cost_and_Latency.md` | `demos/D25_cost_latency_report.py` |
| 26 | Deployment | `04_Production_Layer/Deployment.md` | `architecture/W4_Deployment_Diagram_Draft.md` |
| 27 | Final Architecture Review | `04_Production_Layer/Production_Review.md` | `nfr/W4_NFR_Checklist.md`，`security/W4_Threat_Model.md` |
| 28 | 最终打包 + 面试表达 | 所有核心节点的面试表达栏 | `README_Final.md`，`notes/Interview_QA.md` |

---

## 5. 官方链接索引

### 模型层

- P0 [OpenAI Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering)
- P0 [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- P0 [OpenAI Function calling](https://developers.openai.com/api/docs/guides/function-calling)
- P0 [OpenAI Embeddings](https://developers.openai.com/api/docs/guides/embeddings)
- P1 [Anthropic Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- P1 [Anthropic Tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)

### RAG 与增强层

- P0 [LlamaIndex Introduction to RAG](https://developers.llamaindex.ai/python/framework/understanding/rag/)
- P0 [LlamaIndex Querying](https://developers.llamaindex.ai/python/framework/module_guides/querying/)
- P0 [Azure AI Search: RAG overview](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)
- P0 [Azure AI Search: Hybrid search](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview)
- P0 [Azure AI Search: Security trimming](https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search)
- P1 [Ragas metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)

### Workflow / Agent 层

- P0 [Anthropic Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- P0 [OpenAI Agents SDK overview](https://developers.openai.com/api/docs/guides/agents)
- P0 [LangChain Agents](https://docs.langchain.com/oss/python/langchain/agents)
- P0 [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
- P1 [Model Context Protocol intro](https://modelcontextprotocol.io/docs/getting-started/intro)

### 生产与架构层

- P0 [OpenAI Evals](https://developers.openai.com/api/docs/guides/evals)
- P0 [Phoenix Tracing overview](https://arize.com/docs/phoenix/tracing/llm-traces)
- P0 [Phoenix Tracing how-to](https://arize.com/docs/phoenix/tracing/how-to-tracing)
- P0 [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)
- P0 [Azure AI workload documentation](https://learn.microsoft.com/en-us/azure/well-architected/ai/)
- P0 [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- P0 [C4 model](https://c4model.com/)
- P1 [ADR examples and templates](https://github.com/architecture-decision-record/architecture-decision-record)

---

## 6. 第 1 周：模型层 + Tool Calling 基础

本周目标：搞清楚模型、prompt、结构化输出、tool calling 的边界；做出一个“单 LLM + 2 个只读工具”的最小闭环。

本周项目：`tool_calling_assistant`

本周交付：

- `demos/week1_tool_calling_assistant.py`
- `notes/One_Page_Tool_Calling.md`
- `architecture/W1_System_Context.md`
- `adr/ADR-001-single-llm-tool-calling-first.md`
- `nfr/W1_NFR_Checklist.md`
- `notes/Why_not_agent_first.md`

### Day 1：LLM 应用的四层地图

P0 链接：

- [OpenAI Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering)
- [Anthropic Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)，只找 workflow、agent、when not to use agents 相关内容。

今天必须弄懂的问题：

- 一个 LLM 应用为什么不能只看模型本身？
- 模型层、增强层、编排层、生产层分别管什么？
- workflow 和 agent 的区别是什么？
- 为什么第一天不要直接做 autonomous agent？
- 一个最小 LLM 应用的输入、处理、输出分别是什么？

读资料时具体找：

- Prompt engineering 里找“如何给模型任务、上下文、输出约束”。
- Building effective agents 里找“workflow 是固定流程，agent 是模型动态决定流程”的区别。
- 只摘能帮助你画四层地图的句子，不摘工具细节。

知识树落点：

- `knowledge_tree/00_System_Map/Four_Layers.md`
- `knowledge_tree/03_Orchestration_Layer/Workflow_vs_Agent.md`，今天只填初版。

今天只填这些栏：

- Four_Layers：一句话定义、四层分别解决什么、不解决什么、每层常见失败。
- Workflow_vs_Agent：一句话定义、workflow/agent 边界、什么时候不用 agent。

晚上 demo 验证：

- 写一个最小脚本：用户输入问题，返回自然语言答案。
- 没有 API key 就写 mock：输入问题，返回固定答案。
- demo 只证明一件事：LLM 应用最小闭环是“输入 -> 模型或 mock -> 输出”，不是 agent。

完成标准：

- `notes/D01_four_layers.md`
- `knowledge_tree/00_System_Map/Four_Layers.md`
- 能用 2 分钟讲清楚 workflow 和 agent 的区别。

### Day 2：Prompt 的作用和边界

P0 链接：

- [OpenAI Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering)
- P1 [Anthropic Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)

今天必须弄懂的问题：

- Prompt 到底是在控制什么？
- Prompt 能提升稳定性，但为什么不能保证正确性？
- 行为约束、知识补充、工具调用、输出格式分别应该放在哪里？
- 什么问题不该靠 prompt 硬压？
- 什么叫 prompt 失败 case？

读资料时具体找：

- 找“清楚任务、提供上下文、指定格式、给例子、拆复杂任务”的方法。
- 找“prompt 不能代替外部知识、权限控制、程序校验、eval”的边界。
- 如果看 Anthropic，只补充一个点：好 prompt 应该降低歧义。

知识树落点：

- `knowledge_tree/01_Model_Layer/Prompting.md`

今天只填这些栏：

- 一句话定义。
- 解决什么问题。
- 不解决什么问题。
- 核心流程：任务说明 -> 上下文 -> 约束 -> 输出格式 -> 检查。
- 常见失败模式：指令冲突、上下文不足、格式漂移、把安全交给 prompt。

晚上 demo 验证：

- 同一个任务写 3 个 prompt：宽松版、约束版、带反例版。
- 比较输出稳定性，而不是比较“哪个看起来更聪明”。
- 记录一个失败 case：模型没有按格式、误解任务、编造信息都可以。

完成标准：

- `notes/D02_prompting.md`
- `knowledge_tree/01_Model_Layer/Prompting.md`
- `notes/D02_prompt_failure_case.md`

### Day 3：Structured Output

P0 链接：

- [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)

今天必须弄懂的问题：

- Structured Output 和“叫模型输出 JSON”有什么区别？
- schema 在 AI 应用里解决什么问题？
- 为什么结构化输出后还要本地校验？
- 哪些字段应该 required，哪些字段可以 optional？
- schema 太复杂会带来什么问题？

读资料时具体找：

- 找 schema、strict、required fields、type constraints 的作用。
- 找结构化输出适合用在哪些地方：任务规划、分类、抽取、工具参数。
- 不要研究复杂框架，今天只要会设计一个小 schema。

知识树落点：

- `knowledge_tree/01_Model_Layer/Structured_Output.md`

今天只填这些栏：

- 一句话定义。
- 解决什么问题：让程序可解析、可校验。
- 不解决什么问题：不保证事实正确，不保证业务合理。
- 关键设计参数：schema 字段、required、enum、嵌套深度。
- 失败模式：字段缺失、类型错、schema 过宽、schema 过复杂。

晚上 demo 验证：

- 设计一个 `TaskPlan` schema。
- 输入自然语言需求，输出结构化 JSON。
- 加一层本地校验：缺字段就报错。

完成标准：

- `demos/D03_structured_output.py`
- `notes/D03_structured_output.md`
- `knowledge_tree/01_Model_Layer/Structured_Output.md`
- `notes/Why_structured_output_not_free_text.md`

### Day 4：Function / Tool Calling

P0 链接：

- [OpenAI Function calling](https://developers.openai.com/api/docs/guides/function-calling)
- [Anthropic Tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)

今天必须弄懂的问题：

- 模型为什么“不执行工具”，而是“选择工具和参数”？
- 应用程序在 tool calling 里负责什么？
- 一次 tool calling 的 5 步流程是什么？
- tool result 回传给模型后，模型为什么还要生成最终回答？
- tool calling 和 agent 是什么关系？

读资料时具体找：

- 找工具定义由哪些部分组成：name、description、parameters。
- 找调用流程：用户请求 -> 模型选择工具 -> 应用执行 -> 结果回传 -> 最终回答。
- 找工具调用失败时谁负责重试和处理错误。

知识树落点：

- `knowledge_tree/01_Model_Layer/Function_Calling_Basics.md`
- `knowledge_tree/02_Augmentation_Layer/Tools/Tool_Selection.md`

今天只填这些栏：

- Function_Calling_Basics：定义、核心流程、模型和应用的职责边界。
- Tool_Selection：什么时候该调用工具、什么时候不该调用工具、误选工具的失败模式。

晚上 demo 验证：

- 定义两个只读工具：`get_current_time()` 和 `search_local_notes(query)`。
- 让模型或 mock router 选择工具。
- 重点验证：工具执行在应用侧，模型只产生调用意图和参数。

完成标准：

- `demos/D04_tool_calling.py`
- `notes/D04_function_calling_basics.md`
- `knowledge_tree/01_Model_Layer/Function_Calling_Basics.md`

### Day 5：Tool Schema 设计

P0 链接：

- [OpenAI Function calling](https://developers.openai.com/api/docs/guides/function-calling)，只找 strict mode、parallel tool calls、tool schema 相关内容。
- [Anthropic Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)，只找工具设计建议。

今天必须弄懂的问题：

- 一个好工具 schema 为什么要“窄而清楚”？
- description 应该写给谁看？
- required 字段过多或过少分别会怎样？
- 工具什么时候不该被调用？
- 工具错误应该怎么返回给模型？

读资料时具体找：

- 找工具命名、参数描述、required、错误处理、并行调用限制。
- 找“工具越强，权限越要窄”的设计思想。
- 不看复杂 agent 框架，今天只研究 schema 质量。

知识树落点：

- `knowledge_tree/02_Augmentation_Layer/Tools/Tool_Schema_Design.md`
- `knowledge_tree/02_Augmentation_Layer/Tools/Tool_Safety.md`

今天只填这些栏：

- Tool_Schema_Design：定义、关键设计参数、失败模式、最小 demo。
- Tool_Safety：工具白名单、只读工具、危险操作、人审边界。

晚上 demo 验证：

- 设计一个容易误用的工具 schema。
- 再改成清晰版本。
- 用 3 个输入测试 mock router 是否更容易选对。

完成标准：

- `notes/D05_tool_schema_design.md`
- `notes/D05_tool_failure_case.md`
- `knowledge_tree/02_Augmentation_Layer/Tools/Tool_Schema_Design.md`

### Day 6：Week 1 mini project

P0 链接：

- [C4 model](https://c4model.com/)，只看 System Context diagram。

今天必须弄懂的问题：

- 这个小助手的系统边界在哪里？
- User、Assistant App、LLM Provider、Local Notes 分别是什么？
- 哪些东西在系统内，哪些是外部依赖？
- tool calling assistant 为什么还不是 autonomous agent？
- 最小可运行闭环是什么？

读资料时具体找：

- C4 只找 System Context diagram 的目的：展示系统和外部参与者关系。
- 不看 Container、Component、Deployment，后面再学。

知识树落点：

- 回填 Week 1 所有节点的“项目落点”栏。
- `knowledge_tree/00_System_Map/Four_Layers.md` 补“我的项目怎么落到四层”。

今天只填这些栏：

- 每个 Week 1 节点的“最小 demo”和“我自己的项目落点”。
- Four_Layers 的“架构师问题”。

全天 demo 验证：

- 整合 Day 1 到 Day 5，做 `tool_calling_assistant`。
- 用户可以问时间、查本地笔记、普通回答。
- 画 System Context：User、Assistant App、LLM Provider、Local Notes。

完成标准：

- `demos/week1_tool_calling_assistant.py`
- `architecture/W1_System_Context.md`
- Week 1 知识树节点都有项目落点。

### Day 7：Week 1 复盘 + ADR-001

P0 链接：

- [ADR examples and templates](https://github.com/architecture-decision-record/architecture-decision-record)
- [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)

今天必须弄懂的问题：

- 为什么先做 single LLM + tool calling，而不是 agent？
- 这个选择得到什么、牺牲什么？
- Week 1 小项目的可靠性、安全、成本、运维、性能风险分别是什么？
- tool calling 的本质怎么用 30 秒讲清楚？
- 如果要上线，最小 NFR 是什么？

读资料时具体找：

- ADR 只找 Context、Options、Decision、Trade-offs 的写法。
- Well-Architected 只找五支柱名字和每支柱要问的问题。

知识树落点：

- `knowledge_tree/04_Production_Layer/Cost_and_Latency.md`，今天只填 tool calling 成本。
- Week 1 相关节点补“面试表达”栏。

今天只填这些栏：

- Cost_and_Latency：tool calling 的成本来源、延迟来源、优化方法。
- Prompting、Structured_Output、Function_Calling_Basics、Tool_Schema_Design：补 30 秒面试表达。

当天产物：

- `adr/ADR-001-single-llm-tool-calling-first.md`
- `nfr/W1_NFR_Checklist.md`
- `notes/One_Page_Tool_Calling.md`
- `notes/Why_not_agent_first.md`

---

## 7. 第 2 周：RAG 系统

本周目标：做一个能引用来源的 mini RAG；理解 loading、chunking、embedding、indexing、retrieval、rerank、hybrid、security trimming、evaluation。

本周项目：`mini_rag_with_citations`

本周交付：

- `demos/week2_mini_rag.py`
- `notes/One_Page_RAG.md`
- `architecture/W2_Container_Diagram.md`
- `adr/ADR-002-rag-retrieval-strategy.md`
- `fma/W2_RAG_Failure_Mode_Analysis.md`
- `nfr/W2_NFR_Checklist.md`

### Day 8：RAG 总流程

P0 链接：

- [LlamaIndex Introduction to RAG](https://developers.llamaindex.ai/python/framework/understanding/rag/)
- [Azure AI Search: RAG overview](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)

今天必须弄懂的问题：

- RAG 解决的核心问题是什么？
- RAG 为什么不是“让模型记住文档”？
- Load、Chunk、Embed、Retrieve、Generate 每一步做什么？
- RAG 不解决什么问题？
- citation 为什么是 RAG 产品能力的一部分？

读资料时具体找：

- 找 RAG 的整体流程，不看高级优化。
- 找“外部知识、检索、上下文注入、生成”的关系。
- 找 Azure 文档里 provenance、citation、index、query 的概念。

知识树落点：

- `knowledge_tree/02_Augmentation_Layer/RAG/RAG_Overview.md`
- `knowledge_tree/02_Augmentation_Layer/RAG/Loading.md`

今天只填这些栏：

- RAG_Overview：定义、解决什么、不解决什么、核心流程。
- Loading：输入文档、metadata、source、doc_id 的作用。

晚上 demo 验证：

- 准备 3 个 Markdown 文档作为语料。
- 写 loader，把文档读成 `Document(id, text, source)`。
- 重点验证：RAG 的第一步是把外部资料变成可处理文档对象。

完成标准：

- `demos/D08_load_docs.py`
- `notes/D08_rag_overview.md`
- `knowledge_tree/02_Augmentation_Layer/RAG/RAG_Overview.md`

### Day 9：Chunking

P0 链接：

- [LlamaIndex Introduction to RAG](https://developers.llamaindex.ai/python/framework/understanding/rag/)，只找 loading、indexing、chunking 相关内容。

今天必须弄懂的问题：

- 为什么不能直接把整篇文档塞给模型？
- chunk 太大、太小分别有什么问题？
- overlap 为什么存在？
- metadata 为什么不能丢？
- 按固定长度、标题、段落切分各适合什么场景？

读资料时具体找：

- 找文档如何进入索引。
- 找 chunk 和 retrieval 质量的关系。
- 不研究复杂 parser，今天先会写简单 chunker。

知识树落点：

- `knowledge_tree/02_Augmentation_Layer/RAG/Chunking.md`
- `knowledge_tree/02_Augmentation_Layer/RAG/Indexing.md`

今天只填这些栏：

- Chunking：定义、参数、失败模式、最小 demo。
- Indexing：索引是什么、metadata 为什么要随 chunk 入库。

晚上 demo 验证：

- 实现简单 chunker：`chunk_size=500`，`overlap=80`。
- 每个 chunk 带 `source`、`doc_id`、`chunk_id`。
- 打印前 5 个 chunk，检查有没有丢来源。

完成标准：

- `demos/D09_chunking.py`
- `notes/D09_chunking.md`
- `knowledge_tree/02_Augmentation_Layer/RAG/Chunking.md`

### Day 10：Embeddings + Retrieval

P0 链接：

- [OpenAI Embeddings](https://developers.openai.com/api/docs/guides/embeddings)
- [LlamaIndex Querying](https://developers.llamaindex.ai/python/framework/module_guides/querying/)

今天必须弄懂的问题：

- embedding 的一句话定义是什么？
- keyword match 和 semantic similarity 有什么区别？
- retrieval 的输入输出分别是什么？
- top_k 是什么，为什么不是越大越好？
- 检索结果错了，最终答案会怎样？

读资料时具体找：

- Embeddings 只找“文本转向量”和“相似度检索”的概念。
- Querying 只找 query engine 或 retriever 如何返回相关片段。
- 不纠结模型型号，今天重点是 retrieval 机制。

知识树落点：

- `knowledge_tree/02_Augmentation_Layer/RAG/Embeddings.md`
- `knowledge_tree/02_Augmentation_Layer/RAG/Retrieval.md`

今天只填这些栏：

- Embeddings：定义、解决什么、不解决什么、失败模式。
- Retrieval：核心流程、top_k、score、常见失败。

晚上 demo 验证：

- 有 API key：调用 embedding，做向量相似度检索。
- 没有 API key：用 TF-IDF 或关键词计分做 mock retrieval。
- 重点验证：query 进来后，系统返回 top chunks，而不是直接回答。

完成标准：

- `demos/D10_retrieval.py`
- `notes/D10_embeddings_retrieval.md`
- `knowledge_tree/02_Augmentation_Layer/RAG/Retrieval.md`

### Day 11：Hybrid Search + Rerank

P0 链接：

- [Azure AI Search: Hybrid search](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview)
- [Azure AI Search: Semantic ranking](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview)

今天必须弄懂的问题：

- 什么时候纯向量检索不够？
- 编号、术语、人名、日期为什么更需要 keyword？
- hybrid search 如何融合 keyword 和 vector？
- rerank 在 retrieval 后面解决什么？
- 融合权重错了会有什么后果？

读资料时具体找：

- 找 hybrid search 的基本思想：keyword + vector。
- 找 semantic ranking 或 rerank 的位置：先召回，再重排。
- 不需要学 Azure 配置，只学架构位置。

知识树落点：

- `knowledge_tree/02_Augmentation_Layer/RAG/Hybrid_Search.md`
- `knowledge_tree/02_Augmentation_Layer/RAG/Rerank.md`

今天只填这些栏：

- Hybrid_Search：适用场景、核心流程、参数、失败模式。
- Rerank：输入、输出、为什么不能替代召回。

晚上 demo 验证：

- 把关键词分数和模拟向量分数融合。
- 输出 top 5，并解释为什么排第一。
- 改一次权重，观察排序变化。

完成标准：

- `demos/D11_hybrid_search.py`
- `notes/D11_hybrid_vs_vector.md`
- `knowledge_tree/02_Augmentation_Layer/RAG/Hybrid_Search.md`

### Day 12：RAG Answer + Citation

P0 链接：

- [Azure AI Search: RAG overview](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)，只找 citation、provenance、token constraints 相关内容。

今天必须弄懂的问题：

- RAG answer 为什么必须带来源？
- citation 和“看起来像引用”有什么区别？
- 什么时候应该回答“不知道”？
- 如何让答案只基于 retrieved chunks？
- context 太长时会发生什么？

读资料时具体找：

- 找 provenance、source、citation 的概念。
- 找 token constraint 对上下文拼接的影响。
- 不研究 UI，只研究答案生成规则。

知识树落点：

- `knowledge_tree/02_Augmentation_Layer/RAG/Citation_and_Faithfulness.md`
- `knowledge_tree/02_Augmentation_Layer/RAG/Retrieval.md` 补失败模式。

今天只填这些栏：

- Citation_and_Faithfulness：定义、回答模板、拒答规则、失败模式。
- Retrieval：补“检索错导致答案错”的项目例子。

晚上 demo 验证：

- 做 `ask(query)`：检索 top chunks -> 拼上下文 -> 生成答案。
- 无 API key 就先输出拼接式答案，重点验证 citations。
- 每条答案必须列 source 和 chunk_id。

完成标准：

- `demos/D12_rag_answer_citations.py`
- `notes/D12_rag_citation.md`
- `knowledge_tree/02_Augmentation_Layer/RAG/Citation_and_Faithfulness.md`

### Day 13：RAG 权限与失败模式

P0 链接：

- [Azure AI Search: Security trimming](https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

今天必须弄懂的问题：

- RAG 为什么会出现越权读取？
- security trimming 是在检索前、检索时还是生成后做？
- prompt injection 在 RAG 里怎么进入系统？
- RAG 最常见的 5 个失败模式是什么？
- 失败时应该如何检测和降级？

读资料时具体找：

- Azure 只找“按用户权限过滤检索结果”的思想。
- OWASP 只找 prompt injection、sensitive information disclosure、overreliance。
- 不看所有安全细节，今天只和 RAG 相关。

知识树落点：

- `knowledge_tree/02_Augmentation_Layer/RAG/Security_Trimming.md`
- `knowledge_tree/02_Augmentation_Layer/RAG/RAG_Failure_Modes.md`

今天只填这些栏：

- Security_Trimming：定义、权限标签、过滤位置、失败模式。
- RAG_Failure_Modes：文档过期、chunk 切坏、召回错误、权限丢失、编造引用。

晚上 demo 验证：

- 给文档加 `allowed_roles`。
- 检索时按 user role 过滤。
- 写一个越权测试：普通用户不能检索 admin 文档。

完成标准：

- `demos/D13_security_trimming.py`
- `fma/W2_RAG_Failure_Mode_Analysis.md`
- `knowledge_tree/02_Augmentation_Layer/RAG/Security_Trimming.md`

### Day 14：Week 2 mini project + Container Diagram

P0 链接：

- [C4 model](https://c4model.com/)，只看 Container diagram。

今天必须弄懂的问题：

- 一个 RAG 系统有哪些容器？
- API、Doc Store、Indexer、Vector Store、Retriever、LLM、Trace/Eval Store 分别负责什么？
- 当前检索策略为什么选 keyword、vector 或 hybrid？
- citation 和 security trimming 在系统里放在哪？
- Week 2 项目哪里最容易先坏？

读资料时具体找：

- C4 只找 Container diagram 如何表达系统内部主要容器。
- 不看 component 级别细节。

知识树落点：

- 回填 Week 2 RAG 节点的“项目落点”和“架构师问题”。
- `knowledge_tree/02_Augmentation_Layer/RAG/Evaluation.md` 填初版。

今天只填这些栏：

- 每个 RAG 节点补“最小 demo”和“项目落点”。
- RAG_Evaluation：先填评估什么，不必实现完整指标。

全天 demo 验证：

- 整合 Week 2，做 `mini_rag_with_citations`。
- 画 Container Diagram。
- 写 `ADR-002`：为什么当前采用 hybrid 或当前检索策略。

完成标准：

- `demos/week2_mini_rag.py`
- `architecture/W2_Container_Diagram.md`
- `adr/ADR-002-rag-retrieval-strategy.md`
- `notes/One_Page_RAG.md`

---

## 8. 第 3 周：Workflow / Agent 编排

本周目标：分清 workflow 和 agent，掌握 prompt chaining、routing、parallelization、orchestrator-workers、evaluator-optimizer；做一个可控 workflow，不急着做全自动 agent。

本周项目：`agentic_workflow_reviewer`

本周交付：

- `demos/week3_agentic_workflow_reviewer.py`
- `notes/One_Page_Agent.md`
- `architecture/W3_Dynamic_Diagram.md`
- `adr/ADR-003-workflow-over-autonomous-agent.md`
- `notes/W3_Architecture_Review_Questions.md`
- `nfr/W3_NFR_Checklist.md`

### Day 15：Workflow vs Agent

P0 链接：

- [Anthropic Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [OpenAI Agents SDK overview](https://developers.openai.com/api/docs/guides/agents)

今天必须弄懂的问题：

- workflow 和 agent 的控制权分别在哪里？
- 步骤固定和模型动态决策分别适合什么任务？
- 可调试性、成本、可靠性有什么差异？
- 什么场景应该先用 workflow？
- 什么场景才值得上 agent？

读资料时具体找：

- Anthropic 只找 workflow/agent 分类和选择原则。
- OpenAI Agents 只找 agent 的基本组成：model、tools、instructions、handoff 或 tracing 等概念。

知识树落点：

- `knowledge_tree/03_Orchestration_Layer/Workflow_vs_Agent.md`

今天只填这些栏：

- 定义、判断表、适用场景、不适用场景、失败模式。

晚上 demo 验证：

- 写一个硬编码三步 workflow：分类 -> 处理 -> 总结。
- 重点验证：workflow 的步骤是应用写死的，不是模型自由规划。

完成标准：

- `demos/D15_workflow_basics.py`
- `notes/D15_workflow_vs_agent.md`
- `knowledge_tree/03_Orchestration_Layer/Workflow_vs_Agent.md`

### Day 16：Prompt Chaining

P0 链接：

- [Anthropic Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)，只读 Prompt chaining。

今天必须弄懂的问题：

- prompt chaining 为什么要把复杂任务拆成多步？
- 每一步的输入输出应该怎么定义？
- gate/check 放在链中间解决什么？
- prompt chaining 的成本和延迟代价是什么？
- 链条太长会带来什么失败？

读资料时具体找：

- 找“一个任务拆成多个 LLM 调用”的适用条件。
- 找 gate 判断是否继续下一步。
- 不看 routing 和 parallelization，今天只看 chain。

知识树落点：

- `knowledge_tree/03_Orchestration_Layer/Prompt_Chaining.md`

今天只填这些栏：

- 定义、核心流程、适用条件、gate/check、失败模式。

晚上 demo 验证：

- 做“需求 -> 大纲 -> 详细方案 -> 自检”的链。
- 中间加格式检查 gate。
- 重点验证：中间产物可检查，失败可以停住。

完成标准：

- `demos/D16_prompt_chaining.py`
- `notes/D16_prompt_chaining.md`
- `knowledge_tree/03_Orchestration_Layer/Prompt_Chaining.md`

### Day 17：Routing

P0 链接：

- [Anthropic Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)，只读 Routing。

今天必须弄懂的问题：

- routing 解决什么问题？
- 路由误判的成本是什么？
- route 的数量为什么不能随便变多？
- route schema 应该输出什么？
- 路由失败如何检测和修复？

读资料时具体找：

- 找“根据输入类型选择下游路径”的思想。
- 找 routing 适合明显分流的任务。
- 不看 multi-agent，今天只做单 router。

知识树落点：

- `knowledge_tree/03_Orchestration_Layer/Routing.md`

今天只填这些栏：

- 定义、route 设计、误判成本、失败模式、最小 demo。

晚上 demo 验证：

- 设计 4 个 route：RAG 问答、代码生成、架构评审、闲聊拒绝。
- 写 router，输入问题，输出 route。
- 记录一个路由误判 case 和修复方法。

完成标准：

- `demos/D17_routing.py`
- `notes/D17_routing.md`
- `knowledge_tree/03_Orchestration_Layer/Routing.md`

### Day 18：Parallelization

P0 链接：

- [Anthropic Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)，只读 Parallelization。

今天必须弄懂的问题：

- sectioning 和 voting 有什么区别？
- 并行为什么可能降低总延迟，也可能增加成本？
- 哪些任务适合并行评审？
- 并行结果冲突时怎么合并？
- 并行检查漏掉共享上下文会怎样？

读资料时具体找：

- 找 parallelization 两种典型模式：拆不同部分、多个模型投票或检查。
- 找并行的 trade-off：速度、成本、一致性。

知识树落点：

- `knowledge_tree/03_Orchestration_Layer/Parallelization.md`

今天只填这些栏：

- 定义、两种模式、适用条件、成本/延迟 trade-off、失败模式。

晚上 demo 验证：

- 同一份方案并行做 3 个检查：安全、成本、可靠性。
- 合并为一个 review report。
- 重点验证：并行不是为了炫技，是为了独立检查或缩短墙钟时间。

完成标准：

- `demos/D18_parallel_review.py`
- `notes/D18_parallelization.md`
- `knowledge_tree/03_Orchestration_Layer/Parallelization.md`

### Day 19：Orchestrator-Workers

P0 链接：

- [Anthropic Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)，只读 Orchestrator-workers。
- P1 [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)

今天必须弄懂的问题：

- orchestrator 负责什么，worker 负责什么？
- worker 是不是 agent？
- 什么时候不应该拆 worker？
- orchestrator 如何合并 worker 输出？
- worker 输出格式不一致会怎样？

读资料时具体找：

- 找 orchestrator 根据任务动态拆分 worker 的模式。
- LangGraph 只看“graph/state/node/edge”概念，不写框架代码也可以。

知识树落点：

- `knowledge_tree/03_Orchestration_Layer/Orchestrator_Workers.md`

今天只填这些栏：

- 定义、职责边界、核心流程、失败模式、最小 demo。

晚上 demo 验证：

- orchestrator 根据任务拆成若干检查项。
- worker 分别输出。
- orchestrator 汇总成最终报告。

完成标准：

- `demos/D19_orchestrator_workers.py`
- `notes/D19_orchestrator_workers.md`
- `knowledge_tree/03_Orchestration_Layer/Orchestrator_Workers.md`

### Day 20：Evaluator-Optimizer

P0 链接：

- [Anthropic Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)，只读 Evaluator-optimizer。
- [OpenAI Evals](https://developers.openai.com/api/docs/guides/evals)

今天必须弄懂的问题：

- evaluator-optimizer 适合什么任务？
- 什么叫有清楚评分标准？
- 迭代优化为什么会增加延迟和成本？
- evaluator 和普通总结有什么区别？
- 什么时候不值得做多轮优化？

读资料时具体找：

- 找 evaluator-optimizer 的循环：生成 -> 评估 -> 改写。
- Evals 只找 dataset、grader、pass/fail 的思想。

知识树落点：

- `knowledge_tree/03_Orchestration_Layer/Evaluator_Optimizer.md`
- `knowledge_tree/04_Production_Layer/Evaluation.md` 初步记录。

今天只填这些栏：

- Evaluator_Optimizer：定义、适用条件、rubric、失败模式、最小 demo。
- Evaluation：先填“eval 为什么不是人工感觉”。

晚上 demo 验证：

- generator 生成答案。
- evaluator 按 rubric 打分。
- 低于阈值重写一次。

完成标准：

- `demos/D20_evaluator_optimizer.py`
- `notes/D20_evaluator_optimizer.md`
- `knowledge_tree/03_Orchestration_Layer/Evaluator_Optimizer.md`

### Day 21：Week 3 mini project + Dynamic Diagram

P0 链接：

- [C4 model](https://c4model.com/)，只看 Dynamic diagram。
- P1 [LangChain Agents](https://docs.langchain.com/oss/python/langchain/agents)

今天必须弄懂的问题：

- 一个可控 workflow 如何组合 routing、parallel review、summary、optimization？
- Dynamic Diagram 表达的是运行时交互，不是静态容器。
- 为什么这个项目仍然选择 workflow，而不是 autonomous agent？
- 哪些地方将来可以升级为 agent？
- 本周架构选择的 trade-off 是什么？

读资料时具体找：

- C4 只找 Dynamic diagram 如何表达一次请求流。
- LangChain Agents 只找 agent 的大致结构，用来对比，不急着用。

知识树落点：

- 回填 Week 3 编排节点的“项目落点”和“面试表达”。
- `knowledge_tree/03_Orchestration_Layer/Agent_Loop.md` 填初版，只写概念边界。

今天只填这些栏：

- Week 3 各节点补项目落点。
- Agent_Loop：只填什么是 loop、为什么本项目暂时不用。

全天 demo 验证：

- 整合 Week 3，做 `agentic_workflow_reviewer`。
- 它能对一个 AI 应用设计做：路由、并行评审、汇总、一次优化。
- 写 `ADR-003`：为什么用 workflow 而不是 autonomous agent。

完成标准：

- `demos/week3_agentic_workflow_reviewer.py`
- `architecture/W3_Dynamic_Diagram.md`
- `adr/ADR-003-workflow-over-autonomous-agent.md`
- `notes/One_Page_Agent.md`

---

## 9. 第 4 周：生产化 + 架构整合

本周目标：让项目从“能跑”变成“可观察、可评估、可治理、可解释”；补 tracing、eval、guardrails、security、cost、deployment。

本周项目：`production_ready_rag_agent_case`

本周交付：

- `demos/week4_production_ready_case/`
- `architecture/W4_Deployment_Diagram.md`
- `adr/ADR-004-trace-first-eval-strategy.md`
- `nfr/W4_NFR_Checklist.md`
- `security/W4_Threat_Model.md`
- `README_Final.md`
- `notes/Interview_QA.md`

### Day 22：Tracing

P0 链接：

- [Phoenix Tracing overview](https://arize.com/docs/phoenix/tracing/llm-traces)
- [Phoenix Tracing how-to](https://arize.com/docs/phoenix/tracing/how-to-tracing)

今天必须弄懂的问题：

- trace 和普通 log 有什么区别？
- 一次 AI 请求应该拆成哪些 span？
- retrieval、tool call、LLM call、final answer 分别记录什么？
- trace 如何帮助定位慢、错、贵？
- 哪些内容不应该原样进 trace？

读资料时具体找：

- 找 span、latency、input/output、error、metadata。
- 找 LLM trace 如何展示一次请求路径。
- 不要求今天真的接 Phoenix，可以先写本地 trace logger。

知识树落点：

- `knowledge_tree/04_Production_Layer/Tracing.md`

今天只填这些栏：

- 定义、核心 span、记录字段、失败模式、敏感信息边界。

晚上 demo 验证：

- 在 Week 2 或 Week 3 项目里加简易 trace logger。
- 至少记录 latency、输入、输出、错误、引用来源。

完成标准：

- `demos/D22_trace_logger.py`
- `notes/D22_tracing.md`
- `knowledge_tree/04_Production_Layer/Tracing.md`

### Day 23：Evaluation

P0 链接：

- [OpenAI Evals](https://developers.openai.com/api/docs/guides/evals)
- P1 [Ragas metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)

今天必须弄懂的问题：

- eval dataset 是什么？
- grader 是什么？
- pass/fail/reason 为什么比“感觉不错”更有用？
- RAG 要评估哪些指标？
- tool calling 要评估哪些指标？

读资料时具体找：

- OpenAI Evals 只找 dataset、grader、run、result 的思想。
- Ragas 只找 faithfulness、answer correctness、context precision/recall 的含义。

知识树落点：

- `knowledge_tree/04_Production_Layer/Evaluation.md`
- `knowledge_tree/04_Production_Layer/Datasets_and_Graders.md`
- `knowledge_tree/02_Augmentation_Layer/RAG/Evaluation.md` 补 RAG 指标。

今天只填这些栏：

- Evaluation：定义、指标、评估流程、失败模式。
- Datasets_and_Graders：case 格式、grader 输出、人工和自动评估边界。

晚上 demo 验证：

- 建 10 条最小 eval dataset。
- 指标先只用 4 个：answer correctness、faithfulness、citation correctness、tool choice accuracy。
- 写 evaluator，对每条 case 输出 pass/fail/reason。

完成标准：

- `eval/eval_cases.jsonl`
- `demos/D23_simple_eval_runner.py`
- `notes/D23_eval_strategy.md`

### Day 24：Guardrails + Security

P0 链接：

- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Azure AI workload documentation](https://learn.microsoft.com/en-us/azure/well-architected/ai/)

今天必须弄懂的问题：

- guardrail 是输入、工具、输出哪个位置的防线？
- prompt injection 怎么影响 RAG 或 tool calling？
- excessive agency 为什么危险？
- 工具白名单解决什么，不解决什么？
- 输出引用检查能防哪些问题？

读资料时具体找：

- OWASP 只找 prompt injection、sensitive disclosure、excessive agency、insecure tool/plugin、overreliance。
- Azure AI workload 只找 AI workload 的安全和治理问题。

知识树落点：

- `knowledge_tree/04_Production_Layer/Guardrails.md`
- `knowledge_tree/04_Production_Layer/Security_and_Governance.md`

今天只填这些栏：

- Guardrails：输入拦截、工具白名单、输出检查、失败模式。
- Security_and_Governance：资产、入口、权限边界、剩余风险。

晚上 demo 验证：

- 做 3 个 guardrail：输入危险操作拦截、工具白名单、输出引用检查。
- 写 3 个恶意或异常输入测试。

完成标准：

- `demos/D24_guardrails.py`
- `security/W4_Threat_Model_Draft.md`
- `knowledge_tree/04_Production_Layer/Guardrails.md`

### Day 25：Cost + Latency

P0 链接：

- [Phoenix Tracing overview](https://arize.com/docs/phoenix/tracing/llm-traces)，只找 latency、token、cost 相关能力。
- [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)

今天必须弄懂的问题：

- 单次 AI 请求的成本来自哪里？
- tokens、retrieval、rerank、多轮 workflow、工具 I/O 分别如何影响成本？
- 延迟来自哪些步骤？
- 串行和并行对延迟和成本有什么 trade-off？
- 怎么设置最小预算上限？

读资料时具体找：

- Phoenix 只找 latency 和 token/cost 可观测性。
- Well-Architected 只找 cost 和 performance 两个支柱。

知识树落点：

- `knowledge_tree/04_Production_Layer/Cost_and_Latency.md`

今天只填这些栏：

- 成本来源、延迟来源、关键参数、优化方法、失败模式。

晚上 demo 验证：

- 在 trace 里加 cost/latency summary。
- 给一次请求输出 `total_latency_ms`、`steps`、`estimated_cost_level`。

完成标准：

- `demos/D25_cost_latency_report.py`
- `notes/D25_cost_latency.md`
- `knowledge_tree/04_Production_Layer/Cost_and_Latency.md`

### Day 26：Deployment + Runtime Topology

P0 链接：

- [C4 model](https://c4model.com/)，只看 Deployment diagram。
- [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)

今天必须弄懂的问题：

- 开发机 demo 和上线运行拓扑有什么区别？
- Client、API、Worker、Vector DB、Doc Store、Trace Store、Eval Store、LLM Provider 分别部署在哪里？
- 密钥和配置怎么管理？
- 回滚、限流、日志、eval 在上线 checklist 里怎么体现？
- 哪些组件可以先 mock，哪些上线前必须真实？

读资料时具体找：

- C4 只找 Deployment diagram 如何表达运行节点和容器部署关系。
- Well-Architected 只找 reliability、security、operational excellence 的上线问题。

知识树落点：

- `knowledge_tree/04_Production_Layer/Deployment.md`

今天只填这些栏：

- 定义、部署组件、配置/密钥、上线 checklist、失败模式。

晚上产物：

- 画部署草图：Client、API、Worker、Vector DB、Doc Store、Trace Store、Eval Store、LLM Provider。
- 写上线 checklist：配置、密钥、权限、日志、eval、回滚、限流。

完成标准：

- `architecture/W4_Deployment_Diagram_Draft.md`
- `notes/D26_deployment_checklist.md`
- `knowledge_tree/04_Production_Layer/Deployment.md`

### Day 27：Final Architecture Review

P0 链接：

- [Azure AI workload documentation](https://learn.microsoft.com/en-us/azure/well-architected/ai/)
- [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)

今天必须弄懂的问题：

- Reliability：失败怎么降级？
- Security：越权怎么防？
- Cost：单请求成本怎么控？
- Operational Excellence：trace/eval/log 怎么闭环？
- Performance：P95 延迟怎么优化？

读资料时具体找：

- 只按五支柱找问题，不读全量文档。
- 每个支柱只写“当前项目最可能坏在哪里”和“最小控制措施”。

知识树落点：

- `knowledge_tree/04_Production_Layer/Production_Review.md`
- 回填 Tracing、Evaluation、Guardrails、Cost_and_Latency、Deployment 的“架构师问题”。

今天只填这些栏：

- Production_Review：五支柱评审表、当前风险、检测方式、降级方案。
- 其他生产节点：补架构师问题。

全天产物：

- `nfr/W4_NFR_Checklist.md`
- `security/W4_Threat_Model.md`
- `adr/ADR-004-trace-first-eval-strategy.md`

### Day 28：最终打包 + 面试表达

今天必须弄懂的问题：

- 你 4 周做出来的系统到底是什么？
- 它为什么不是“看了很多教程”的散点笔记？
- RAG、tool calling、workflow、eval、trace 如何连成一个架构故事？
- 这个系统的最大 trade-off 是什么？
- 面试官追问时，哪个 demo 可以证明你真的做过？

知识树落点：

- 所有核心节点补“面试表达”栏。
- `knowledge_tree/00_System_Map/Four_Layers.md` 补最终项目总览。

今天只填这些栏：

- 每个核心节点只补 30 秒版和项目例子。
- 不再扩展新概念。

全天产物：

- `README_Final.md`
- `notes/Interview_QA.md`
- `architecture/Final_Architecture_Review.md`

最终 5 个面试题：

- 什么是 RAG？
- workflow 和 agent 区别？
- 如何提升 tool calling 稳定性？
- 如何评估一个 agent 系统？
- 为什么很多场景不该先做 autonomous agent？

---

## 10. 周复盘模板

```markdown
# Week x Review

## 1. 本周我能讲清楚的 3 个概念

## 2. 本周最有价值的 demo

## 3. 本周踩过的 3 个坑

## 4. 本周更新的知识树节点
- 

## 5. 架构产物
- C4:
- ADR:
- NFR:
- FMA/Threat Model:

## 6. 五支柱检查
- Reliability:
- Security:
- Cost:
- Operational Excellence:
- Performance:

## 7. 下周只追一个核心问题
```

---

## 11. 最终验收标准

4 周结束，你应该能拿出：

- 一个可运行的 RAG / workflow / tool calling 综合小项目。
- 4 张架构图：System Context、Container、Dynamic、Deployment。
- 4 条 ADR。
- 4 份 NFR 检查。
- 1 份 RAG Failure Mode Analysis。
- 1 份 Threat Model。
- 1 份 Interview QA。
- 一棵能反映你自己理解的知识树。

最重要的是：你能讲清楚每个选择背后的 trade-off，而不是只说“教程这么写”。
