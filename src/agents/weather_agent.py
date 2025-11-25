from langchain.agents import create_agent
from src.models import bytedance_volcengine_chat_model
from src.prompts.template import apply_prompt_template
from src.tools.weather import get_weather

weather_agent = create_agent(
  # agent的名字
  name="weather-agent",
  # 使用的model
  model=bytedance_volcengine_chat_model,
  # agent的tools
  tools=[get_weather],
  # agent的系统提示词
  system_prompt=apply_prompt_template('weather_agent')
)