from langchain_openai import ChatOpenAI
import os

ali_bailian_chat_model = ChatOpenAI(
  # 模型名称
  model="qwen-plus",
  # qwen的open ai格式的base url（如果不设置默认会走open ai官方的base url）
  base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
  # apikey
  api_key=os.getenv("ALI_BAILIAN_LLM_API_KEY"),
  # 模型温度
  temperature=0
)
