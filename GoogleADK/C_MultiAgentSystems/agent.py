from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import FunctionTool
import requests, json


# Creating a custom Tool with Google ADK
def get_current_weather(city:str)->dict:
    """ can be used to get/fetch current weather information for a city name
    """
    api_key = "6a8b0ac166a37e2b7a38e64416b3c3fe"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    response = response.content.decode()
    response = json.loads(response)
    output = {"City Name":city,"weather":response["weather"][0]['description'],
              "temperature":response['main']['temp'],
              "unit":"kelvin"}

    return output


get_current_weather_tool = FunctionTool(get_current_weather)


# Using a tool from Langchain with Google ADK
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

def wiki_tool(query:str):
    """this function can be used to fetch historical information about people, places, and events.
    arguments:
    - query: query to search on wikipedia in string format
    returns: wikipedia search results
    """
    output = wiki.run(query)
    return output


wiki_tool_adk = FunctionTool(wiki_tool)

agent_prompt = """ You are an expert agentic assistant to human users which provides correct and precise information.
you are provided with multiple tools, use the tools wherever it suits."""

root_agent = LlmAgent(name='customerServiceWorkflow',
                      model = "gemini-2.5-flash",
                      instruction=agent_prompt,
                                          
                      description = "Assistant Agent",
                      tools=[wiki_tool_adk,get_current_weather_tool]
                      )

app = root_agent