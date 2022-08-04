import os
import string
import asyncio
from mdisky import Mdisk
from pyrogram import Client, filters


BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

API_KEY = os.environ.get("API_KEY", "ox1G5YFFLX0uBxLee7Mn")


app = Client("tgid", bot_token=BOT_TOKEN, api_hash=API_HASH, api_id=API_ID)


@app.on_message(filters.command(['start']))
async def start(client, message):
    await message.reply_text(text=f"Hello 👋", reply_to_message_id=message.message_id)


@app.on_message(filters.command(['mdisk']))
async def id(client, message):
    await client.send_chat_action(message.chat.id, "typing")
    mdisk = Mdisk(API_KEY)

    mt = message.text
    if (" " in message.text):
        cmd, url = message.text.split(" ", 1)
    link = await mdisk.convert(url)
    await message.reply_text(text=f"{link}")
    print(link)
    #await message.reply_text(text=f"`{message.chat.id}`", reply_to_message_id=message.message_id)


app.run()