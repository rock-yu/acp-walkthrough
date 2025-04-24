import asyncio
from acp_sdk.client import Client
from acp_sdk.models import (
    Message,
    MessagePart,
)

async def example() -> None:
    async with Client(base_url="http://localhost:8001") as client:
        run = await client.run_sync(
            agent="policy_agent", inputs=[Message(parts=[MessagePart(content="What is the waiting period for rehabilitation?", content_type="text/plain")])]
        )
        print(run)

if __name__ == "__main__":
    asyncio.run(example())