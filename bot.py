import uvloop
import asyncio
from pyrogram import Client, filters
from decouple import config
print("Starting...")

uvloop.install()

# Necessary credentials, fill before running the bot
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")

# Add multiple channels by spacing. Example: FROM = "-10012345678 -10023456789 -10034567890"
FROM = config("FROM_CHANNEL")  # channel ids from bot will forward messages
TO = config("TO_CHANNEL")  # The channel ids im wich which userbot will forward messages

FROM = [int(i) for i in FROM.split()]
TO = [int(i) for i in TO.split()]

async def main():
    try:
        Bot = Client("Forward_Bot", api_id=APP_ID, api_hash=API_HASH, session_string=SESSION)
        await Bot.start()
        print("Bot started.")
        
        @Bot.on_message(filters.incoming & filters.chat(FROM))
        async def msg_sender(client, message):
            for i in TO:
                try:
                    await message.forward(i)
                except Exception as e:
                    print(f"Error forwarding message: {e}")
        
        await asyncio.Event().wait()
    except Exception as e:
        print(f"ERROR in starting userbot - {e}")

asyncio.run(main())
