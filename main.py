import discord
from discord.ext import commands
import asyncio
import os

TOKEN = os.environ['TOKEN']
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

async def load_extensions():
    """
    Get all the cogs from the cog folder and add them to the bot.
    """
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')

async def main():
    """
    Start and run the bot.\n
    Must be run with asyncio.run()
    """
    async with bot:
        await load_extensions()
        print('Running Bot')
        await bot.start(TOKEN)

asyncio.run(main())
