# Asynchronous Example
import asyncio
from mistralai import Mistral
import os

async def generate(content):
    async with Mistral(
        api_key=os.getenv("AI_TOKEN"),
    ) as mistral:

        res = await mistral.chat.complete_async(model="pixtral-12b-2409", messages=[
            {
                "content": content,
                "role": "user",
            },
        ])

        if res is not None:
            return res
        
