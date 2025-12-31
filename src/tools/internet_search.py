import os
from typing import Literal
from dotenv import load_dotenv
from tavily import TavilyClient

# 加载 .env 文件中的环境变量
load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY") or "")

def internet_search(
  query: str,
  max_results: int = 5,
  topic: Literal["general", "news", "finance"] = "general",
  include_raw_content: bool = False,
):
  """Run a web search"""
  return tavily_client.search(
    query,
    max_results=max_results,
    include_raw_content=include_raw_content,
    topic=topic,
  )