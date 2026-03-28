import discord
from discord.ext import commands
from config import DISCORD_TOKEN, CHANNEL_ID
from matcher import match_intent

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


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
    else:
        # Optional fallback
        pass

    await bot.process_commands(message)


bot.run(DISCORD_TOKEN)
