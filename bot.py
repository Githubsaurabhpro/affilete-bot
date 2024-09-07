import uvloop
import asyncio
from pyrogram import Client, filters
from decouple import config
print("Starting...")

uvloop.install()

APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")
FROM = [-1002278830292, -1001511276789]
TO = [-1002336608535]

try:
    BotzHubUser = Client(name=SESSION, api_id=APP_ID, api_hash=API_HASH, session_string=SESSION)
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

async def start_bot():
    await BotzHubUser.start()
    user = await BotzHubUser.get_me()
    print(f"Logged in as : {user.first_name}")

    await asyncio.Event().wait()

@BotzHubUser.on_message(filters.chat(FROM))
async def sender_bH(client, message):
    for i in TO:
        try:
            await client.copy_message(
                chat_id=i,
                from_chat_id=message.chat.id,
                message_id=message.id,
                caption=message.caption,
                caption_entities=message.caption_entities,
                reply_markup=message.reply_markup
            )
        except Exception as e:
            print(e)

BotzHubUser.run(start_bot())
