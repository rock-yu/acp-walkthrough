import asyncio
from acp_sdk.client import Client
from acp_sdk.models import (
    Message,
    MessagePart,
)
from colorama import Fore

async def example() -> None:
    while True: 
        async with Client(base_url="http://localhost:8000") as client, Client(base_url="http://localhost:8001") as enterprise:
            prompt = input(Fore.LIGHTMAGENTA_EX + '✏️ Enter your prompt: ' + Fore.RESET) 

            async for agent in client.agents(): 
                print(agent) 
            # # commentary = await client.run_sync(
            # #     agent="ollama_smolagents", inputs=[Message(parts=[MessagePart(content=prompt, content_type="text/plain")])]
            # # )
            # print(Fore.LIGHTMAGENTA_EX + commentary.outputs[0].parts[0].content + Fore.RESET)

    

if __name__ == "__main__":
    asyncio.run(example())