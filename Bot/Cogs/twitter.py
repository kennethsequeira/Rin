import discord
from discord.ext import commands
from discord import Embed
from dotenv import load_dotenv
import tweepy
import os
import pytest
load_dotenv()

# Access the Twitter API via Tweepy
Twitter_API_Key = os.getenv("Twitter_API_Key")
API_Secret_Key = os.getenv("API_Secret_Key")
Access_Token = os.getenv("Access_Token")
Access_Token_Secret = os.getenv("Access_Token_Secret")

auth = tweepy.OAuthHandler(Twitter_API_Key, API_Secret_Key)
auth.set_access_token(Access_Token, Access_Token_Secret)

api = tweepy.API(auth)

class rintwitter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="rintwitter")
    async def rintwitter(self, ctx):
        home_timeline = api.home_timeline()
        embedVar = discord.Embed(title="Twitter Timeline")
        embedVar.description = f'{api.home_timeline()}'
        await ctx.send(embed=embedVar)
    @commands.command(name="rintsearch")
    async def rintwittersearch(self, ctx, search):
        twitter_query = api.search_tweets(search)
        twitter_embed = discord.Embed()
        twitter_embed.description = f'{twitter_query}'
        await ctx.send(embed=twitter_embed)

def setup(bot):
    bot.add_cog(rintwitter(bot))
