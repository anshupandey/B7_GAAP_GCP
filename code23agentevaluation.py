
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
import mlflow
from mlflow.genai import scorer
import asyncio
from mlflow.genai.scorers import ToolCallCorrectness, ToolCallEfficiency
from dotenv import load_dotenv
from langchain.tools import tool
import requests,json,wikipedia
load_dotenv()


mlflow.set_tracking_uri("http://20.81.137.57:5000/")
mlflow.set_experiment("AgentEvaluation")


tool()
def get_current_weather(city:str)->dict:
    """ this funciton can be used to get current weather information"""
    api_key="6a8b0ac166a37e2b7a38e64416b3c3fe"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    response = json.loads(response.content.decode())
    output = {"city":city,"weather":response['weather'][0]['description'],
              "temperature":response['main']['temp'], "unit":"kelvin"
              }
    return output

tool()
def get_wikipedia_summary(query:str)->str:
    "get informaiton about any places, people, events from wikipedia"
    response = wikipedia.summary(query)
    return response


tools = [get_current_weather,get_wikipedia_summary]

def main():

    agent = create_agent("google_genai:gemini-2.5-flash",tools)

    def predict_function(task:str):
        response = agent.invoke({"messages":[{"role":'user',"content":task}]})
        return response

    eval_data = [{"inputs":{"task":"what is temperature in delhi today?"},
                "expectations":{"answer":"The weather in Delhi is haze with a temperature of 306.2 Kelvin."},
                "tags":{"topic":"weather"}},
                {"inputs":{"task":"what is temperature in Mumbai today?"},
                "expectations":{"answer":"The current temperature in Mumbai is 307.14 Kelvin."},
                "tags":{"topic":"weather"}},
                {"inputs":{"task":"what is temperature in London today?"},
                "expectations":{"answer":'The weather in London is broken clouds with a temperature of 276.07 Kelvin.'},
                "tags":{"topic":"weather"}},
                ]


    @scorer
    def exact_match(outputs,expectations):
        return outputs['messages'][-1].content==expectations['answer']


    results = mlflow.genai.evaluate(data=eval_data, predict_fn= predict_function,
                                    scorers=[exact_match,ToolCallCorrectness(model="gemini:/gemini-2.5-flash"), ToolCallEfficiency(model="gemini:/gemini-2.5-flash")])

if __name__=="__main__":
    main()
