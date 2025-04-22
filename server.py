from collections.abc import AsyncGenerator
from acp_sdk.models import Message, MessagePart
from acp_sdk.server import Context, RunYield, RunYieldResume, Server
from smolagents import ToolCallingAgent, ToolCollection, CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, VisitWebpageTool

server = Server()

model = LiteLLMModel(
    model_id="ollama_chat/qwen2.5:14b",
    api_base="http://localhost:11434",
    api_key="your-api-key",
    num_ctx=8192,
)

@server.agent()
async def ollama_smolagents(input: list[Message], context: Context) -> AsyncGenerator[RunYield, RunYieldResume]:
    "This is a CodeAgent with the ability to search the internet for pro level research"
    agent = CodeAgent(tools=[DuckDuckGoSearchTool(), VisitWebpageTool()], model=model)

    prompt = input[0].parts[0].content
    response = agent.run(prompt)

    yield Message(parts=[MessagePart(content=str(response))])


if __name__ == "__main__":
    server.run()