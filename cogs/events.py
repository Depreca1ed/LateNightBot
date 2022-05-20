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
from discord_components import *
from discord.ext import commands


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready.")
        DiscordComponents(self.bot)
  

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
          pass
        elif isinstance(error, commands.MissingPermissions):
          pass
        elif isinstance(error, commands.MemberNotFound):
          pass
        elif isinstance(error, commands.EmojiNotFound):
          pass
        elif isinstance(error, commands.MissingRequiredArgument):
          pass
        elif isinstance(error, commands.NSFWChannelRequired):
            pass
        elif isinstance(error, commands.RoleNotFound):
          pass
        elif isinstance(error, commands.ChannelNotFound):
          pass
        elif isinstance(error, commands.CommandOnCooldown):
            pass
        elif isinstance(error, commands.NotOwner):
          embedowner = discord.Embed(description="This command is reserved for the owners of the bot.", color=discord.Colour.dark_red())
          await ctx.reply(embed=embedowner)
        elif isinstance(error, commands.CommandNotFound):
            await ctx.reply("*Command not found! Use `n!help` for every command*", delete_after=4.0)
        elif isinstance(error, commands.CommandError):
            embedarg = discord.Embed(title="Unexpected Error!", description=f"**How to fix this error?**\nYou cannot fix the error as it has something to do with the code, the developers will be notified about the bug now. I suggest not using the command again as the same response will be recieved.", colour=discord.Colour.dark_red())
            await ctx.send(embed=embedarg)
          
            bugreport = await ctx.bot.fetch_channel(941749075408212039)
            errembed = discord.Embed(title="Error", description=f"**Error**:\n```\n{error}```\n\n**Command**: {ctx.command}\n**Guild**: {ctx.guild.name}\n**User**: {ctx.author} / {ctx.author.id}\n**Error on**: <t:{round((datetime.datetime.utcnow().timestamp()))}>")
            try:
              invitec = self.bot.get_channel(ctx.channel.id)
              invitel = await invitec.create_invite(uses=5)
              errembed.add_field(name="Invite link", value=invitel)
            except:
              errembed.add_field(name="Invite link", value="Wasn't able to create an invite due to missing permissions!")
            await bugreport.send("<@&937060684225736805>", embed=errembed)
            print(f"\n\nError in Bot below:\n\n")
            raise error


    @commands.Cog.listener()
    async def on_message(self, message):
      if message.channel.id == 940614519498100767:
        channel = self.bot.get_channel(940614519498100767)
        data = message.content.split(" ")
        user = re.sub("\D", '', data[0])
        user_object = self.bot.get_user(str(user)) or await self.bot.fetch_user(str(user))
        user = user_object
        await self.open_account(user)
        users = await self.get_bank_data()
        try:
          emoji = "<a:LN_latenightcoin:943274431923486740>"
          embed = discord.Embed(title="Rewards!", description=f"10,000 {emoji}", color=discord.Colour.random())
          await user.send("Thank you for your vote, here are your rewards!", embed=embed)
          print(f"gave {user} 10k")
          users[str(user.id)]["wallet"] += 10000
          with open("json_files/economy.json", "w") as f:
              json.dump(users, f)
          print(f"gave {user} 10k")
          channel2 = self.bot.get_channel(958439062233034842)
          await channel2.send(f"{user} has voted for LateNight!")
        except:
          emoji = "<a:LN_latenightcoin:943274431923486740>"
          rewembed = discord.Embed(title="Rewards!", description=f"10,000 {emoji}", color=discord.Colour.random())
          await channel.send(f"I wasn't able to DM {user} / {user} but they still got the rewards.\n", embed=rewembed)
          users[str(user.id)]["wallet"] += 10000
          with open("json_files/economy.json", "w") as f:
              json.dump(users, f)
          print(f"gave {user} 10k")
          channel2 = self.bot.get_channel(958439062233034842)
          await channel2.send(f"{user} has voted for LateNight!")
      elif message.content == self.bot.user.mention:
        embed=discord.Embed(title="Hello!", description=f"Hi there {message.author}, for more information please use `n!help`!", colour=discord.Colour.random())
        embed.set_footer(text="If this didn't help you, make sure to contact a developer!")
        await message.channel.send(embed=embed)
        return


    async def open_account(self, user):
      users = await self.get_bank_data()
      if str(user.id) in users:
        return False
      else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
      with open("json_files/economy.json", "w") as f:
        json.dump(users, f)
      return True
    
    async def get_bank_data(self):
      with open("json_files/economy.json", "r") as f:
        users = json.load(f)
      return users


def setup(bot):
    bot.add_cog(events(bot))