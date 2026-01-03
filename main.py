# ================== IMPORTS ==================
import os
import asyncio
import logging
from pyrogram import Client, idle
from logging.handlers import RotatingFileHandler
from flask import Flask
from threading import Thread

# ================== LOGGING ==================
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=5_000_000, backupCount=5),
        logging.StreamHandler()
    ],
)
LOGGER = logging.getLogger(__name__)

# ================== BOT ==================
bot = Client(
    "StarkBot",                       # ✔ name kuch bhi rakh sakte ho
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH"),
    plugins=dict(root="plugins"),
    workers=20
)

# ================== BOT START ==================
async def main():
    await bot.start()
    me = await bot.get_me()
    LOGGER.info(f"🤖 @{me.username} started successfully")
    await idle()

# ================== FLASK KEEP ALIVE ==================
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is Alive!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

# ================== RUN ==================
if __name__ == "__main__":
    Thread(target=run_flask).start()   # Flask first
    asyncio.run(main())                # Pyrogram safe run
