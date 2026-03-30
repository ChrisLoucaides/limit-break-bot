import logging
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

# ----- Discord bot -----
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)


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

    if score < config.CONFIDENCE_THRESHOLD:
        answer = "I'm not 100% sure on how to answer that question, please wait until the real Afro or another TO responds"

    logger.info(f"Match result: {answer}, score: {score}")

    if answer:
        await message.channel.send(answer)

    await bot.process_commands(message)


# ----- Run bot -----
bot.run(DISCORD_TOKEN)
