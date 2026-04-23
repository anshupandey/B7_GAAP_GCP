from google.adk.agents import LlmAgent

root_agent = LlmAgent(name='ChatAgent',
                      model='gemini-2.5-flash',
                      instruction = "You are a helpful assistant",
                      description = "Assistant Agent",
                      )
