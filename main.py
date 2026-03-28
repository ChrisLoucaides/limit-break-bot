import os
import logging
from threading import Thread

import discord
from discord.ext import commands
from flask import Flask

from config import DISCORD_TOKEN, CHANNEL_ID
from matcher import match_intent

print("Bot is starting...")

# ----- Configure logging -----
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)

# ----- Discord Bot -----
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.id != CHANNEL_ID:
        return
    content = message.content.strip()
    if len(content) < 6:
        return
    answer, score = match_intent(content)
    if answer:
        await message.channel.send(answer)
    await bot.process_commands(message)

# ----- Flask Webserver -----
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# Start Flask in a separate thread
Thread(target=run_flask).start()

# Start Discord bot (blocking)
bot.run(DISCORD_TOKEN)