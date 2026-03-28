import os
import logging
from threading import Thread
from flask import Flask
import discord
from discord.ext import commands
from matcher import match_intent

# ----- Environment variables -----
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))

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
    if message.author.bot: return
    if message.channel.id != CHANNEL_ID: return
    content = message.content.strip()
    if len(content) < 6: return
    answer, score = match_intent(content)
    if answer:
        await message.channel.send(answer)
    await bot.process_commands(message)

# ----- Flask webserver for UptimeRobot -----
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_bot():
    bot.run(DISCORD_TOKEN)

# Start Discord bot in a separate thread
Thread(target=run_bot).start()

# Run Flask in main thread (Render health checks)
port = int(os.environ.get("PORT", 8080))
app.run(host="0.0.0.0", port=port)