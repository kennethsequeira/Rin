import discord
from discord import Intents
from discord.ext import commands
import os
from dotenv import load_dotenv
# Grabs the bot's token from the .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = Intents.all()
bot = commands.Bot(command_prefix=".")

# Loads in all extensions
initial_extensions = ['Cogs.rininfo', 'Cogs.reddit', 'Cogs.plugin_tools', 'Cogs.global', 'Cogs.chat',  'Cogs.images', 'Cogs.rinping']
for extension in initial_extensions:
    bot.load_extension(extension)

bot.run(TOKEN)