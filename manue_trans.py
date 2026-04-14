
# pip install gradio openai-whisper requests
# Windows 需要用“下载 + 配置环境变量”的方式安装 ffmpeg

import os
import subprocess
import tempfile
import requests
import gradio as gr
import whisper

# ================== 配置区 ==================
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
QWEN_MODEL = "qwen-turbo"

if not DASHSCOPE_API_KEY:
    raise RuntimeError("请先设置环境变量 DASHSCOPE_API_KEY")

# ================== Whisper 模型 ==================
print("加载 Whisper 模型中...")
whisper_model = whisper.load_model("medium")

# ================== 功能函数 ==================

def extract_audio(video_path):
    audio_path = os.path.join(os.path.dirname(video_path), "audio.wav")
    cmd = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-ar", "16000",
        "-ac", "1",
        audio_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return audio_path


def transcribe_audio(audio_path):
    result = whisper_model.transcribe(audio_path, language="zh")
    return result["text"]


def call_qwen(raw_text):
    prompt = f"""
你是一名资深中餐厨师和菜谱编辑。
以下是一段来自做菜视频的【口语化讲解】，内容可能凌乱、重复。

请将其整理为一份【清晰、专业、适合普通人照做的菜谱】。

严格按以下格式输出【纯文本】：

菜名：
用料：
- 材料 + 用量

步骤：
1. ...
2. ...

关键技巧：
- ...

【视频口语内容】：
{raw_text}
"""

    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    headers = {
        "Authorization": f"Bearer {DASHSCOPE_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": QWEN_MODEL,
        "input": {"prompt": prompt},
        "parameters": {
            "temperature": 0.3,
            "max_tokens": 1500
        }
    }

    resp = requests.post(url, headers=headers, json=data, timeout=120)
    resp.raise_for_status()
    return resp.json()["output"]["text"]


# ================== 主 Pipeline ==================

def video_to_recipe(video_file):
    if video_file is None:
        return "❌ 请先上传视频", "", None

    with tempfile.TemporaryDirectory() as tmp:
        video_path = os.path.join(tmp, "input.mp4")
        with open(video_path, "wb") as f:
            f.write(video_file.read())

        status = "🎧 正在提取音频..."
        audio_path = extract_audio(video_path)

        status = "🧠 Whisper 正在转写语音..."
        raw_text = transcribe_audio(audio_path)

        status = "🍳 Qwen 正在整理菜谱..."
        recipe_text = call_qwen(raw_text)

        output_path = os.path.join(tmp, "recipe.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(recipe_text)

        return raw_text, recipe_text, output_path


# ================== Gradio UI ==================

with gr.Blocks(title="做菜视频 → 自动菜谱（Demo）") as demo:
    gr.Markdown(
        """
# 🍳 做菜视频自动生成菜谱（AI Demo）

📤 上传一个做菜视频  
🎧 自动识别语音  
🧠 AI 整理成标准菜谱  
📄 可直接下载 TXT  

⚠️ 本页面仅用于演示，请勿上传超大或敏感视频
"""
    )

    video_input = gr.File(
        label="上传做菜视频（MP4）",
        file_types=[".mp4"]
    )

    run_btn = gr.Button("开始解析")

    raw_text_box = gr.Textbox(
        label="① Whisper 转写文本",
        lines=8
    )

    recipe_box = gr.Textbox(
        label="② AI 整理后的菜谱",
        lines=12
    )

    file_output = gr.File(
        label="③ 下载菜谱 TXT"
    )

    run_btn.click(
        fn=video_to_recipe,
        inputs=video_input,
        outputs=[raw_text_box, recipe_box, file_output]
    )

# ================== 启动（Demo 公网模式） ==================

demo.launch(
    share=True,          # ✅ 生成公网临时地址
    show_error=True,
    max_file_size=200,   # ✅ 限制上传 200MB（防止 demo 被玩坏）
)
