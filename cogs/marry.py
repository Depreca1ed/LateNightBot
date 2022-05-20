import datetime
import discord
import json
from discord.ext import commands
import asyncio
from discord_components import *

class marry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def marry(self, ctx, user: discord.Member = None):
      if user is None:
        await ctx.reply("You need to mention the user that you want to marry!")
        return
      await self.open_account(ctx.author)
      await self.open_account(user)
      users = await self.get_profile_data()
      a = users[str(ctx.author)]["Married"]
      b = users[str(user)]["Married"]
      if a == "True":
        await ctx.reply("You can't betray your partner! smh")
      elif b == "True":
        await ctx.reply("The mentioned user already has a partner!")
      elif user.mention == ctx.author.mention:
        await ctx.reply("You can't marry yourself!")
      else:
        embed = discord.Embed(title="Proposing", description=f"Hey {user.mention}! {ctx.author.mention} wants to marry you, will you accept them as your Husband/Wife?", color=discord.Colour.green())
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        msg = await ctx.reply(embed=embed, components=[[Button(style=ButtonStyle.green, label="Accept"), Button(style=ButtonStyle.red, label="Deny")]])
        while True:
          try:
            res = await self.bot.wait_for("button_click", check=lambda inter: inter.user == user, timeout=15.0)
            if res.component.label == "Accept":
              x = datetime.datetime.utcnow().timestamp()
              embedy = discord.Embed(title="Successfully proposed!", description=f"Congratulations! {ctx.author.mention} & {user.mention} are now officially married since <t:{round(x)}:R>", color=discord.Colour.green())
              embedy.set_thumbnail(url=ctx.guild.icon_url)
              embedy.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
              await msg.edit(embed=embedy, components=[[Button(style=ButtonStyle.green, label="Accept", disabled=True), Button(style=ButtonStyle.red, label="Deny", disabled=True)]])
              await res.respond(type=6)
              x = datetime.datetime.utcnow().timestamp()
              y = round(x)
              users[str(ctx.author)]["Married"] = "True"
              users[str(user)]["TStamp"] = y
              users[str(ctx.author)]["TStamp"] = y
              users[str(user)]["Married"] = "True"
              users[str(ctx.author)]["Partner"] = str(user)
              users[str(user)]["Partner"] = str(ctx.author)
              users[str(user)]["Guild"] = str(ctx.guild.name)
              users[str(ctx.author)]["Guild"] = str(ctx.guild.name)
              with open("json_files/marriage.json", "w") as f:
                json.dump(users, f)
              break
            elif res.component.label =="Deny":
              x = datetime.datetime.utcnow().timestamp()
              embedn = discord.Embed(title="Failed proposing!", description=f"I'm sorry to say this {ctx.author.mention}, but sadly {user.mention} declined you as their partner.", color=discord.Colour.red())
              embedn.set_thumbnail(url=ctx.guild.icon_url)
              embedn.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
              await msg.edit(embed=embedn, components=[[Button(style=ButtonStyle.green, label="Accept", disabled=True), Button(style=ButtonStyle.red, label="Deny", disabled=True)]])
              await res.respond(type=6)
              break
          except asyncio.TimeoutError:
              embedt = discord.Embed(title="Failed proposing!", description="Your partner took to long to respond. The interaction has been timeouted.", color=discord.Colour.red())
              embedt.set_thumbnail(url=ctx.guild.icon_url)
              embedt.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
              await msg.edit(embed=embedt, components=[[Button(style=ButtonStyle.green, label="Accept", disabled=True), Button(style=ButtonStyle.red, label="Deny", disabled=True)]])
              break
    @marry.error
    async def marry_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def status(self, ctx, user: discord.Member = None):
        if user is None:
          await self.open_account(ctx.author)
          users = await self.get_profile_data()
          a = users[str(ctx.author)]["Married"]
          b = users[str(ctx.author)]["TStamp"]
          c = users[str(ctx.author)]["Partner"]
          d = users[str(ctx.author)]["Guild"]
          if b == 0:
            embed1 = discord.Embed(title="", description=f"**{ctx.author} isn't married yet.**", color=discord.Colour.random())
            embed1.set_thumbnail(url=ctx.author.avatar_url)
            embed1.set_author(name="Relationship status", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed1)
          else:
            embed2 = discord.Embed(title="", description=f"__Marriage status is {a}.__\n**Current relationship between {ctx.author} and {c} goes since <t:{b}> / <t:{b}:R>.** \n`They both married in the guild {d}`", color=discord.Colour.random())
            embed2.set_thumbnail(url=ctx.author.avatar_url)
            embed2.set_author(name="Relationship status", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed2)
        else:
          await self.open_account(user)
          users = await self.get_profile_data()
          a = users[str(user)]["Married"]
          b = users[str(user)]["TStamp"]
          c = users[str(user)]["Partner"]
          d = users[str(user)]["Guild"]
          if b == 0:
            embed1 = discord.Embed(title="", description=f"**{user} isn't married yet.**", color=discord.Colour.random())
            embed1.set_thumbnail(url=user.avatar_url)
            embed1.set_author(name="Relationship status", icon_url=user.avatar_url)
            await ctx.send(embed=embed1)
          else:
            embed2 = discord.Embed(title="", description=f"__Marriage status is {a}.__\n**Current relationship between {user} and {c} goes since <t:{b}> / <t:{b}:R>.** \n`They both married in the guild {d}`", color=discord.Colour.random())
            embed2.set_thumbnail(url=user.avatar_url)
            embed2.set_author(name="Relationship status", icon_url=user.avatar_url)
            await ctx.send(embed=embed2)
    @status.error
    async def status_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def divorce(self, ctx):
      await self.open_account(ctx.author)
      users = await self.get_profile_data()
      a = users[str(ctx.author)]["Married"]
      b = users[str(ctx.author)]["TStamp"]
      c = users[str(ctx.author)]["Partner"]
      d = users[str(ctx.author)]["Guild"]
      if a == "False":
        await ctx.reply("You're not married!")
      if a == "True":
        embed = discord.Embed(title="Oh oh!", description=f"{ctx.author.mention} do you really want to divorce {c}? I bet they won't be happy about this...", color=discord.Colour.red())
        embed.set_footer(text="Think twice!", icon_url=ctx.author.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.reply(embed=embed, components=[[Button(style=ButtonStyle.green, label="Yes"), Button(style=ButtonStyle.red, label="No")]])
        while True:
          try:
            res = await self.bot.wait_for("button_click", check=lambda inter: inter.user == ctx.author, timeout=15.0)
            if res.component.label == "No":
              await ctx.reply("Good choice...")
              await res.respond(type=6)
              break
            elif res.component.label == "Yes":
              await ctx.reply(f"You have divorced {c}!")
              await res.respond(type=6)
              users[str(ctx.author)]["Married"] = "False"
              users[str(c)]["TStamp"] = 0
              users[str(ctx.author)]["TStamp"] = 0
              users[str(c)]["Married"] = "False"
              users[str(ctx.author)]["Partner"] = ""
              users[str(c)]["Partner"] = ""
              users[str(c)]["Guild"] = ""
              users[str(ctx.author)]["Guild"] = ""
              with open("json_files/marriage.json", "w") as f:
                json.dump(users, f)        
              break
          except asyncio.TimeoutError:
            await ctx.reply("The message has timeouted.")  
    @divorce.error
    async def divorce_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
            
      
    async def open_account(self, user):
      users = await self.get_profile_data()
      if str(user) in users:
        return False
      else:
        users[str(user)] = {}
        users[str(user)]["Married"] = "False"
        users[str(user)]["Partner"] = "None"
        users[str(user)]["Guild"] = "None"
        users[str(user)]["TStamp"] = 0
      with open("json_files/marriage.json", "w") as f:
        json.dump(users, f)
      return True
  
    async def get_profile_data(self):
      with open("json_files/marriage.json", "r") as f:
        users = json.load(f)
      return users

def setup(bot):
    bot.add_cog(marry(bot))