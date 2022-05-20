import datetime
import discord
import random
import os
import requests
import json
import asyncio
import wikipedia
from aiohttp import request
from discord.ext import commands
from discord_components import *

class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["avatar"])
    @commands.bot_has_permissions(embed_links=True)
    async def av(self, ctx, *, user: discord.Member = None):
        if user:
            png = str(user.avatar_url_as(static_format="png"))
            jpg = str(user.avatar_url_as(static_format="jpg"))
            webp = str(user.avatar_url_as(static_format="webp"))
            embed = discord.Embed(title="", description=f"Avatar of {user.mention}", color=discord.Colour.purple())
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_image(url=f"{user.avatar_url}")
            embed.set_footer(text=f"Hottie! | Issued by {ctx.author}")
            await ctx.reply(embed=embed, components=[ActionRow(Button(style=ButtonStyle.URL, url=png, label="PNG"), Button(style=ButtonStyle.URL, url=jpg, label="JPG"), Button(style=ButtonStyle.URL, url=webp, label="WEBP"))])
        else:
            png = str(ctx.author.avatar_url_as(static_format="png"))
            jpg = str(ctx.author.avatar_url_as(static_format="jpg"))
            webp = str(ctx.author.avatar_url_as(static_format="webp"))
            embed = discord.Embed(title="", description=f"Avatar of {ctx.author.mention}!", color=discord.Colour.purple())
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_image(url=f"{ctx.author.avatar_url}")
            embed.set_footer(text=f"Hottie! | Issued by {ctx.author}")
            await ctx.reply(embed=embed, components=[ActionRow(Button(style=ButtonStyle.URL, url=png, label="PNG"), Button(style=ButtonStyle.URL, url=jpg, label="JPG"), Button(style=ButtonStyle.URL, url=webp, label="WEBP"))])
    @av.error
    async def av_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)
          

    @commands.command(aliases=["inv"])
    @commands.bot_has_permissions(embed_links=True)
    async def invite(self, ctx):
        embed = discord.Embed(title="Invite me!", description="Hey! Thank you for using my bot. You can invite me through [this link!](https://discord.com/oauth2/authorize?client_id=868817426937184306&scope=bot&permissions=8)", color=discord.Colour.purple())
        embed.set_footer(text="If you need help, make sure to contact one of the developers! down bad#8487 / Karp#9652")
        await ctx.reply(embed=embed)
    @invite.error
    async def invite_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def support(self, ctx):
      embed = discord.Embed(title="Support server", description="Hey, if you have some problems with the bot, make sure to join our support server and contact a developer. [Join here](https://discord.gg/2TXcFa57rR)", color=discord.Colour.purple())
      await ctx.reply(embed=embed)
    @support.error
    async def support_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def vote(self, ctx):
      embed = discord.Embed(title="", description="📧 - [Vote for me!](https://top.gg/bot/868817426937184306/vote)\n📧 - [Vote for the support server](https://top.gg/servers/897866866557603890/vote)", color=discord.Colour.purple())
      embed.set_footer(text="You voted you hot")
      await ctx.reply(embed=embed)
    @vote.error
    async def vote_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")

    def wiki_summary(self, arg, features="lxml"):
      definition = wikipedia.summary(arg, sentences=6, chars=1000, auto_suggest=True, redirect=True)
      return definition

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def wikipedia(self, ctx):
      try:
          message_content = ctx.message.content
          search = discord.Embed(title=f"**Searching...**", description=self.wiki_summary(message_content), color=discord.Colour.random())
          await ctx.reply(embed=search)
      except:
          eembed = discord.Embed(title="Error!", description="Something went wrong while fetching the data.", color=discord.Colour.dark_red())
          await ctx.reply(embed=eembed)
    @wikipedia.error
    async def wikipedia_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def gif(self, ctx, search: str):
      tenorkey = "P3M7RP3ONY5F"
      url = f"https://g.tenor.com/v1/search?q={search}&key={tenorkey}&contentfilter=high"
      if search:
          async with request("GET", url, headers={}) as response:
            if response.status == 200:
              data = await response.json()
              content = data["results"]
              gifUrl = content[random.randint(0, len(content))]['url']
              await ctx.reply(gifUrl)
            else:
              await ctx.reply(f"API Exception. Server returned {response.status}")
      else:
            await ctx.reply("You need to input a search term.")
    @gif.error
    async def gif_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(embed_links=True, send_messages=True)
    async def embed(self, ctx, channel: discord.TextChannel = None):
      if channel is None:
        await ctx.reply("Provide a channel where you want the embed to be sent.")
      elif channel:
        x = await self.bot.fetch_channel(str(channel.id))
        embedc = discord.Embed(title="Confirmation", description=f"Do you want me to send the embed into <#{x.id}>?", embed=discord.Colour.dark_purple())
        await ctx.reply(embed=embedc, components=[ActionRow(Button(style=ButtonStyle.green, label="Confirm"), Button(style=ButtonStyle.red, label="Cancel"))])
        
    @embed.error
    async def embed_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` & the `send_messages` permissions in the mentioned channel.")
      elif isinstance(error, commands.ChannelNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the channel wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.ChannelNotFound")
        await ctx.reply(embed=embed)
      elif isinstance(error, commands.MissingPermissions):
        eeembed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like you're missing some permissions.*", color=discord.Colour.dark_red())
        eeembed.set_footer(text="commands.MissingPermissions")
        await ctx.reply(embed=eeembed)


def setup(bot):
    bot.add_cog(utility(bot))