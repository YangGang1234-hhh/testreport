# Grant 的 4 周 LLM / Agent 系统化学习计划（架构师增强版）

> 适用对象：已经学过一遍 LLM / Agent，但感觉知识零散、掌握感弱；同时希望培养 **架构师思维**，从整体框架、质量属性、关键决策和系统演进角度学习的人。  
> 计划定位：这不是单纯的“技术补课计划”，而是 **技术学习主线 + 架构师训练副线** 的双线程计划。  
> 学习节奏：  
> - **周中**：每天 **早上 2 小时 + 晚上 2 小时 = 4 小时**  
> - **周末**：每天 **8 小时**  
> - **每周总计**：36 小时  
> - **4 周总计**：144 小时  

---

# 0. 这份“架构师增强版”计划和原计划有什么不同？

原来的 4 周计划重点在于：把 LLM / Agent 的知识树学扎实，并且通过 mini demo 和最终项目形成系统化理解。这个版本额外引入了一条 **架构师训练副线**，目的是让你不仅学“怎么做”，还学“为什么这么设计、有哪些替代方案、有哪些质量风险、如果规模变大或约束变化时怎么办”。这种训练方式，本质上就是在把开发者视角升级成架构师视角。微软的 Azure Well-Architected Framework 正是用 **Reliability、Security、Cost Optimization、Operational Excellence、Performance Efficiency** 五个支柱来帮助架构师系统性评估方案，而这个框架同样适用于 AI workloads。citeturn9search74turn9search80turn9search68

这个增强版计划里，每周除了学习主线，还会固定增加五类架构训练动作：  
1. **画 1 张架构图（C4）**  
2. **写 1 条 ADR（Architecture Decision Record）**  
3. **做 1 次 NFR（非功能需求）检查**  
4. **做 1 次 Failure Mode Analysis（失败模式分析）**  
5. **写 1 页 Trade-off Note（方案取舍说明）**  
C4 模型非常适合训练“整体框架感”和层次化表达能力，而 ADR 则是微软明确强调的 solution architect 的关键交付物之一，因为架构本质上就是一系列关键决策的累积。citeturn9search62turn9search82

---

# 1. 整体学习框架：双线程推进

## 1.1 技术学习主线（你原来那条线）

这条主线严格按照知识树推进：  
1. **模型层**：模型本身会什么、不会什么，特别是 prompt、structured output、tool calling 的边界。OpenAI 的 function calling 文档明确说明，模型不会真的执行函数，而是根据 schema 选择工具和参数，再由应用执行并回传。citeturn1search13  
2. **增强层**：RAG / Tools / Memory。Anthropic 将 retrieval、tools、memory 视为 augmented LLM 的三大增强能力；LlamaIndex 则把 RAG 拆成五阶段，特别适合你做结构化学习。citeturn1search1turn1search26  
3. **编排层**：Workflow / Agent / Multi-Agent。Anthropic 明确区分了 workflow（固定代码路径）与 agent（模型动态决定流程和工具使用），并总结了五类高频 workflow 模式。citeturn1search1  
4. **生产层**：Tracing / Eval / Guardrails / Security / Deployment。OpenAI 推荐先从 traces 开始理解 agent 行为，再逐步建立 datasets 和 eval runs；Phoenix 也强调 tracing 是 agent 迭代的底座。citeturn1search54turn1search39

## 1.2 架构师训练副线（新增）

这条副线帮助你从“会用技术点”升级到“能做架构判断”：  
- 用 **C4 模型** 画 System Context、Container、Dynamic、Deployment 图，训练你从系统边界到运行时拓扑的整体抽象能力。C4 本身就是一种层次化的软件架构表达方法：System、Container、Component、Code 四层结构，再配合 dynamic 和 deployment 图补充行为与部署视角。citeturn9search62turn9search63  
- 用 **ADR** 记录关键决策，包括背景、备选方案、最终决策、trade-offs 和 consequences。微软明确建议将 ADR 作为工作负载整个生命周期的 append-only 决策日志，用来保留架构演进历史，而不是只记“最后选了什么”。citeturn9search82  
- 用 **Well-Architected 五支柱** 检查每周的 demo / 项目：是否可靠？是否安全？是否成本过高？是否可运维？性能是否合格？Azure WAF 明确指出，这五个支柱是架构评审的基本框架，而且需要在 AI workload 中显式平衡 trade-offs。citeturn9search74turn9search77turn9search68  
- 用 **Failure Mode Analysis** 主动思考：如果模型、向量库、工具、权限、日志链路中的任一模块失效，系统会怎么坏、怎么降级、怎么恢复。Azure 的 AI workload 设计原则明确建议 architect 在 AI 系统中进行 failure mode analysis，并且尽量移除单点故障。citeturn9search68

---

# 2. 每天固定节奏（带架构训练）

## 2.1 周中（每天 4 小时）

### 早上 2 小时：输入 + 重建 + 架构抽象
- **30 分钟**：看当天主题的核心资料  
- **30 分钟**：闭眼重建（自己写定义 / 画最简结构图）  
- **30 分钟**：填知识树节点模板  
- **30 分钟**：回答一个架构问题：  
  - 这个点主要影响哪类质量属性？  
  - 如果规模扩大 10 倍，哪里最先出问题？  
  - 有没有更简单方案？

### 晚上 2 小时：输出 + 实操 + 架构决策训练
- **60 分钟**：做最小 demo / 小实验  
- **30 分钟**：写失败案例 / bug 记录  
- **30 分钟**：写一条 mini ADR / trade-off note

---

## 2.2 周末（每天 8 小时）

### 建议时段
- **09:00–12:00**：专题深挖 + 画图（C4 / 流程图 / 部署图）  
- **14:00–17:00**：做 mini project / 项目联调 / Failure Mode Analysis  
- **19:00–21:00**：写 ADR + NFR 检查 + 周复盘

---

# 3. 架构师训练中，你每周都要固定产出什么？

## 3.1 一张 C4 图
- **第 1 周**：System Context Diagram（系统边界、用户、外部依赖）  
- **第 2 周**：Container Diagram（服务、数据库、向量库、索引、日志）  
- **第 3 周**：Dynamic Diagram（workflow / agent 的运行时交互）  
- **第 4 周**：Deployment Diagram（部署、依赖、运行时拓扑）  
C4 的优势在于层级清晰，适合逐层训练你的“整体框架感”，而不是一上来陷进实现细节。citeturn9search62turn9search63

## 3.2 一条 ADR
每周至少一条，结构固定：  
- Context / Problem  
- Options considered  
- Decision  
- Trade-offs  
- Consequences  
- Status  
微软明确建议 ADR 用 append-only 的方式持续维护，不要覆盖旧记录；如果方向改变，应写一条新的 ADR supersede 旧记录。citeturn9search82

## 3.3 一次 NFR 检查
每周都要从五个支柱问一次：  
- Reliability：单点故障在哪里？  
- Security：权限与审批足够吗？  
- Cost：单请求预算是否可接受？  
- Operational Excellence：是否有 trace / log / eval？  
- Performance Efficiency：P95 延迟是否可接受？  
Azure WAF 明确强调，这五个维度不是上线前才看，而是设计阶段就要显式纳入权衡。citeturn9search74turn9search80

## 3.4 一次 Failure Mode Analysis
至少写 3～5 个“如果它坏了怎么办”的问题：  
- 模型服务不可用怎么办？  
- 向量库超时怎么办？  
- 工具调用失败怎么办？  
- 权限标签缺失怎么办？  
- 日志里出现敏感数据怎么办？  
Azure AI workload 设计原则明确建议 architect 针对关键组件做 failure mode analysis，并通过冗余、重试、熔断、fallback 等模式提升鲁棒性。citeturn9search68

## 3.5 一页 Trade-off Note
每周至少写一次“为什么不用另一个方案”：  
- 为什么不用 agent，而先用 workflow？  
- 为什么不用微调，而先用 RAG？  
- 为什么不用纯向量检索，而用 hybrid？  
- 为什么不暴露 20 个工具，而只暴露 3 个？  
这一步会强迫你从“技术点堆叠”切换到“方案比较”。Well-Architected Framework 的核心价值之一就是把 trade-offs 明文化，而不是假装所有维度都能同时最优。citeturn9search77turn9search80

---

# 4. 第 1 周：模型层 + Tool Calling 基础（附 System Context 训练）

## 4.1 技术目标
- 建立“模型 / 工具 / 应用”的明确边界。OpenAI 明确指出：模型只负责产生 tool call 请求，应用负责执行。citeturn1search13  
- 理解 Anthropic 所说的 augmented LLM 最小单元：LLM + tools。citeturn1search1  
- 做出一个最小闭环 demo：`LLM + 1~2 个工具 + 严格 schema`

## 4.2 架构训练目标
- 画出 **System Context Diagram**：系统的用户是谁、外部依赖有哪些、系统边界在哪里。C4 的 System Context 图正是用来回答“这个系统在整个生态里扮演什么角色”的。citeturn9search62  
- 写 **ADR-001**：为什么先做“单 LLM + Tool Calling”，而不是直接做多 Agent。Anthropic 明确建议从最简单、最可解释的方案开始。citeturn1search1turn9search82  
- 做一次最小 NFR 检查：  
  - Reliability：工具失败怎么处理？  
  - Security：工具是不是只读？  
  - Cost：限制几次模型 / 工具调用？  
  - OpEx：是否记录 tool call 输入输出？  
  - Performance：单次响应时延是否可接受？

## 4.3 本周新增产物
- C4：`W1_System_Context_Diagram`  
- ADR：`ADR-001-single-llm-and-tool-calling-first.md`  
- NFR 检查表：`W1_NFR_Checklist.md`  
- Trade-off Note：`Why-not-agent-first.md`

## 4.4 每日计划（在原计划上新增的架构动作）

### Day 1（周一）
- 在原有任务之外，增加：  
  - 列出系统中的 3 类参与者：用户、模型服务、数据系统  
  - 开始画 System Context Diagram 草图

### Day 2（周二）
- 在 `Prompting.md` 之外，补一个架构问题：  
  - Prompt 属于“行为约束”，那知识和动作应该分别归到哪个层？

### Day 3（周三）
- 在结构化输出实验后，写一个 Trade-off Note：  
  - 为什么这里要做 structured output，而不是自然语言解析？

### Day 4（周四）
- 在 tool calling demo 基础上，补写 ADR-001 草稿：  
  - 背景、方案、决策、trade-off、后果

### Day 5（周五）
- 做本周的 NFR mini-check：  
  - 可靠性 / 安全 / 成本 / 运维 / 性能 五维打分

### Day 6（周六）
- 下午 mini project v1 完成后，整理出正式版 System Context Diagram

### Day 7（周日）
- 周末复盘时，把 ADR-001、System Context 图、NFR 表一起放进项目目录

---

# 5. 第 2 周：RAG 系统（附 Container 训练）

## 5.1 技术目标
- 按 LlamaIndex 的 RAG 五阶段理解整个检索管道。citeturn1search26  
- 理解 Azure 在企业 RAG 中强调的 chunking、hybrid search、semantic ranking、安全 trimming、token constraints。citeturn1search33  
- 做一个带来源引用的 mini RAG demo

## 5.2 架构训练目标
- 画 **Container Diagram**：至少把 API 服务、向量库、原始文档存储、索引器、日志/评测存储画出来。C4 的 Container 图帮助你从“系统是什么”进一步走到“系统由哪些独立运行单元构成”。citeturn9search62  
- 写 **ADR-002**：为什么采用 hybrid search（或为什么采用某种 chunking 策略）。Azure 在企业 RAG 中明确推荐 hybrid search 和 semantic ranking。citeturn1search33turn9search82  
- 做 **Failure Mode Analysis**：  
  - 文档没更新  
  - chunk 切坏  
  - 权限标签丢失  
  - 向量库超时  
  - rerank 过慢  
  这一步直接训练你从“happy path”走向“故障路径”思维。Azure AI design principles 明确建议对关键依赖做 failure mode analysis。citeturn9search68

## 5.3 本周新增产物
- C4：`W2_Container_Diagram`  
- ADR：`ADR-002-hybrid-search-or-chunking-strategy.md`  
- NFR 检查表：`W2_NFR_Checklist.md`  
- FMA：`W2_RAG_Failure_Mode_Analysis.md`  
- Trade-off Note：`Why-hybrid-search.md`

## 5.4 每日计划（新增架构动作）

### Day 8（周一）
- 在准备语料库时，同时明确：  
  - 原始文档存储与索引存储是不是同一层？  
  - 元数据与权限标签由谁维护？

### Day 9（周二）
- 在 chunking 实验之外，补一个架构问题：  
  - 如果以后接入 PDF / 网页 / 数据库，chunking 能否统一？还是要多策略？

### Day 10（周三）
- 画 Container Diagram 初稿：  
  - API、Retriever、Vector Store、Doc Store、Eval Store、Trace Store

### Day 11（周四）
- 写 ADR-002 草稿：  
  - 纯向量 vs 关键词 vs hybrid  
  - 为什么当前场景选择 hybrid

### Day 12（周五）
- 做本周 NFR 检查：  
  - RAG 权限控制是否到位？  
  - 响应延迟是否可接受？  
  - 评测是否可重复？

### Day 13（周六）
- 做一次 Failure Mode Analysis：  
  - 至少 5 个问题点，每个写“影响 / 检测方式 / 降级方案 / 修复动作”

### Day 14（周日）
- 最终收口：Container 图 + ADR-002 + Failure Mode Analysis 一起存档

---

# 6. 第 3 周：Workflow / Agent 编排层（附 Dynamic 行为训练）

## 6.1 技术目标
- 明确 workflow 与 agent 的边界。Anthropic 认为 workflow 适合路径可预定义的任务，agent 适合步骤和工具使用不可预测的问题。citeturn1search1  
- 理解五种经典 workflow 模式，并借助 LangChain 的 agent runtime 思维理解 middleware、HITL、subagent 等工程实现。citeturn1search1turn1search7

## 6.2 架构训练目标
- 画 **Dynamic Diagram**：把 planner、researcher、reviewer、tool call、human approval 的运行时顺序画出来。C4 的 Dynamic 图非常适合表达“系统如何协作完成一个具体任务”。citeturn9search62  
- 写 **ADR-003**：为什么当前场景用 workflow，而不是 autonomous agent。Anthropic 明确建议优先使用更简单、更可控的方案。citeturn1search1turn9search82  
- 做一次 **架构设计评审问题单**：  
  - 停止条件是什么？  
  - 哪些步骤可以并行？  
  - 如果一个 worker 失败怎么办？  
  - 哪些动作必须人审？  
  - 哪些状态需要持久化？

## 6.3 本周新增产物
- C4：`W3_Dynamic_Diagram`  
- ADR：`ADR-003-workflow-over-agent.md`  
- NFR 检查表：`W3_NFR_Checklist.md`  
- 设计评审单：`W3_Architecture_Review_Questions.md`  
- Trade-off Note：`Why-not-autonomous-agent.md`

## 6.4 每日计划（新增架构动作）

### Day 15（周一）
- 在 `Workflow_vs_Agent.md` 之外，加一张架构判断表：  
  - 可预测性 / 可控性 / 复杂度 / 成本 / 可评测性

### Day 16（周二）
- 在 routing demo 后，记录：  
  - 如果分类错了，系统会如何自我修正？这是 reliability 问题还是 correctness 问题？

### Day 17（周三）
- 画 Dynamic Diagram 初稿：  
  - orchestrator 下发任务  
  - worker 执行  
  - 合并结果  
  - 错误分支

### Day 18（周四）
- 写一页 trade-off：  
  - 为什么生成-评审循环适合这一类任务，而不适合高延迟敏感任务

### Day 19（周五）
- 做本周 NFR 检查：  
  - 是否存在死循环风险？  
  - 人审点是否足够？  
  - 多 agent 协作是否引入额外 token / latency 成本？

### Day 20（周六）
- 完成 Dynamic Diagram 正式版
- 写 ADR-003 正式版

### Day 21（周日）
- 做一次模型化的架构评审：  
  - 把“workflow / single agent / multi-agent”三个方案做个对比页

---

# 7. 第 4 周：生产层 + 项目整合（附 Deployment / Governance 训练）

## 7.1 技术目标
- 根据 OpenAI 的建议，把项目从“能跑”升级为“可 trace、可 eval、可迭代”的系统。citeturn1search54  
- 根据 Phoenix 的思路，把每一步关键事件记录下来，使系统具备可观测性。citeturn1search39  
- 根据 Azure / MCP 的要求，把安全、权限、日志和工具审批纳入设计。citeturn1search33turn1search20

## 7.2 架构训练目标
- 画 **Deployment Diagram**：运行时部署拓扑，包括 API、模型服务、向量库、存储、日志与监控。C4 的 Deployment 图能逼你从“代码逻辑”切换到“系统运行在哪、如何连接、哪里是敏感路径”。citeturn9search62  
- 写 **ADR-004**：为什么采用 trace-first + dataset eval 的质量策略，而不是只靠人工 spot check。OpenAI 明确建议用 traces、graders、datasets、eval runs 去做系统性质量改进。citeturn1search54turn9search82  
- 做 **Threat Model**：至少列 5 类风险：越权检索、工具误调用、敏感数据进日志、提示注入、成本滥用。Azure WAF 强调 Security 是全程设计问题；MCP 也强调工具和数据访问必须在显式授权下进行。citeturn9search74turn1search20

## 7.3 本周新增产物
- C4：`W4_Deployment_Diagram`  
- ADR：`ADR-004-trace-first-eval-strategy.md`  
- NFR 检查表：`W4_NFR_Checklist.md`  
- Threat Model：`W4_Threat_Model.md`  
- Trade-off Note：`Why-trace-first.md`

## 7.4 每日计划（新增架构动作）

### Day 22（周一）
- 在 `Tracing.md` 之外，先回答一个架构问题：  
  - 哪些 trace 事件是必须有的？哪些只是 nice-to-have？  
  - trace 数据可能引入什么隐私风险？

### Day 23（周二）
- 在 eval 数据集之外，补一份质量门槛定义：  
  - 哪些指标不达标时不能上线？

### Day 24（周三）
- 做 Threat Model 草稿：  
  - 风险、攻击路径、影响、现有控制、残余风险

### Day 25（周四）
- 画 Deployment Diagram 初稿：  
  - 哪些组件在应用层？  
  - 哪些组件是托管服务？  
  - 敏感数据经过哪些路径？

### Day 26（周五）
- 写 ADR-004 草稿：  
  - 为什么要 trace-first + dataset eval  
  - 不这样做的代价是什么

### Day 27（周六）
- 做完整的架构评审：  
  - 看 Reliability / Security / Cost / OpEx / Performance 五维是否平衡

### Day 28（周日）
- 最终收口：  
  - Deployment 图  
  - ADR-004  
  - Threat Model  
  - 最终 README / 架构图 / Interview QA

---

# 8. 每周最终交付（增强版）

## 第 1 周交付
- 6 个知识树节点  
- 1 个最小 tool calling demo  
- 1 份 `One_Page_Tool_Calling.md`  
- 1 张 System Context Diagram  
- 1 条 ADR-001  
- 1 份 NFR 检查表  
- 1 份 Trade-off Note

## 第 2 周交付
- 9 个 RAG 节点  
- 1 个最小 RAG demo  
- 1 份 `One_Page_RAG.md`  
- 1 张 Container Diagram  
- 1 条 ADR-002  
- 1 份 Failure Mode Analysis  
- 1 份 NFR 检查表

## 第 3 周交付
- 9 个编排层节点  
- 1 个 workflow / agent demo  
- 1 份 `One_Page_Agent.md`  
- 1 张 Dynamic Diagram  
- 1 条 ADR-003  
- 1 份 Design Review 问题单  
- 1 份 NFR 检查表

## 第 4 周交付
- 7 个生产层节点  
- 1 个完整项目  
- 1 套项目文档 + 失败案例 + Interview QA  
- 1 张 Deployment Diagram  
- 1 条 ADR-004  
- 1 份 Threat Model  
- 1 份最终架构评审结论

---

# 9. 你应该优先培养的“架构师习惯”

## 9.1 任何技术点都问 5 个问题
1. 它解决什么问题？  
2. 它属于系统哪一层？  
3. 有没有更简单方案？  
4. 代价是什么？  
5. 如果规模扩大 10 倍，会先坏在哪里？  
这些问题本质上就是从“实现思维”切换到“架构思维”。Azure Well-Architected Framework 之所以有价值，不是因为它提供某个具体技术，而是因为它强迫你持续做这种平衡式设计。citeturn9search74turn9search77

## 9.2 任何周末都做一次 Architecture Review Hour
建议你每周日晚上固定做 1 小时架构复盘，只回答这 6 个问题：  
1. 系统边界清楚了吗？  
2. 关键容器拆分合理吗？  
3. 关键决策写进 ADR 了吗？  
4. NFR 是否显式写出来了？  
5. 最大风险点是什么？  
6. 如果业务量变成 10 倍，先改哪层？

## 9.3 不只画图，更要解释图
C4 图不是为了好看，而是为了让你能回答：  
- 这个系统在更大生态里扮演什么角色？  
- 它如何拆分容器和组件？  
- 它如何在运行时协同？  
- 它最终部署在什么形态上？  
这正是 C4 模型的层级抽象价值。citeturn9search62turn9search65

## 9.4 不只写 ADR，更要让 ADR 记录 trade-off
ADR 不是“记结论”，而是记“为什么选这个而不是那个”。微软明确建议在 ADR 中记录 options、trade-offs、confidence 和 consequences，因为这些信息随着时间推移会比结论本身更有价值。citeturn9search82

---

# 10. 这 4 周结束后，你会多出什么能力？

如果你认真执行完这版计划，你拿到的就不只是“学了 4 周 LLM / Agent”，而是：  
- 你能从 **System Context / Container / Dynamic / Deployment** 四个层次解释你的系统。citeturn9search62  
- 你能用 **ADR** 记录自己的架构决策，不再只会说“我这么写是因为网上都这么写”。citeturn9search82  
- 你能用 **Reliability / Security / Cost / Operational Excellence / Performance** 五个维度做最基本的架构评审。citeturn9search74turn9search80  
- 你会开始习惯做 **Failure Mode Analysis 和 Threat Modeling**，也就是提前思考系统怎么坏，而不是线上坏了再想。Azure 对 AI workloads 明确建议 architect 这么做。citeturn9search68  
- 你最后拿出来的也不只是一个 demo，而是一套“有图、有 ADR、有 NFR、有 eval、有 trace、有项目文档”的小型架构案例。

---

# 11. 最后提醒：你的优势非常适合往“AI 应用架构”发展

你本身是数据工程背景，所以你最适合发展的路线，并不是“只会 prompt 调参”，而是：  
> **懂数据底座 + 懂 AI 应用链路 + 懂治理与评测 + 会做架构取舍**  

企业里真正痛的往往不是“我怎么调一个模型 API”，而是：  
- 数据从哪里来？  
- 权限怎么继承？  
- 检索怎么做？  
- 工具怎么接？  
- trace 怎么打？  
- eval 怎么做？  
- 成本怎么控？  
- 出故障怎么排？  
这些，本质上正是 AI workload 架构问题，也是 Azure Well-Architected AI guidance 关注的核心。citeturn9search68turn9search74

---

> 结论一句话：  
> 这版“架构师增强版”计划，目的不是让你立刻成为 title 上的架构师，而是让你在学习 LLM / Agent 的同时，提早养成 **整体抽象、质量属性、关键决策、风险分析、方案取舍** 的架构思维习惯。  
> 只要你把这 4 周坚持做完，你的思考方式会明显不一样。  
