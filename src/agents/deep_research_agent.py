from deepagents import create_deep_agent
from src.tools import internet_search
from src.prompts.template import apply_prompt_template
from src.models.ali_bailian import ali_bailian_chat_model

deep_research_agent = create_deep_agent(
  name="deep_research_agent",
  tools=[internet_search],
  system_prompt=apply_prompt_template('deep_research_agent'),
  model=ali_bailian_chat_model,
)