import os

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

CAPITAL_AGENT_MODEL_NAME = os.getenv("CAPITAL_AGENT_MODEL_NAME")

root_agent = LlmAgent(
    model=LiteLlm(model=CAPITAL_AGENT_MODEL_NAME),
    name="capital_agent",
    description="Answers user questions about the capital city of a given country.",
    instruction="You are a helpful agent that answers with the capital city of the country provided by the user."
)
