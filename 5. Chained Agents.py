import asyncio
from acp_sdk.client import Client
from acp_sdk.models import (
    Message,
    MessagePart,
)

async def example() -> None:
    async with Client(base_url="http://localhost:8001") as insurer, Client(base_url="http://localhost:8000") as hospital:
        run1 = await hospital.run_sync(
            agent="health_agent", inputs=[Message(parts=[MessagePart(content="Do i need rehabilitation for a shoulder reconstruction?", content_type="text/plain")])]
        )
        print(run1) 
        run2 = await insurer.run_sync(
            agent="policy_agent", inputs=[Message(parts=[MessagePart(content="What is the waiting period for rehabilitation?", content_type="text/plain")])]
        )
        print(run2)

if __name__ == "__main__":
    asyncio.run(example())