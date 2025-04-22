# Import the implementation from the file
import asyncio 
from acp_sdk.client import Client
from smolagents import LiteLLMModel
from fastacp import AgentCollection, ACPCallingAgent, ActionStep

model = LiteLLMModel(
        model_id="ollama_chat/qwen2.5:14b",
        num_ctx=8192) 

async def example() -> None:
    async with Client(base_url="http://localhost:8000") as client, Client(base_url="http://localhost:8001") as enterprise:
        agent_collection = await AgentCollection.from_acp(client, enterprise)  
        acp_agents = {agent.name: agent for agent in agent_collection.agents}
        print(acp_agents) 
        acpagent = ACPCallingAgent(acp_agents=acp_agents, model=model)
        await acpagent.run("how far is japan from australia?")  

if __name__ == '__main__': 
    asyncio.run(example())