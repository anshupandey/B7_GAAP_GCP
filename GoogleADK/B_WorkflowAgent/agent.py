from google.adk.agents import LlmAgent, SequentialAgent

# Classifier
classifer = LlmAgent(name='Classifier',
                      model='gemini-2.5-flash',
                      instruction = f""" You are expert query router, analyze the user query and identify the right intent of it, output one category from
    ['billing','technical','returns','human_escalation']
    Always follow below approach:
    1. billing: if the query is about payments, invoices, purchase orders, pricing, it is about billing
    2. returns: if the query is about returns, refunds, refund status, reorder, damaged products
    3. technical: if the query is about, product page crash, not able to login, account deactivated, payment failure, errors, 
    4. human_escalation: any other query
    """,
                      description = "Assistant Agent",
                      )



billing = LlmAgent(name='BillingAgent',
                      model='gemini-2.5-flash',
                      instruction = """You are a BIlling query resolver, customer executive, be polite and professional. Understand the billing query and provide the answer to the question.
    Provide answer in 2 lines. """,
                      description = "Assistant Agent",
                      )



root_agent = SequentialAgent(name='customerServiceWorkflow',
                                          
                      description = "Assistant Agent",
                      sub_agents=[classifer,billing]
                      )

app = root_agent