from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import FloodWaitError

from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
API_ID = os.getenv('17575277')
API_HASH = os.getenv('06811043f4205a551d7f6870cd3c7292')

f = open('sub_baza.txt', 'r')
CHANNELS = f.readlines()

async def mainn():
    async with TelegramClient('subb_baza', 17575277, "06811043f4205a551d7f6870cd3c7292") as client:
        for channel in CHANNELS:
            try:
                await client(JoinChannelRequest(channel))
            except FloodWaitError as fwe:
                print(f'Waiting for {fwe}')
                await asyncio.sleep(delay=fwe.seconds)
            except Exception as err:
                print(f"Encountered an error while joining {channel}\n{err}")


asyncio.run(mainn())