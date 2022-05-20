import discord
import datetime
import asyncio
import random
from discord.ext import commands
import time
import humanize
from discord_components import *

class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def gtn(self, ctx):
      channel = ctx.message.channel
      embeddif = discord.Embed(title="Choose your difficulty!", description="**Green / Easy** - Guess a number from 1-25 in 10 seconds.\n**Blue / Medium** - Guess a number from 1-50 in 20 seconds.\n**Red / Hard** - Guess a number from 1-100 in 30 seconds.", color=discord.Colour.purple())
      msg = await ctx.reply(embed=embeddif, components=[[Button(style=ButtonStyle.green, label="Easy"), Button(style=ButtonStyle.blue, label="Medium"), Button(style=ButtonStyle.red, label="Hard")]])
      res = await self.bot.wait_for("button_click")
      if res.component.label == "Easy":
        await res.respond(type=6)
        number1 = random.randint(1,25)
        embed = discord.Embed(title="Guess the Number!", description="The number is between 1-25!\nYou have 10 seconds to guess.\nDifficulty = `Easy`", color=discord.Colour.green())
        await msg.edit(embed=embed, components=[[Button(style=ButtonStyle.green, label="Good luck!", disabled=True)]])
        print(number1)
        number2 = str(number1)
        def check(m):
          return m.content == number2 and m.channel == channel
        try:
          msg = await ctx.bot.wait_for('message', check=check,timeout=10.0)
        except asyncio.TimeoutError:
          await ctx.reply(f"Time's up! The correct answer was {number1}.")
          pass
        except discord.errors.HTTPException:
          pass
        else:
          await ctx.send(f"{msg.author.mention} got the correct answer! The number was {number2}")
      elif res.component.label == "Medium":
        await res.respond(type=6)
        number1 = random.randint(1,50)
        embed = discord.Embed(title="Guess the Number!", description="The number is between 1-50!\nYou have 20 seconds to guess.\nDifficulty = `Medium`", color=discord.Colour.blue())
        await msg.edit(embed=embed, components=[[Button(style=ButtonStyle.blue, label="Good luck!", disabled=True)]])
        print(number1)
        number2 = str(number1)
        def check(m):
          return m.content == number2 and m.channel == channel
        try:
          msg = await ctx.bot.wait_for('message', check=check,timeout=20.0)
        except asyncio.TimeoutError:
          await ctx.reply(f"Time's up! The correct answer was {number1}.")
          pass
        except discord.errors.HTTPException:
          pass
        else:
          await ctx.send(f"{msg.author.mention} got the correct answer! The number was {number2}")
      elif res.component.label == "Hard":
        await res.respond(type=6)
        number1 = random.randint(1,100)
        embed = discord.Embed(title="Guess the Number!", description="The number is between 1-100!\nYou have 30 seconds to guess.\nDifficulty = `Hard`", color=discord.Colour.red())
        await msg.edit(embed=embed, components=[[Button(style=ButtonStyle.red, label="Good luck!", disabled=True)]])
        print(number1)
        number2 = str(number1)
        def check(m):
          return m.content == number2 and m.channel == channel
        try:
          msg = await ctx.bot.wait_for('message', check=check,timeout=30.0)
        except asyncio.TimeoutError:
          await ctx.reply(f"Time's up! The correct answer was {number1}.")
          pass
        except discord.errors.HTTPException:
          pass
        else:
          await ctx.send(f"{msg.author.mention} got the correct answer! The number was {number2}")
    @gtn.error
    async def gtn_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


    @commands.command(aliases=['rps'])
    @commands.bot_has_permissions(embed_links=True)
    async def rockpaperscissors(self, ctx, user: discord.Member = None):
        embed = discord.Embed(title="Rock Paper Scissors:", description=f"Choose between `rock`, `paper` and `scissors`.", colour=discord.Colour.random())
        msg = await ctx.reply(embed=embed, components=[[Button(style=ButtonStyle.green, label="🪨 - Rock"), Button(style=ButtonStyle.red, label="📰 - Paper"), Button(style=ButtonStyle.blue, label="✂️ - Scissors")]])
        res = await self.bot.wait_for("button_click", timeout = 30)
        bot = random.choice(['🪨 - Rock', '📰 - Paper', '✂️ - Scissors'])
        if res.component.label == bot:
          embed = discord.Embed(title="Tie!", description=f"I choose: {bot}\nYou choose: {res.component.label}", color=discord.Colour.random())
          await msg.edit(embed=embed)
          await res.respond(type=6)
        if res.component.label == "🪨 - Rock" and bot == "📰 - Paper":
          embed = discord.Embed(title="I won", description=f"I choose: {bot}\nYou choose: {res.component.label}", color=discord.Colour.random())
          await msg.edit(embed=embed)
          await res.respond(type=6)
        if res.component.label == "📰 - Paper" and bot == "✂️ - Scissors":
          embed = discord.Embed(title="I won", description=f"I choose: {bot}\nYou choose: {res.component.label}", color=discord.Colour.random())
          await msg.edit(embed=embed)
          await res.respond(type=6)
        if res.component.label == "✂️ - Scissors" and bot == "🪨 - Rock":
          embed = discord.Embed(title="I won", description=f"I choose: {bot}\nYou choose: {res.component.label}", color=discord.Colour.random())
          await msg.edit(embed=embed)
          await res.respond(type=6)
        if res.component.label == "📰 - Paper" and bot == "🪨 - Rock":
          embed = discord.Embed(title="You won", description=f"I choose: {bot}\nYou choose: {res.component.label}", color=discord.Colour.random())
          await msg.edit(embed=embed)
          await res.respond(type=6)
        if res.component.label == "✂️ - Scissors" and bot == "📰 - Paper":
          embed = discord.Embed(title="You won", description=f"I choose: {bot}\nYou choose: {res.component.label}", color=discord.Colour.random())
          await msg.edit(embed=embed)
          await res.respond(type=6)
        if res.component.label == "🪨 - Rock" and bot == "✂️ - Scissors":
          embed = discord.Embed(title="You won", description=f"I choose: {bot}\nYou choose: {res.component.label}", color=discord.Colour.random())
          await msg.edit(embed=embed)
          await res.respond(type=6)
    @gtn.error
    async def gtn_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


def setup(bot):
  bot.add_cog(games(bot))