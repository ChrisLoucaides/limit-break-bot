import os
import asyncio
import logging
from aiohttp import web
import discord
from discord.ext import commands
import config
from matcher import match_intent

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
    if message.author.bot: return
    if message.channel.id != CHANNEL_ID: return

    content = message.content.strip()
    if len(content) < 6: return

    answer, score = match_intent(content)
    logger.info(f"Match result: {answer}, score: {score}")
    if answer:
        await message.channel.send(answer)
    await bot.process_commands(message)


# ----- Web server for uptime -----
async def handle(request):
    return web.Response(text="Bot is running")


async def start_web_server():
    app = web.Application()
    app.add_routes([web.get("/", handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.environ.get("PORT", 8080)))
    await site.start()
    logger.info("Web server started on port %s", os.environ.get("PORT", 8080))


# ----- Main entrypoint -----
async def main():
    await start_web_server()
    await bot.start(DISCORD_TOKEN)  # non-blocking inside asyncio loop


if __name__ == "__main__":
    asyncio.run(main())

asyncio.run(main())
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
