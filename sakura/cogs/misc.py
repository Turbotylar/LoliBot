import discord
from discord.ext import commands
import datetime
import requests
import random


class Misc(commands.Cog, name="Miscellaneous"):
    """
    Commands that do not fit into their own categories.
    """

    
    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def inspire(self, ctx):
        """Get some ai generated inspiration."""
        link = "http://inspirobot.me/api?generate=true"
        f = requests.get(link)
        imgurl = f.text
        embed = discord.Embed(title=("Be Inspired!"), color=0xeb34cf)
        embed.set_image(url=imgurl)
        await ctx.send(embed=embed)
    

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.bot:
            return
        if ctx.content.startswith("wait"):
                await ctx.channel.send("Too late!")
        elif ctx.content.startswith("^"):
                await ctx.channel.send("^")
        elif ctx.content.startswith("true"):
                await ctx.channel.send("Very true")
        elif "china" in ctx.content:
                social_credit = random.randint(1,100000)
                var = ["+","-","÷","×"]
                await ctx.channel.send(f"Social credit {random.choice(var)}{social_credit}")

    
    @commands.command()
    async def ping(self, ctx):
        """Pong!"""
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')
    
    
    @commands.command()
    async def eatan(self, ctx):
        embed = discord.Embed(color=0xeb34cf)
        embed.set_image(url="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/aurora-bloom-2-jpg-1579817827.jpg")
        await ctx.send(embed=embed)
        
        
def setup(bot):
    bot.add_cog(Misc(bot))
