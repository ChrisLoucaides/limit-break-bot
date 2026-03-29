import logging
from threading import Thread
from flask import Flask
import discord
from discord.ext import commands
import config
from matcher import match_intent
import os

# ----- Env -----
DISCORD_TOKEN = config.DISCORD_TOKEN
CHANNEL_ID = config.CHANNEL_ID

# ----- Logging -----
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)

# ----- Discord bot -----
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
    logger.info(f"Match result: {answer}, score: {score}")

    if answer:
        await message.channel.send(answer)
    await bot.process_commands(message)

# ----- Flask for uptime -----
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

# Run Flask in a background thread
def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

Thread(target=run_flask, daemon=True).start()

# ----- MAIN THREAD: Run bot -----
logger.info("Starting Discord bot in main thread...")
bot.run(DISCORD_TOKEN)

# def run_bot():
#     logger.debug("Starting Discord bot thread...")
#     logger.debug(f"TOKEN EXISTS:  {bool(DISCORD_TOKEN)}")
#     bot.run(DISCORD_TOKEN)
#
#
# # Start Discord bot in a separate thread
# Thread(target=run_bot).start()
#
# # Run Flask in main thread (Render health checks)
# port = int(os.environ.get("PORT", 8080))
# app.run(host="0.0.0.0", port=port)
