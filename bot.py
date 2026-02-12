import asyncio
from telegram import Bot

TOKEN = "ТВОЙ_ТОКЕН"
CHAT_ID = "ТВОЙ_CHAT_ID"

PHOTO_URL = "https://via.placeholder.com/600x400.jpg"
CAPTION = "Сообщение каждые 15 минут"

bot = Bot(token=TOKEN)

async def send_loop():
    while True:
        await bot.send_photo(
            chat_id=CHAT_ID,
            photo=PHOTO_URL,
            caption=CAPTION
        )
        await asyncio.sleep(900)

asyncio.run(send_loop())
