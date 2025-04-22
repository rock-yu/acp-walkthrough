from collections.abc import AsyncGenerator
from acp_sdk.models import Message, MessagePart
from acp_sdk.server import Context, RunYield, RunYieldResume, Server

from crewai import Crew, Task, Agent
from crewai_tools import SerperDevTool
from langchain_ollama import ChatOllama
from llamaguardprompt import prompt_template

import logging 
logger = logging.getLogger(__name__)


server = Server()

guardian = ChatOllama(model="llama-guard3:1b",temperature = 0.8,
    num_predict = 1024)

@server.agent()
async def llama_guard(input: list[Message], context: Context) -> AsyncGenerator[RunYield, RunYieldResume]:
    "This is an agent for safety evaluation, it uses LLama guard to check whether a prompt is safe or unsafe"
    prompt = prompt_template(input[0].parts[0].content)
    response = guardian.invoke([('human',prompt)]).content
    logger.info(response)

    yield Message(parts=[MessagePart(content=str(response))])


if __name__ == "__main__":
    server.run(port=8001)