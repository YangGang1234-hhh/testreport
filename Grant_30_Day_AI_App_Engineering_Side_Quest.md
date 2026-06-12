# Grant 的 30 天大模型应用工程底座副线

> 定位：不打乱原来的 LLM / Agent 主线，每天额外 1.5 小时，补齐大模型应用开发工程师需要的后端、数据库、中间件、工程工具和部署运维能力。
>
> 学习方式：以官方资料阅读 + 手写代码为主。每天只做一个小闭环，不追求大而全。

---

## 0. 总目标

30 天后，你应该能独立搭出一个最小但完整的 AI 应用工程骨架：

```text
Client
  -> FastAPI REST API
  -> Redis cache / rate limit / session
  -> MongoDB document store
  -> Milvus vector store
  -> Kafka async indexing events
  -> vLLM / OpenAI-compatible model endpoint
  -> structured logging
  -> Docker / Docker Compose
  -> GitHub Actions CI
  -> Claude Code-assisted engineering workflow
```

这个副线不是为了让你变成数据库专家、运维专家或中间件专家，而是让你能胜任“大模型应用开发工程师”岗位里最常见的工程任务：能写 API、能接数据库、能做异步任务、能容器化、能管理配置和密钥、能看日志、能把最小 CI 跑起来。

---

## 1. 每天 1.5 小时固定节奏

- 20 分钟：读当天 P0 官方资料，只读指定章节
- 50 分钟：手写代码，不复制完整示例
- 15 分钟：排错、验证、跑接口或跑测试
- 5 分钟：写学习日志和明天问题

Claude Code 使用原则：

- 每天最多占 10 分钟，嵌入在编码和验证环节里，不额外挤占主线。
- 核心代码先自己手写，再让 Claude Code review、解释、补测试或定位报错。
- 不把“让 Claude Code 直接写完整功能”当成学习完成；你必须能解释它改了什么、为什么这么改。
- 遇到环境、依赖、Docker、Kafka、Milvus、vLLM 报错时，可以优先让 Claude Code 帮你读日志和提出排查路径。

执行口径：

- 90 分钟是标准版：适合正常学习日，能完成阅读、编码、验证和记录。
- 60 分钟是保底版：当天忙时只保留 P0 阅读、核心代码和日志。
- 120 分钟是难点版：Milvus、Kafka、Docker、vLLM 这类环境重的主题，周末或状态好时可以加时。

每天产物：

```text
engineering-side-quest/
  app/
  tests/
  scripts/
  docker/
  docs/
  notes/
```

每天至少留下一个：

- `notes/Dxx_topic.md`
- `app/...`
- `scripts/...`
- `tests/...`
- `docker/...`
- `docs/...`

---

## 2. 技术选择说明

### 2.1 后端

- FastAPI：Python AI 应用里非常常见，天然支持 OpenAPI / Swagger 文档，适合快速做 LLM/RAG 服务。
- REST API：岗位里最基础的服务接口表达方式，必须熟悉资源、方法、状态码、错误响应。

### 2.2 NoSQL

本计划选择 MongoDB / MongoDB-compatible 文档数据库。

原因：

- 很适合存对话、文档元数据、任务状态、trace 摘要、用户配置等半结构化数据。
- 国内云厂商也常见 MongoDB 兼容服务或托管 MongoDB 服务，知识迁移成本低。
- 它和 Redis / Milvus 的职责边界清楚：MongoDB 存业务文档，Redis 做缓存和短状态，Milvus 存向量。

### 2.3 向量数据库

- Milvus：国内大模型应用和 RAG 场景里很常见，适合系统学习向量库的 collection、schema、index、search。

### 2.4 中间件

- Redis：缓存、session、rate limit、分布式锁、轻量队列。
- Kafka：事件流、异步索引、日志/数据管道、解耦 API 和后台任务。

### 2.5 工程工具与部署

- Git：版本管理和协作基本功。
- Docker / Docker Compose：本地复现服务栈。
- vLLM：本地或私有化模型推理服务的常见选择，重点学 OpenAI-compatible serving。
- 环境变量、密钥管理、日志、CI/CD：从 demo 到工程项目的基本门槛。

### 2.6 Claude Code

- Claude Code：AI 编程工作流工具，适合读项目、解释架构、定位报错、写测试、做代码 review、生成文档、辅助 Git 操作和 CI 排查。
- 学它的目标不是“让 AI 替你写代码”，而是掌握一种现代工程协作方式：你负责目标、边界、验收标准和最终判断；Claude Code 负责加速搜索、编辑、验证和复盘。
- 在本副线里，Claude Code 主要承担三类角色：
  - 架构解释器：让它帮你画清楚 FastAPI、MongoDB、Milvus、Redis、Kafka、vLLM 之间的边界。
  - 代码审查员：让它检查接口设计、错误处理、配置管理、日志脱敏和测试覆盖。
  - 排错助手：把报错、日志、失败测试交给它，让它给出排查路径，但最终修复必须由你确认。

---

## 3. 官方资料索引

### FastAPI / REST

- [FastAPI First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [FastAPI Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [FastAPI Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [FastAPI Settings and Environment Variables](https://fastapi.tiangolo.com/advanced/settings/)
- [MDN HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)
- [MDN HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

### MongoDB

- [MongoDB PyMongo Get Started](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/get-started/)
- [MongoDB CRUD Operations](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/)
- [MongoDB Indexes](https://www.mongodb.com/docs/manual/indexes/)

### Milvus

- [Milvus Quickstart](https://milvus.io/docs/quickstart.md)
- [Milvus Collections](https://milvus.io/docs/manage-collections.md)
- [Milvus Insert Entities](https://milvus.io/docs/insert-update-delete.md)
- [Milvus Single Vector Search](https://milvus.io/docs/single-vector-search.md)

### Redis

- [Redis Quick starts](https://redis.io/docs/latest/develop/get-started/)
- [Redis Data types](https://redis.io/docs/latest/develop/data-types/)
- [Redis Python client redis-py](https://redis.readthedocs.io/en/stable/)

### Kafka

- [Apache Kafka Quickstart](https://kafka.apache.org/quickstart/)
- [Apache Kafka Introduction](https://kafka.apache.org/intro)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)

### Git / Docker / vLLM / CI

- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Docker Get Started](https://docs.docker.com/get-started/)
- [Docker Compose Quickstart](https://docs.docker.com/compose/gettingstarted/)
- [vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)
- [vLLM OpenAI-Compatible Server](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html)
- [GitHub Actions Quickstart](https://docs.github.com/en/actions/get-started/quickstart)
- [Python Logging HOWTO](https://docs.python.org/3/howto/logging.html)

### Claude Code

- [Claude Code Overview](https://code.claude.com/docs/en/overview)
- [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)
- [Claude Code Common workflows](https://code.claude.com/docs/en/common-workflows)
- [Claude Code Best practices](https://code.claude.com/docs/en/best-practices)
- [Claude Code Memory / CLAUDE.md](https://code.claude.com/docs/en/memory)
- [Claude Code Permissions](https://code.claude.com/docs/en/permissions)
- [Claude Code Hooks](https://code.claude.com/docs/en/hooks)

---

## 3.1 Claude Code 架构、原理和应用（贯穿 30 天）

这一节不是单独占用一天，而是每天 5-10 分钟穿插使用。你要同时学会 Claude Code 的三个层面：架构、原理、应用。

### 3.1.1 架构：它由哪些部分组成？

用一个最小模型理解：

```text
你的任务描述
  -> Claude 模型推理
  -> Claude Code agentic harness
  -> 工具层
      - 文件读写
      - 代码搜索
      - Shell 命令
      - Git
      - 测试和构建
      - Web / 文档检索
      - MCP / hooks / skills / subagents
  -> 执行结果回到上下文
  -> 模型决定下一步
  -> 直到完成或等待你确认
```

你需要掌握的架构概念：

- Agentic loop：收集上下文、采取行动、验证结果，然后循环。
- Tools：没有工具时模型只能说话；有工具后才能读文件、改代码、跑命令、查资料。
- Context：会话历史、文件内容、命令输出、`CLAUDE.md`、memory、skills 都会占上下文。
- Session：一次任务是一条会话，可以 resume，也可以 fork。
- Permissions：文件编辑、命令执行、外部副作用需要权限边界。
- Extensibility：MCP 连接外部系统，hooks 在关键动作前后执行脚本，skills 固化可复用工作流，subagents 分担长任务。

### 3.1.2 原理：它为什么能帮你做工程任务？

Claude Code 的核心不是“自动补全”，而是“带工具的循环执行”：

1. 读任务：理解你的目标和约束。
2. 找上下文：搜索文件、阅读代码、查看配置和日志。
3. 制定计划：复杂任务先给方案，简单任务直接行动。
4. 执行动作：编辑文件、运行测试、执行命令。
5. 验证结果：看测试、构建、接口响应、日志。
6. 继续修正：根据结果调整下一步。

学习时要记住边界：

- Claude Code 可以加速工程工作，但不替代你的架构判断。
- 它能运行命令，所以权限、密钥、生产环境、副作用操作必须谨慎。
- 它的上下文会被压缩，所以长期规则要写进 `CLAUDE.md`，不要只放在聊天里。
- 它会犯错，所以每次改动必须有测试、diff review 或可运行验证。

### 3.1.3 应用：每天怎么用？

每天固定用 1 个小动作即可：

```text
开始前 3 分钟：
让 Claude Code 解释今天要改的文件、接口或配置。

编码中 3 分钟：
遇到报错时，把错误和相关文件交给它，让它给排查路径。

结束前 4 分钟：
让它 review 今天的 diff，并要求它只指出 bug、风险、缺测试。
```

常用提示词：

```text
请先阅读当前项目结构，只解释和今天任务相关的文件，不要改代码。
```

```text
请 review 我今天的改动，优先找 bug、边界条件、错误处理和缺失测试。不要做无关重构。
```

```text
这是报错日志。请按最可能原因排序，给我 3 步排查路径。先不要改代码。
```

```text
请根据当前 FastAPI 接口，帮我补 3 个 pytest 测试用例。只覆盖核心路径和错误路径。
```

```text
请帮我生成一份简短的 CLAUDE.md，包含项目结构、常用命令、编码约定、禁止事项和测试命令。
```

### 3.1.4 30 天穿插任务

| 时间 | Claude Code 任务 | 产物 |
|---|---|---|
| Day 1 | 让它解释工程目录和 Git 工作流 | `notes/D01_claude_code_usage.md` |
| Day 3 | 让它解释 FastAPI app 启动流程 | `notes/D03_claude_code_fastapi_review.md` |
| Day 7 | 让它 review 测试覆盖 | `notes/D07_claude_code_test_review.md` |
| Day 14 | 让它解释 MongoDB 和 Milvus 的职责边界 | `notes/D14_claude_code_data_layer_review.md` |
| Day 21 | 让它分析 Redis/Kafka/Docker 排错路径 | `notes/D21_claude_code_middleware_debug.md` |
| Day 24 | 让它检查环境变量和密钥是否可能泄露 | `notes/D24_claude_code_secret_review.md` |
| Day 27 | 让它 review GitHub Actions CI 配置 | `notes/D27_claude_code_ci_review.md` |
| Day 30 | 让它生成最终 README 初稿，再由你手动修改 | `docs/claude_code_final_review.md` |

### 3.1.5 Claude Code 学习产物

30 天结束时，额外留下 4 个文件：

- `docs/claude_code_architecture.md`：解释 Claude Code 的 agentic loop、tools、context、session、permissions。
- `docs/claude_code_workflow.md`：记录你最常用的 5 个工作流。
- `CLAUDE.md`：项目级指导文件，包含项目结构、常用命令、编码规范、测试方式和安全边界。
- `docs/claude_code_risks.md`：记录它容易犯错的地方，以及你如何验证。

## 4. 第 1 周：FastAPI / REST / Git 基础

本周目标：能写一个规范的 REST API，知道请求、响应、状态码、错误处理、分层结构和测试怎么组织。

本周产物：

- `app/main.py`
- `app/api/`
- `app/schemas/`
- `app/services/`
- `tests/test_health.py`
- `docs/api_design.md`

### Day 1：工程目录 + Git 基本流

P0：

- [Pro Git Book - Getting Started](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)

阅读目标：

- 只理解 working tree、staging area、commit、branch。

手写代码：

- 建目录：

```text
engineering-side-quest/
  app/
  tests/
  scripts/
  docs/
  notes/
```

- 初始化 Git。
- 写 `.gitignore`，至少忽略 `.env`、`.venv`、`__pycache__`、`.pytest_cache`。

完成标准：

- `notes/D01_git_basics.md`
- 至少有 1 次 commit。

### Day 2：HTTP / REST 基本概念

P0：

- [MDN HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)
- [MDN HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

阅读目标：

- 搞清楚 GET / POST / PUT / PATCH / DELETE。
- 搞清楚 200 / 201 / 400 / 401 / 403 / 404 / 409 / 422 / 500。

手写代码：

- 在 `docs/api_design.md` 写一个 AI 笔记服务 API 草案：
  - `GET /health`
  - `POST /documents`
  - `GET /documents/{id}`
  - `POST /chat`
  - `GET /tasks/{id}`

完成标准：

- 能解释每个接口为什么用这个 HTTP method。

### Day 3：FastAPI Hello World + Swagger

P0：

- [FastAPI First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)

阅读目标：

- 理解 `FastAPI()`、path operation、Swagger UI、OpenAPI JSON。

手写代码：

- 写 `app/main.py`。
- 实现：
  - `GET /`
  - `GET /health`

完成标准：

- 本地能访问 `/docs`。
- `notes/D03_fastapi_first_steps.md`

### Day 4：Request Body + Pydantic Schema

P0：

- [FastAPI Request Body](https://fastapi.tiangolo.com/tutorial/body/)

阅读目标：

- 理解请求体、字段校验、类型标注。

手写代码：

- 新建 `app/schemas/chat.py`：
  - `ChatRequest`
  - `ChatResponse`
- 实现 `POST /chat`，先返回 mock answer。

完成标准：

- Swagger 里能看到请求体 schema。

### Day 5：错误处理 + 状态码

P0：

- [FastAPI Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [MDN HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

阅读目标：

- 理解 `HTTPException`。
- 区分 400、404、409、422。

手写代码：

- 给 `GET /documents/{id}` 加 404。
- 给 `POST /chat` 加空问题校验。
- 统一错误格式：

```json
{
  "error": {
    "code": "DOCUMENT_NOT_FOUND",
    "message": "..."
  }
}
```

完成标准：

- `notes/D05_error_handling.md`

### Day 6：多文件结构 + Service 层

P0：

- [FastAPI Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

阅读目标：

- 理解 `APIRouter`、模块拆分。

手写代码：

- 拆目录：

```text
app/api/routes/health.py
app/api/routes/chat.py
app/api/routes/documents.py
app/services/chat_service.py
```

- `main.py` 只负责组装 app。

完成标准：

- API 行为不变，但代码分层更清楚。

### Day 7：FastAPI 测试

P0：

- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)

阅读目标：

- 理解 `TestClient`。

手写代码：

- 写：
  - `tests/test_health.py`
  - `tests/test_chat.py`
- 至少测 3 个 case：健康检查、正常 chat、空问题报错。

完成标准：

- 本周 API 骨架完成。
- `docs/week1_backend_review.md`

---

## 5. 第 2 周：MongoDB + Milvus 数据层

本周目标：能用 MongoDB 存业务文档和对话记录，用 Milvus 存向量并做最小检索。

本周产物：

- `app/repositories/mongo_repo.py`
- `app/repositories/milvus_repo.py`
- `scripts/seed_documents.py`
- `scripts/rebuild_vector_index.py`
- `docs/data_model.md`

### Day 8：MongoDB 文档模型

P0：

- [MongoDB PyMongo Get Started](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/get-started/)

阅读目标：

- 理解 database、collection、document。

手写代码：

- 设计 `documents` collection：

```json
{
  "_id": "...",
  "title": "...",
  "source": "...",
  "content": "...",
  "created_at": "...",
  "metadata": {}
}
```

- 写 `docs/data_model.md`。

完成标准：

- 能说清 MongoDB 和 Milvus 分别存什么。

### Day 9：PyMongo CRUD

P0：

- [MongoDB CRUD Operations](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/)

阅读目标：

- 理解 insert、find、update、delete。

手写代码：

- 写 `app/repositories/mongo_repo.py`：
  - `create_document`
  - `get_document`
  - `list_documents`
  - `update_document_status`

完成标准：

- 写 `scripts/seed_documents.py` 插入 3 条测试文档。

### Day 10：MongoDB 索引和查询设计

P0：

- [MongoDB Indexes](https://www.mongodb.com/docs/manual/indexes/)

阅读目标：

- 理解为什么要建索引。

手写代码：

- 给 `documents` 设计索引：
  - `source`
  - `created_at`
  - `metadata.owner`
- 写分页查询 `list_documents(limit, offset)`。

完成标准：

- `notes/D10_mongodb_indexes.md`

### Day 11：Milvus 基础概念

P0：

- [Milvus Quickstart](https://milvus.io/docs/quickstart.md)
- [Milvus Collections](https://milvus.io/docs/manage-collections.md)

阅读目标：

- 理解 collection、schema、field、vector dimension。

手写代码：

- 写 `docs/milvus_schema.md`：

```text
collection: document_chunks
fields:
  chunk_id: varchar
  document_id: varchar
  text: varchar
  embedding: float_vector
  metadata_json: varchar
```

完成标准：

- 能解释 Milvus 为什么不替代 MongoDB。

### Day 12：Milvus 插入和检索

P0：

- [Milvus Insert Entities](https://milvus.io/docs/insert-update-delete.md)
- [Milvus Single Vector Search](https://milvus.io/docs/single-vector-search.md)

阅读目标：

- 理解 insert、index、search。

手写代码：

- 写 `app/repositories/milvus_repo.py`：
  - `create_collection_if_not_exists`
  - `insert_chunks`
  - `search_similar_chunks`
- embedding 先用 mock 向量函数，不依赖模型 API。

完成标准：

- `scripts/rebuild_vector_index.py`

### Day 13：MongoDB + Milvus 组合查询

P0：

- 复读 Day 8-12 的笔记，不开新资料。

阅读目标：

- 只回答一个问题：RAG 里 metadata、chunk text、embedding、source 应该分别放哪里？

手写代码：

- 做 `POST /documents`：
  - 写入 MongoDB
  - 切 chunk
  - 写入 Milvus
- 做 `POST /retrieve`：
  - Milvus 查 chunk
  - MongoDB 补 document metadata

完成标准：

- `notes/D13_data_layer_integration.md`

### Day 14：数据层周项目

P0：

- 复盘本周所有代码。

手写代码：

- 完成一个最小 RAG data layer：

```text
POST /documents
GET /documents/{id}
POST /retrieve
```

完成标准：

- `docs/week2_data_layer_review.md`
- 画一张数据流图：API -> MongoDB / Milvus。

---

## 6. 第 3 周：Redis / Kafka / Docker 中间件

本周目标：能用 Redis 做缓存和短状态，用 Kafka 做异步事件，用 Docker Compose 组织本地依赖。

本周产物：

- `app/infra/redis_client.py`
- `app/infra/kafka_client.py`
- `scripts/index_worker.py`
- `Dockerfile`
- `docker-compose.yml`

### Day 15：Redis 基础和缓存

P0：

- [Redis Quick starts](https://redis.io/docs/latest/develop/get-started/)
- [Redis Data types](https://redis.io/docs/latest/develop/data-types/)

阅读目标：

- 理解 Redis 可以做缓存、数据库、消息代理等用途。
- 只重点看 string、hash、list。

手写代码：

- 写 `app/infra/redis_client.py`。
- 给 `GET /documents/{id}` 加缓存：
  - cache hit 直接返回
  - cache miss 查 MongoDB 后写 Redis

完成标准：

- `notes/D15_redis_cache.md`

### Day 16：Redis session / rate limit

P0：

- [redis-py documentation](https://redis.readthedocs.io/en/stable/)

阅读目标：

- 理解 TTL、incr、expire。

手写代码：

- 做简单 rate limit：
  - 每个 `user_id` 每分钟最多 10 次 `POST /chat`
- 超过限制返回 429。

完成标准：

- `notes/D16_redis_rate_limit.md`

### Day 17：Kafka 基础概念

P0：

- [Apache Kafka Introduction](https://kafka.apache.org/intro)
- [Apache Kafka Quickstart](https://kafka.apache.org/quickstart/)

阅读目标：

- 理解 topic、producer、consumer、broker、event。

手写代码：

- 写 `docs/kafka_event_design.md`：

```json
{
  "event_type": "document_uploaded",
  "document_id": "...",
  "source": "...",
  "created_at": "..."
}
```

完成标准：

- 能解释为什么索引构建适合异步事件。

### Day 18：Kafka producer / consumer

P0：

- [Apache Kafka Quickstart](https://kafka.apache.org/quickstart/)

阅读目标：

- 只看 create topic、write events、read events。

手写代码：

- 写：
  - `app/infra/kafka_client.py`
  - `scripts/index_worker.py`
- `POST /documents` 不直接建索引，而是发送 `document_uploaded` 事件。
- worker 消费事件后切 chunk、写 Milvus。

完成标准：

- `notes/D18_kafka_async_indexing.md`

### Day 19：Dockerfile

P0：

- [Docker Get Started](https://docs.docker.com/get-started/)

阅读目标：

- 理解 image、container、Dockerfile。

手写代码：

- 写 FastAPI 的 `Dockerfile`。
- 容器启动命令运行 API。

完成标准：

- `Dockerfile`
- `notes/D19_dockerfile.md`

### Day 20：Docker Compose

P0：

- [Docker Compose Quickstart](https://docs.docker.com/compose/gettingstarted/)

阅读目标：

- 理解 service、ports、volumes、environment。

手写代码：

- 写 `docker-compose.yml`，至少包含：
  - api
  - mongo
  - redis
  - kafka
- Milvus 可以先用本地 Milvus Lite 或单独 compose 文件，避免本周堆太重。

完成标准：

- `docker-compose.yml`
- `docs/local_dev_stack.md`

### Day 21：中间件周项目

P0：

- 复盘 Redis / Kafka / Docker 笔记。

手写代码：

- 跑通：

```text
POST /documents
  -> MongoDB 保存文档
  -> Kafka 发送 document_uploaded
  -> worker 消费事件
  -> Milvus 写入 chunk vectors

GET /documents/{id}
  -> Redis cache
  -> MongoDB fallback
```

完成标准：

- `docs/week3_middleware_review.md`
- 记录 3 个排错 case。

---

## 7. 第 4 周：vLLM / 配置密钥 / 日志 / CI/CD / 运维

本周目标：让项目从“本地能跑”变成“像一个工程项目”：配置清楚、密钥不进代码、日志可查、CI 能跑、vLLM 可接入。

本周产物：

- `app/core/config.py`
- `app/core/logging.py`
- `.env.example`
- `.github/workflows/ci.yml`
- `docs/deployment_checklist.md`
- `docs/runbook.md`

### Day 22：vLLM 基础

P0：

- [vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)
- [vLLM OpenAI-Compatible Server](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html)

阅读目标：

- 理解 offline inference 和 online serving。
- 重点理解 OpenAI-compatible server 的价值：应用层可以像调 OpenAI API 一样调本地模型服务。

手写代码：

- 写 `docs/vllm_serving_notes.md`。
- 在配置里预留：

```text
LLM_BASE_URL
LLM_API_KEY
LLM_MODEL
```

完成标准：

- 能说明 vLLM 在企业私有化部署里的位置。

### Day 23：接入 OpenAI-compatible LLM endpoint

P0：

- 复读 vLLM OpenAI-compatible server 文档。

手写代码：

- 写 `app/services/llm_client.py`。
- 只依赖环境变量：
  - `LLM_BASE_URL`
  - `LLM_API_KEY`
  - `LLM_MODEL`
- 如果没有本地 vLLM，就用 mock client。

完成标准：

- `POST /chat` 从 mock answer 改成走 `llm_client.generate()`。

### Day 24：环境变量和密钥管理

P0：

- [FastAPI Settings and Environment Variables](https://fastapi.tiangolo.com/advanced/settings/)

阅读目标：

- 理解 settings、environment variables、`.env`。

手写代码：

- 写：
  - `app/core/config.py`
  - `.env.example`
- 禁止把真实 key 写入仓库。
- 所有连接串从环境变量读取：
  - `MONGO_URI`
  - `REDIS_URL`
  - `KAFKA_BOOTSTRAP_SERVERS`
  - `MILVUS_URI`
  - `LLM_BASE_URL`

完成标准：

- `notes/D24_env_secret_management.md`

### Day 25：结构化日志

P0：

- [Python Logging HOWTO](https://docs.python.org/3/howto/logging.html)

阅读目标：

- 理解 logger、level、handler、formatter。

手写代码：

- 写 `app/core/logging.py`。
- 每个请求记录：
  - request_id
  - path
  - latency_ms
  - user_id
  - error_code
- 不记录 API key 和完整敏感输入。

完成标准：

- `notes/D25_structured_logging.md`

### Day 26：健康检查和运维接口

P0：

- [FastAPI First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- 复读 Docker Compose 笔记。

阅读目标：

- 理解 health/readiness 的区别。

手写代码：

- 实现：
  - `GET /health`：进程活着即可
  - `GET /ready`：检查 MongoDB、Redis、Milvus、Kafka 配置可用性
- 写 `docs/runbook.md`：
  - 服务启动失败怎么查
  - MongoDB 连不上怎么查
  - Kafka 消费慢怎么查
  - Milvus 查询慢怎么查

完成标准：

- `docs/runbook.md`

### Day 27：CI/CD 基础

P0：

- [GitHub Actions Quickstart](https://docs.github.com/en/actions/get-started/quickstart)

阅读目标：

- 理解 workflow、job、step。

手写代码：

- 写 `.github/workflows/ci.yml`：
  - checkout
  - setup python
  - install dependencies
  - run tests
- 如果暂时不装 lint，也至少跑 `pytest`。

完成标准：

- `notes/D27_github_actions_ci.md`

### Day 28：部署清单

P0：

- [Docker Get Started](https://docs.docker.com/get-started/)
- [FastAPI Settings and Environment Variables](https://fastapi.tiangolo.com/advanced/settings/)

阅读目标：

- 不追云平台，先整理部署前必须确认的工程项。

手写代码：

- 写 `docs/deployment_checklist.md`：
  - 环境变量是否齐全
  - 真实密钥是否未入库
  - 日志是否脱敏
  - 健康检查是否可用
  - 数据库是否有备份
  - Kafka topic 是否创建
  - Redis key 是否有 TTL
  - vLLM endpoint 是否可访问
  - CI 是否通过
  - 回滚方式是什么

完成标准：

- `docs/deployment_checklist.md`

---

## 8. 第 5 周前 2 天：性能和最终打包

### Day 29：最小性能压测和瓶颈观察

P0：

- 复读 Redis / logging / vLLM 笔记。

阅读目标：

- 只理解：平均延迟、P95、吞吐、错误率。

手写代码：

- 写 `scripts/simple_load_test.py`：
  - 并发请求 `POST /chat`
  - 输出 avg latency、P95 latency、error count
- 观察：
  - Redis cache hit 是否降低延迟
  - Kafka 异步索引是否避免 API 阻塞
  - LLM 调用是否是最大瓶颈

完成标准：

- `docs/performance_notes.md`

### Day 30：最终工程骨架打包

P0：

- 不读新资料。

手写代码：

- 整理 `README.md`：
  - 项目结构
  - 本地启动
  - 环境变量
  - API 列表
  - 数据流
  - 中间件职责
  - 常见排错
- 画最终架构图：

```text
FastAPI
  -> MongoDB: documents / conversations / task state
  -> Milvus: chunk vectors
  -> Redis: cache / session / rate limit
  -> Kafka: async indexing events
  -> vLLM: OpenAI-compatible LLM serving
```

完成标准：

- `README.md`
- `docs/final_architecture.md`
- `docs/interview_engineering_qa.md`

---

## 9. 每日学习日志模板

```markdown
# Dxx - 主题

## 今天读了什么
- 

## 今天手写了什么
- 

## 我现在能解释的 3 个概念
1.
2.
3.

## 今天遇到的错误
- 现象:
- 原因:
- 修复:

## 今天怎么使用 Claude Code
- 用它做了什么:
- 它给了什么帮助:
- 我如何验证它的建议:
- 它有没有犯错:

## 它和大模型应用的关系

## 明天继续的问题
```

---

## 10. 面试表达清单

30 天结束后，你至少要能回答：

1. FastAPI 项目怎么分层？
2. REST API 里 400、401、403、404、409、422 怎么区分？
3. MongoDB、Redis、Milvus 分别适合存什么？
4. 为什么 RAG 索引构建适合异步化？
5. Kafka 和 Redis 队列有什么区别？
6. Dockerfile 和 Docker Compose 分别解决什么问题？
7. vLLM 在私有化大模型应用里解决什么问题？
8. 环境变量和密钥为什么不能写死在代码里？
9. AI 应用日志里哪些信息必须记录，哪些不能记录？
10. 一个 RAG 服务上线前要检查哪些东西？
11. Claude Code 的 agentic loop 是什么？
12. Claude Code 的 tools、context、session、permissions 分别解决什么问题？
13. Claude Code 适合参与哪些工程任务，不适合直接接管哪些任务？
14. 怎么用 `CLAUDE.md`、hooks、permissions 降低 Claude Code 的误操作风险？
15. 使用 Claude Code 改代码后，你如何验证它没有引入 bug？

---

## 11. 最低配执行版

如果当天只有 60 分钟：

- 15 分钟读 P0
- 35 分钟手写一个函数、一个接口或一个配置文件
- 5 分钟写日志
- 5 分钟记录未解决的错误和下一步

如果当天真的只有 30 分钟：

- 10 分钟读 P0
- 15 分钟手写一个最小片段
- 5 分钟写日志

不要补 P1，不要扩大范围，不要重构昨天代码。副线的目标是每天接触工程肌肉，而不是一天练成。
