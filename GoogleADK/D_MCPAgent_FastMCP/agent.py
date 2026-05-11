from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools.mcp_tool import MCPToolset, StdioConnectionParams

server_params = {"command":"python",
                                      "args":["/home/zadmin/Desktop/B7_GAAP_GCP/mcpserver/mcpserver2.py",'stdio']}

conn = StdioConnectionParams(server_params=server_params, timeout=120)
tools = MCPToolset(connection_params=conn)



agent_prompt = """ You are an expert agentic assistant to human users which provides correct and precise information.
you are provided with multiple tools, use the tools wherever it suits."""

root_agent = LlmAgent(name='customerServiceWorkflow',
                      model = "gemini-2.5-flash",
                      instruction=agent_prompt,
                                          
                      description = "Assistant Agent",
                      tools=[tools]
                      )

app = root_agent