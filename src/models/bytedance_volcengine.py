from langchain_openai import ChatOpenAI
from pydantic import SecretStr
import os

bytedance_volcengine_chat_model = ChatOpenAI(
  # 模型名称
  model="doubao-seed-1-6-lite-251015",
  # 火山引擎的open ai格式的base url（如果不设置默认会走open ai官方的base url）
  base_url="https://ark.cn-beijing.volces.com/api/v3/",
  # apikey
  api_key=SecretStr(os.getenv("BYTE_DANCE_VOLCENGINE_LLM_API_KEY") or ""),
  # 模型温度
  temperature=0
)
