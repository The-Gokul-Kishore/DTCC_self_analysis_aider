from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic import BaseModel, Field
from typing import Annotated
from pydantic_ai.providers.google_gla import GoogleGLAProvider
from pydantic_ai.messages import ModelMessage
import os
from dataclasses import dataclass
@dataclass
class Response(BaseModel):
    response :Annotated[str, Field(min_length=3)] 

model_name = "gemini-1.5-flash"
model = GeminiModel(
    model_name = model_name,
    provider=GoogleGLAProvider(api_key=os.getenv("GEMINI_API_KEY"))
)
agent:Agent[Response] = Agent(
    model=model,
    system_prompt=" you are a financial assitance agent in a Retrival Argumentation setup, you will help the user with the financail queires on the related data given to you",
    result_type=Response,
)

class RAG_Agent:
    def __init__(self,agent:Agent[Response]):
        self.agent = agent
    def get_prompt(self,user_request:str,similar_docs:list[str])->str:
        prompt = f"""
        the user request is as follows : {user_request}
        
        answer based on the relvant documents based on the query:
        {similar_docs}
        """
        return prompt
    async def run(self, query: str,history_context: list[ModelMessage]=None, context: list[str]=None) -> Response:

        prompt = self.get_prompt(user_request=query,similar_docs=context)
        response = await self.agent.run(user_prompt=prompt,message_history=history_context)
        return response
rag_agent:RAG_Agent = RAG_Agent(agent=agent)

