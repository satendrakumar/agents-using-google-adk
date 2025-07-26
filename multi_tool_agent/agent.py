import datetime
import logging
import os
import threading
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

WEATHER_AGENT_MODEL_NAME = os.getenv("WEATHER_AGENT_MODEL_NAME")

logger = logging.getLogger(__name__)


def get_weather(city: str) -> dict:
    logger.info(f"########## Weather tool calling from Thread {threading.current_thread().name}")
    if city.lower() == "new york":

        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


def get_current_time(city: str) -> dict:
    logger.info(f"########## Current time tool calling from Thread {threading.current_thread().name}")
    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    return {"status": "success", "report": report}


root_agent = Agent(
    name="weather_time_agent",
    model=LiteLlm(model=WEATHER_AGENT_MODEL_NAME),
    description="Agent to answer questions about the time and weather in a city.",
    instruction="You are a helpful agent who can answer user questions about the time and weather in a city.",
    tools=[get_weather, get_current_time],
)

class MyAgent(Agent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.se