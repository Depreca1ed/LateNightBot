# Copyright (C) 2022-2023 LateNight Development

# This file is part of the LateNight project.

# The LateNight project can not be copied and/or distributed without the express
# permission of the LateNight Development team. 
import discord
import datetime
import os
import random
import asyncio
import contextlib
import io
import textwrap
import re
import keep_alive
import json
import asyncio
from discord_components import *
from discord.ext import commands

intents = discord.Intents.all()
bot = ComponentsBot(["n!", "N!", "Æ!", "(ง'̀-'́)ง"], case_insensitive=True, intents=intents, strip_after_prefix=True)
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
bot.load_extension("jishaku")
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True" 
os.environ["JISHAKU_HIDE"] = "True"
bot.reload_extension("jishaku")
bot.remove_command("help")
token = os.environ["TOKEN"]


@bot.listen("on_connect")
async def ch_pr():
    await bot.wait_until_ready()
    statuses = ["My prefix is: n! | LateNight", "I'm in " + str(len(bot.guilds)) +
        " servers. Wow, so many people think that this bot is cool!",
        "It's late already, you should go sleep."]
    while not bot.is_closed():
      status = random.choice(statuses)
      await bot.change_presence(activity=discord.Game(name=status))
      await asyncio.sleep(20)
bot.loop.create_task(ch_pr())


@bot.command(pass_context=True)
async def loadcog(ctx, cog):
    if ctx.author.id == 703671503954378782:
        emoji = "<:3_LN_tick:901466423837196288>"
        bot.load_extension(f"cogs.{cog}")
        await ctx.message.add_reaction(emoji)
    elif ctx.author.id == 688293803613880334:
        emoji = "<:3_LN_tick:901466423837196288>"
        bot.load_extension(f"cogs.{cog}")
        await ctx.message.add_reaction(emoji)
    else:
        pass

@bot.command(pass_context=True)
async def unloadcog(ctx, cog):
    if ctx.author.id == 703671503954378782:
        emoji = "<:3_LN_tick:901466423837196288>"
        bot.unload_extension(f"cogs.{cog}")
        await ctx.message.add_reaction(emoji)
    elif ctx.author.id == 688293803613880334:
        emoji = "<:3_LN_tick:901466423837196288>"
        bot.unload_extension(f"cogs.{cog}")
        await ctx.message.add_reaction(emoji)
    else:
        pass

@bot.command(pass_context=True)
async def reloadcog(ctx, cog):
    if ctx.author.id == 703671503954378782:
        emoji = "<:3_LN_tick:901466423837196288>"
        bot.reload_extension(f"cogs.{cog}")
        await ctx.message.add_reaction(emoji)
    elif ctx.author.id == 688293803613880334:
        emoji = "<:3_LN_tick:901466423837196288>"
        bot.reload_extension(f"cogs.{cog}")
        await ctx.message.add_reaction(emoji)
    else:
        pass

@bot.command(pass_context=True)
async def reloadbot(ctx, cog):
  if ctx.author.id == 703671503954378782:
    emoji = "<:3_LN_tick:901466423837196288>"
    for filename in os.listdir("./cogs"):
      if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
    await ctx.message.add_reaction(emoji)
  elif ctx.author.id == 688293803613880334:
    emoji = "<:3_LN_tick:901466423837196288>"
    for filename in os.listdir(".py"):
      if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
    await ctx.message.add_reaction(emoji)
  else:
    pass

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


try:
    keep_alive.keep_alive()
    bot.run(os.getenv("TOKEN"))
except:
    os.system("kill 1")
    keep_alive.keep_alive()
    bot.run(os.getenv("TOKEN"))