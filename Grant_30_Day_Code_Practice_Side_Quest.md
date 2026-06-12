# Grant 的 30 天 AI 应用代码骨架练习支线

> 定位：专门练大模型应用开发里的通用代码套路。每天 30 分钟，不补 Python 基础，不追大而全，只练 RAG、Agent、MCP、LangChain、多模态、工程化里最常出现的小代码骨架。
>
> 核心目标：30 天后，你不是精通所有框架，而是看到一个 RAG / Agent / 多模态项目时，知道常见模块怎么写、放在哪里、怎么串起来。

---

## 0. 执行原则

### 0.1 30 天只做骨架版

每天只练一个小片段，代码量控制在 20-60 行。

不要追求：

- 完整项目
- 复杂框架封装
- 生产级异常处理
- 所有工具都接真实服务

只追求：

- 看懂这个模块解决什么问题
- 能照着手敲
- 能改 1-3 行
- 能跑通或用 mock 跑通

### 0.2 每天 30 分钟节奏

```text
5 分钟：看最小代码骨架
15 分钟：照着手敲，不复制
5 分钟：做一个小改造
5 分钟：运行 + 记录
```

### 0.3 Claude Code 陪练方式

每天可以用 Claude Code，但它是助教，不是代写员。

推荐提示词：

```text
今天我练习的主题是：xxx。
请给我一个不超过 60 行的最小代码骨架。
要求：先给代码，再逐行解释，最后给我一个只改 1-3 行的小练习。
不要写完整项目。
```

```text
请 review 我刚才手敲的代码，只指出 bug、边界问题和我需要理解的 3 个点。不要做无关重构。
```

---

## 1. 30 天总结构

```text
第 1 周：RAG 通用代码骨架
第 2 周：Agent / Tool / LangChain / MCP 通用代码骨架
第 3 周：多模态 + LLM API 封装骨架
第 4 周：工程化 + Eval / Trace 骨架
Day 29-30：整合成一个小型 AI 应用骨架
```

---

## 2. 每日记录模板

```markdown
# Dxx - 主题

## 今天练的模块

## 这个模块在 AI 应用里解决什么问题

## 我手敲了什么代码

## 我改了哪 1-3 行

## 我能解释的关键函数 / 类

## 报错或卡点

## 明天继续练什么
```

---

## 3. 第 1 周：RAG 通用代码骨架

目标：能写出 `loader -> cleaner -> splitter -> metadata -> retriever -> context -> answer` 的最小链路。

### Day 1：Markdown / TXT Loader

练习目标：

- 写一个本地文档加载函数。

代码骨架：

```python
from pathlib import Path


def load_text_file(path: str) -> dict:
    file_path = Path(path)
    return {
        "source": str(file_path),
        "title": file_path.stem,
        "text": file_path.read_text(encoding="utf-8"),
    }


doc = load_text_file("sample.md")
print(doc["title"])
print(doc["text"][:100])
```

小改造：

- 增加字段 `file_type`。
- 如果文件不存在，返回 `None`。

完成标准：

- 能解释 `source / title / text` 为什么要分开存。

### Day 2：文档清洗 Cleaner

练习目标：

- 写一个简单清洗函数，去空行、去多余空格。

代码骨架：

```python
def clean_text(text: str) -> str:
    lines = []
    for line in text.splitlines():
        clean_line = line.strip()
        if clean_line:
            lines.append(clean_line)
    return "\n".join(lines)


raw = "  Title  \n\n  line one  \n\nline two"
print(clean_text(raw))
```

小改造：

- 把连续多个空格压成一个空格。

完成标准：

- 能解释清洗太激进会丢什么信息。

### Day 3：固定长度 Chunk Splitter

练习目标：

- 写一个带 overlap 的 chunk 切分器。

代码骨架：

```python
def split_text(text: str, chunk_size: int = 200, overlap: int = 40) -> list[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks


chunks = split_text("abcdefghijklmnopqrstuvwxyz" * 20, chunk_size=50, overlap=10)
print(len(chunks))
print(chunks[0])
```

小改造：

- 如果 `overlap >= chunk_size`，抛出 `ValueError`。

完成标准：

- 能解释为什么 RAG 需要 overlap。

### Day 4：Metadata Builder

练习目标：

- 给 chunks 加 source、chunk_id、index、权限信息。

代码骨架：

```python
def build_chunks(document: dict, chunks: list[str]) -> list[dict]:
    records = []
    for index, text in enumerate(chunks):
        records.append({
            "chunk_id": f"{document['title']}_{index}",
            "document_title": document["title"],
            "source": document["source"],
            "chunk_index": index,
            "text": text,
            "allowed_roles": ["user"],
        })
    return records


doc = {"title": "note", "source": "note.md"}
records = build_chunks(doc, ["hello", "world"])
print(records[0])
```

小改造：

- 增加 `created_at` 字段。

完成标准：

- 能解释 metadata 对 citation 和权限过滤的作用。

### Day 5：Embedding Client Mock

练习目标：

- 写一个 embedding client 接口，先用 mock 向量。

代码骨架：

```python
class EmbeddingClient:
    def embed_text(self, text: str) -> list[float]:
        length = len(text)
        return [float(length % 10), float(length % 7), float(length % 5)]

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        return [self.embed_text(text) for text in texts]


client = EmbeddingClient()
print(client.embed_text("hello"))
print(client.embed_batch(["hello", "world"]))
```

小改造：

- 增加空字符串校验。

完成标准：

- 能解释为什么先写 mock client 对测试有帮助。

### Day 6：Vector Search Mock

练习目标：

- 写一个不用真实向量库的 top_k 检索。

代码骨架：

```python
def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def search(query_vector: list[float], records: list[dict], top_k: int = 3) -> list[dict]:
    scored = []
    for record in records:
        score = dot(query_vector, record["embedding"])
        scored.append({**record, "score": score})
    return sorted(scored, key=lambda x: x["score"], reverse=True)[:top_k]


records = [
    {"chunk_id": "1", "text": "FastAPI", "embedding": [1, 2, 3]},
    {"chunk_id": "2", "text": "Redis", "embedding": [2, 1, 0]},
]
print(search([1, 1, 1], records))
```

小改造：

- 增加 `score_threshold`。

完成标准：

- 能解释 top_k 和 threshold 的区别。

### Day 7：RAG Answer Chain 骨架

练习目标：

- 串起 query -> embed -> search -> context -> answer。

代码骨架：

```python
def build_context(results: list[dict]) -> str:
    lines = []
    for item in results:
        lines.append(f"[{item['chunk_id']}] {item['text']}")
    return "\n".join(lines)


def answer_with_context(question: str, context: str) -> dict:
    return {
        "answer": f"Based on context, answer question: {question}",
        "context": context,
    }


results = [{"chunk_id": "note_0", "text": "FastAPI is a Python web framework."}]
context = build_context(results)
print(answer_with_context("What is FastAPI?", context))
```

小改造：

- 返回 `citations` 列表。

完成标准：

- 能讲清 RAG 最小链路。

---

## 4. 第 2 周：Agent / Tool / LangChain / MCP 骨架

目标：能写出 `tool schema -> registry -> executor -> agent loop -> LangChain tool -> MCP tool` 的最小链路。

### Day 8：Tool Schema

练习目标：

- 用 dict 描述一个工具。

代码骨架：

```python
weather_tool = {
    "name": "get_weather",
    "description": "Get weather for a city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "City name"}
        },
        "required": ["city"],
    },
}

print(weather_tool["name"])
```

小改造：

- 增加一个 `get_document` 工具 schema。

完成标准：

- 能解释 name、description、parameters 分别给谁看。

### Day 9：Tool Registry

练习目标：

- 写一个工具注册表。

代码骨架：

```python
def get_weather(city: str) -> dict:
    return {"city": city, "weather": "sunny"}


TOOLS = {
    "get_weather": get_weather,
}


def call_tool(name: str, arguments: dict) -> dict:
    tool = TOOLS.get(name)
    if tool is None:
        return {"error": f"unknown tool: {name}"}
    return tool(**arguments)


print(call_tool("get_weather", {"city": "Shanghai"}))
```

小改造：

- 增加 `get_time` 工具。

完成标准：

- 能解释 registry 解决什么问题。

### Day 10：Tool Executor + Error

练习目标：

- 给工具执行增加异常捕获和结构化返回。

代码骨架：

```python
def divide(a: float, b: float) -> dict:
    return {"result": a / b}


TOOLS = {"divide": divide}


def execute_tool(name: str, arguments: dict) -> dict:
    try:
        if name not in TOOLS:
            return {"ok": False, "error": "unknown_tool"}
        result = TOOLS[name](**arguments)
        return {"ok": True, "result": result}
    except Exception as exc:
        return {"ok": False, "error": type(exc).__name__, "message": str(exc)}


print(execute_tool("divide", {"a": 1, "b": 0}))
```

小改造：

- 增加 `duration_ms` 字段。

完成标准：

- 能解释为什么工具输出要结构化。

### Day 11：Agent Loop Mock

练习目标：

- 写一个模型选择工具的 mock agent loop。

代码骨架：

```python
def mock_model_decide(user_input: str) -> dict:
    if "weather" in user_input.lower():
        return {"type": "tool_call", "name": "get_weather", "arguments": {"city": "Shanghai"}}
    return {"type": "final", "answer": "I can answer directly."}


def run_agent(user_input: str) -> dict:
    decision = mock_model_decide(user_input)
    if decision["type"] == "tool_call":
        tool_result = call_tool(decision["name"], decision["arguments"])
        return {"answer": f"Tool result: {tool_result}"}
    return {"answer": decision["answer"]}


print(run_agent("What is the weather?"))
```

小改造：

- 增加最大工具调用次数 `max_steps`。

完成标准：

- 能解释 agent loop 和普通函数调用的区别。

### Day 12：LangChain Tool 包装

练习目标：

- 了解 LangChain 里 tool 包装的最小形态。

代码骨架：

```python
try:
    from langchain_core.tools import tool
except ImportError:
    tool = None


if tool:
    @tool
    def get_weather(city: str) -> str:
        """Get weather for a city."""
        return f"The weather in {city} is sunny."

    print(get_weather.name)
else:
    print("Install langchain-core to run this example.")
```

小改造：

- 包装一个 `search_docs(query: str)` 工具。

完成标准：

- 能解释 LangChain tool 和普通 Python 函数的关系。

### Day 13：MCP Server 最小工具骨架

练习目标：

- 理解 MCP server 是把工具标准化暴露给 agent 的服务。

代码骨架：

```python
# Pseudocode skeleton. Use real MCP SDK when environment is ready.

TOOLS = {
    "search_docs": {
        "description": "Search local documents",
        "input_schema": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
    }
}


def search_docs(query: str) -> dict:
    return {"matches": [{"title": "note", "snippet": f"Result for {query}"}]}


def handle_tool_call(name: str, arguments: dict) -> dict:
    if name == "search_docs":
        return search_docs(**arguments)
    return {"error": "unknown_tool"}


print(handle_tool_call("search_docs", {"query": "RAG"}))
```

小改造：

- 增加 `get_document(document_id)`。

完成标准：

- 能解释 MCP 和本地 tool registry 的区别。

### Day 14：Agent 调 MCP Tool 的概念骨架

练习目标：

- 写出 agent -> MCP client -> MCP server tool 的调用形状。

代码骨架：

```python
class MockMCPClient:
    def call_tool(self, name: str, arguments: dict) -> dict:
        return handle_tool_call(name, arguments)


def agent_with_mcp(question: str, mcp_client: MockMCPClient) -> dict:
    tool_result = mcp_client.call_tool("search_docs", {"query": question})
    return {
        "answer": "I searched documents before answering.",
        "tool_result": tool_result,
    }


client = MockMCPClient()
print(agent_with_mcp("What is RAG?", client))
```

小改造：

- 如果问题不包含 `doc` 或 `RAG`，直接回答，不调用 MCP。

完成标准：

- 能解释 LangChain/LangGraph 是应用内编排，MCP 是外部工具接入协议。

---

## 5. 第 3 周：多模态 + LLM API 封装骨架

目标：能写出 `client -> retry -> structured output -> image input -> vision result` 的最小骨架。

### Day 15：OpenAI-Compatible Client

练习目标：

- 封装一个模型调用 client，先用 mock。

代码骨架：

```python
class LLMClient:
    def __init__(self, base_url: str, model: str):
        self.base_url = base_url
        self.model = model

    def generate(self, prompt: str) -> dict:
        return {
            "model": self.model,
            "text": f"Mock answer for: {prompt}",
        }


client = LLMClient(base_url="http://localhost:8000/v1", model="local-model")
print(client.generate("hello"))
```

小改造：

- 增加 `temperature` 参数。

完成标准：

- 能解释为什么业务代码不要直接散落 API 调用。

### Day 16：Retry with Backoff

练习目标：

- 写一个简单重试包装器。

代码骨架：

```python
import time


def retry_call(fn, max_attempts: int = 3):
    for attempt in range(1, max_attempts + 1):
        try:
            return fn()
        except Exception as exc:
            if attempt == max_attempts:
                raise
            time.sleep(attempt)


count = 0

def unstable():
    global count
    count += 1
    if count < 2:
        raise RuntimeError("temporary error")
    return "ok"


print(retry_call(unstable))
```

小改造：

- 返回每次 attempt 的日志。

完成标准：

- 能解释哪些错误可以重试，哪些不该重试。

### Day 17：Structured Output Parser

练习目标：

- 把模型输出 JSON 字符串解析并校验字段。

代码骨架：

```python
import json


def parse_task_plan(text: str) -> dict:
    data = json.loads(text)
    if "steps" not in data:
        raise ValueError("missing steps")
    return data


raw = '{"steps": [{"name": "load docs"}, {"name": "retrieve"}]}'
print(parse_task_plan(raw))
```

小改造：

- 校验每个 step 都有 `name`。

完成标准：

- 能解释为什么 structured output 仍然需要本地校验。

### Day 18：Image to Base64 / Data URL

练习目标：

- 写图片转 base64 的工具函数。

代码骨架：

```python
import base64
from pathlib import Path


def image_to_data_url(path: str, mime_type: str = "image/png") -> str:
    data = Path(path).read_bytes()
    encoded = base64.b64encode(data).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


print(image_to_data_url("sample.png")[:50])
```

小改造：

- 根据后缀自动判断 `image/png` 或 `image/jpeg`。

完成标准：

- 能解释 vision API 为什么常用 base64 / URL 输入。

### Day 19：Vision Request Builder

练习目标：

- 构造图文输入请求结构。

代码骨架：

```python
def build_vision_request(question: str, image_data_url: str) -> dict:
    return {
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {"type": "image_url", "image_url": {"url": image_data_url}},
                ],
            }
        ]
    }


payload = build_vision_request("What is in this image?", "data:image/png;base64,xxx")
print(payload)
```

小改造：

- 支持多张图片。

完成标准：

- 能解释 text + image 为什么要放进同一个 message。

### Day 20：OCR Result Structuring

练习目标：

- 模拟 OCR 输出，并转成结构化字段。

代码骨架：

```python
def parse_invoice_ocr(text: str) -> dict:
    result = {"invoice_no": None, "amount": None}
    for line in text.splitlines():
        if line.startswith("Invoice:"):
            result["invoice_no"] = line.split(":", 1)[1].strip()
        if line.startswith("Amount:"):
            result["amount"] = line.split(":", 1)[1].strip()
    return result


ocr_text = "Invoice: INV-001\nAmount: 123.45"
print(parse_invoice_ocr(ocr_text))
```

小改造：

- 增加 `date` 字段。

完成标准：

- 能解释多模态项目里“识别”和“结构化”是两步。

### Day 21：Image Analysis Chain

练习目标：

- 串起 image input -> prompt -> model mock -> parser。

代码骨架：

```python
def analyze_image(image_path: str, question: str) -> dict:
    image_data_url = f"mock://{image_path}"
    request = build_vision_request(question, image_data_url)
    model_output = "Invoice: INV-001\nAmount: 123.45\nDate: 2026-06-12"
    structured = parse_invoice_ocr(model_output)
    return {"request": request, "result": structured}


print(analyze_image("invoice.png", "Extract invoice fields."))
```

小改造：

- 返回 `raw_output`。

完成标准：

- 能讲清多模态最小链路。

---

## 6. 第 4 周：工程化 + Eval / Trace 骨架

目标：能写出 `config -> logging -> middleware -> tests -> eval runner -> trace summary` 的最小骨架。

### Day 22：Settings from Env

练习目标：

- 写一个配置读取类。

代码骨架：

```python
import os


class Settings:
    def __init__(self):
        self.llm_base_url = os.getenv("LLM_BASE_URL", "http://localhost:8000/v1")
        self.llm_model = os.getenv("LLM_MODEL", "mock-model")
        self.redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")


settings = Settings()
print(settings.llm_model)
```

小改造：

- 增加 `milvus_uri`。

完成标准：

- 能解释为什么密钥和连接串不写死。

### Day 23：Structured Logger

练习目标：

- 打印结构化日志。

代码骨架：

```python
import json
import time


def log_event(event: str, **fields):
    record = {
        "event": event,
        "timestamp": time.time(),
        **fields,
    }
    print(json.dumps(record, ensure_ascii=False))


log_event("tool_call", tool="search_docs", duration_ms=12, ok=True)
```

小改造：

- 增加 `request_id`。

完成标准：

- 能解释为什么日志不要只写自然语言。

### Day 24：Request ID Middleware 骨架

练习目标：

- 理解每个请求有 request_id 的意义。

代码骨架：

```python
import uuid


def handle_request(path: str, handler):
    request_id = str(uuid.uuid4())
    log_event("request_start", request_id=request_id, path=path)
    result = handler()
    log_event("request_end", request_id=request_id, path=path)
    return result


def fake_handler():
    return {"ok": True}


print(handle_request("/chat", fake_handler))
```

小改造：

- 记录 `duration_ms`。

完成标准：

- 能解释 request_id 如何帮助排错。

### Day 25：Fake Repository for Tests

练习目标：

- 写 fake repository，避免测试依赖真实数据库。

代码骨架：

```python
class FakeDocumentRepo:
    def __init__(self):
        self.documents = {}

    def save(self, document_id: str, text: str):
        self.documents[document_id] = {"id": document_id, "text": text}

    def get(self, document_id: str):
        return self.documents.get(document_id)


repo = FakeDocumentRepo()
repo.save("doc1", "hello")
print(repo.get("doc1"))
```

小改造：

- 增加 `list_all()`。

完成标准：

- 能解释 fake repo 对测试的价值。

### Day 26：Eval Dataset Reader

练习目标：

- 读取 JSONL 评测集。

代码骨架：

```python
import json


def read_jsonl(path: str) -> list[dict]:
    cases = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                cases.append(json.loads(line))
    return cases


# eval_cases.jsonl:
# {"question": "What is RAG?", "expected": "retrieval"}
```

小改造：

- 如果某行 JSON 解析失败，记录错误并跳过。

完成标准：

- 能解释 eval dataset 为什么要版本化。

### Day 27：Rule-Based Grader

练习目标：

- 写一个最简单的规则评分器。

代码骨架：

```python
def grade_answer(answer: str, expected_keywords: list[str]) -> dict:
    missing = []
    for keyword in expected_keywords:
        if keyword.lower() not in answer.lower():
            missing.append(keyword)
    return {
        "passed": len(missing) == 0,
        "missing": missing,
    }


print(grade_answer("RAG uses retrieval.", ["RAG", "retrieval"]))
```

小改造：

- 增加 `score`，范围 0-1。

完成标准：

- 能解释 rule grader 和 LLM judge 的区别。

### Day 28：Trace Span 骨架

练习目标：

- 写一个 trace span 数据结构。

代码骨架：

```python
import time
from contextlib import contextmanager


@contextmanager
def span(name: str, trace: list[dict]):
    start = time.time()
    record = {"name": name, "start": start}
    try:
        yield record
        record["ok"] = True
    except Exception as exc:
        record["ok"] = False
        record["error"] = str(exc)
        raise
    finally:
        record["duration_ms"] = int((time.time() - start) * 1000)
        trace.append(record)


trace = []
with span("retrieve", trace):
    time.sleep(0.01)
print(trace)
```

小改造：

- 给 span 增加 `metadata`。

完成标准：

- 能解释 trace 和普通 log 的区别。

---

## 7. Day 29-30：整合小项目骨架

### Day 29：AI App Skeleton

练习目标：

- 把前 28 天模块串成一个骨架，不接真实服务。

骨架结构：

```text
app/
  rag.py
  tools.py
  agent.py
  multimodal.py
  llm_client.py
  eval_runner.py
  tracing.py
```

任务：

- 写一个 `run_demo()`：
  - 加载文档
  - 切 chunk
  - mock 检索
  - agent 决定是否调用 `search_docs`
  - 输出 answer、citations、trace

完成标准：

- 能跑出一个完整 demo 输出。

### Day 30：代码骨架复盘

任务：

- 写 `docs/code_skeleton_review.md`

内容：

```markdown
# AI 应用代码骨架复盘

## RAG 骨架我能写哪些

## Agent / MCP / LangChain 骨架我能写哪些

## 多模态骨架我能写哪些

## 工程化 / Eval / Trace 骨架我能写哪些

## 我最不熟的 5 个模块

## 下一轮 30 天应该深练什么
```

完成标准：

- 能用 5 分钟讲清一个 AI 应用项目通常有哪些代码模块。

---

## 8. 结束标准

30 天结束，你应该能做到：

- 看懂 RAG 项目里 loader、splitter、retriever、context builder 的代码。
- 看懂 Agent 项目里 tool schema、tool registry、tool executor、agent loop 的代码。
- 知道 LangChain tool 包装和普通 Python 函数的关系。
- 知道 MCP 是把外部工具标准化暴露给 agent 的协议层。
- 能写多模态项目里的 image input、vision request、OCR structuring 骨架。
- 能写 config、structured logging、fake repo、eval reader、rule grader、trace span 的最小代码。
- 能用 Claude Code review 自己的代码，而不是完全依赖它生成。
