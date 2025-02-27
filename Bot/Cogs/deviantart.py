import asyncio
import os

import deviantart
import discord
from discord import Client
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
Client_ID = os.getenv("Client_ID")
Client_Secret = os.getenv("Client_Secret")
da = deviantart.Api(Client_ID, Client_Secret)


# the devartfetch gives out numbers, will need to get images instead
class devart(commands.Cog, discord.Client):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="devartfind")
    async def on_message(ctx, search: str):
        devartfind = da.browse(endpoint=f"{search}")
        devEmbed = discord.Embed()
        devEmbed.description = f"{devartfind}"
        await ctx.send(embed=devEmbed)

    async def on_error(ctx):
        await ctx.send("There seems to be an error. Please try again")


class devartuserget(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="devartuserget")
    async def on_message(ctx, search: str):
        devartuserget = da.get_users(search)
        devartget_embed = discord.Embed()
        devartget_embed.description = f"{devartuserget}"
        await ctx.send(embed=devartget_embed)


class devartsearcher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="devartsearch")
    async def on_message(message, ctx, search: str):
        devsearch = search
        devart = da.search_tags(search)
        devart_embed = discord.Embed()
        devart_embed.description = f"{devart}"
        await ctx.send(embed=devart_embed)


def setup(bot):
    bot.add_cog(devart(bot))
    bot.add_cog(devartuserget(bot))
    bot.add_cog(devartsearcher(bot))
