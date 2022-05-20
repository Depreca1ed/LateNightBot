import discord
import datetime
import os
import random
import asyncio
import contextlib
import json
from discord_components import *
from discord.ext import commands

update = "`n!kao has been added!`"

funembed = discord.Embed(title="Fun", description="""
`n!countingleaderboard`: Get the top users who counted.
`n!eightball (question)`: Rolls the eightball to give you answers to your question
`n!funfact`: Get a random funfact!
`n!emojify (text)`: Emojify a specific text!
`n!howgay [user]`: Shows someone's gayness!
`n!caught (user)`: Caught anyone simping?
`n!insult [user]`: Insult someone, *or yourself*
`n!facts`: Get a random fact!
`n!waifu [user]` Shows someone's waifu-ness!
`n!dummy [user]`: Shows someone's dumbness!
`n!count`: Count!
`n!cute [user]`: Shows someone's cuteness!
`n!simp [user]`: Shows how big of a simp someone is!
`n!meme`: Get a random meme!
`n!cat`: Shows random cute cat images!
`n!wyr`: Would you rather...
`n!kao`: Get 5 random kao emojis!
""", color=discord.Colour.random())

utilityembed = discord.Embed(title="Utility", description="""
`n!wikipedia (entry)`: Get a wikipedia entry for a specific object.
`n!support`: Link to the support server
`n!invite`: To invite the bot to your server
`n!help`: Shows this message
`n!vote`: Vote for the bot!
`n!gif (gif)`: Shows a gif from the specific search term.
`n!av [user]`: Shows the avatar of the user`
""", color=discord.Colour.random())

infoembed = discord.Embed(title="Info", description="""
`n!serverinfo`: Shows information about the server
`n!animewaifu (waifu)`: Shows information about your cute waifu
`n!emojiinfo (emoji)`: Get information about an emoji (must be server emoji)
`n!animenews`: Shows some thicc anime news
`n!roleinfo (user)`: Shows information about the mentioned role
`n!userinfo [user]`: Shows information about the user
`n!botinfo`: Shows information about LateNight
`n!anime (anime)`: Shows information about the anime
""", color=discord.Colour.random())

roleplayembed = discord.Embed(title="Roleplay", description="""
`n!highfive (user)`: Give someone a highfive!
`n!cuddle (user)`: Cuddle with someone!
`n!bully (user)`: Bully someone!
`n!glomp (user)`: Glomp someone!
`n!slap (user)`: Slap someone!
`n!kiss (user)`: Kiss someone!
`n!bonk (user)`: Bonk someone!
`n!lick (user)` Lick someone!
`n!smug (user)` Smug at someone!
`n!yeet (user)`: Yeet someone!
`n!bite (user)`: Bite someone!
`n!kill (user)`: Kill someone!
`n!wink (user)`: Wink at someone!
`n!poke (user)`: Poke someone!
`n!hug (user)`: Hug someone!
`n!pat (user)`: Pat someone!
`n!cringe`: Welp, that was cringe.
`n!dance`: Sometimes you just gotta do a dance, don't you think?
`n!happy`: Wooo! Being happy is nice.
`n!blush`: Did something embarassing just happen?
`n!cry`: Sometimes you just need to let it out.
""", color=discord.Colour.random())

gamesembed = discord.Embed(title="Games", description="""
`n!math`: Do some math!
`n!rps`: Play a round of Rock, Paper, Scissors!
`n!gtn`: Play a round of guess the number!
""", color=discord.Colour.random())

moderationembed = discord.Embed(title="Moderation", description="""
`n!softban (user)`: Softban a user from the server.
`n!purge (amount)`: Purge a certain amount of messages.
`n!ban (user)`: Ban a user from the server.
""", color=discord.Colour.random())

economyembed = discord.Embed(title="Economy", description="""
`n!economyleaderboard`: See the economy leaderboard.
`n!withdraw (amount)`: Withdraw money.
`n!deposit (amount)`: Deposit money.
`n!search`: Search somewhere for money.
`n!daily`: Claim your daily coins.
`n!give` (user)`: Give someone money.
`n!work`: Work to earn money.
`n!rob` (user)`: Rob someone.
`n!bal` [user]`: See your balance.
`n!beg`: Beg for money.
""", color=discord.Colour.random())

marryembed = discord.Embed(title="Marriage", description="""
`n!divorce`: Divorce yourself with your aprtner
`n!status [user]`: See the status of yourself/a user
`n!marry (user)`: Marry a user. 
""", color=discord.Colour.random())

with open("cogs/economy.py", "r") as f:
      data = f.readlines()  
with open("cogs/fun.py", "r") as f:
      data2 = f.readlines()  
with open("cogs/games.py", "r") as f:
      data3 = f.readlines()  
with open("cogs/info.py", "r") as f:
      data4 = f.readlines()  
with open("cogs/moderation.py", "r") as f:
      data5 = f.readlines()  
with open("cogs/roleplay.py", "r") as f:
      data6 = f.readlines()  
with open("cogs/utility.py", "r") as f:
      data7 = f.readlines()  
with open("main.py") as f:
      data8 = f.readlines()
with open("cogs/marry.py", "r") as f:
      data9 = f.readlines()
with open("cogs/test.py", "r") as f:
      data10 = f.readlines()
with open("./main.py", "r") as f:
      data11 = f.readlines()
with open("cogs/events.py", "r") as f:
      data12 = f.readlines()
lines = data + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def help(self, ctx):
      await self.selectboxtesting(ctx)
    @help.error
    async def help_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")

  
    async def selectboxtesting(self, ctx):
      funemoji = self.bot.get_emoji(901462836071522334)
      utilityemoji = self.bot.get_emoji(901462836696481863)
      infoemoji = self.bot.get_emoji(901462839250800641)
      rpemoji = self.bot.get_emoji(899817086950461480)
      gamesemoji = self.bot.get_emoji(901462842430079016)
      modemoji = self.bot.get_emoji(967796438677487616)
      ecmoji = self.bot.get_emoji(967798992652083261)
      memoji = self.bot.get_emoji(967803312781025380)
      embed = discord.Embed(title="Help panel!", description=f"""
```css\n() -> means the argument is required
[] -> means the argument is optional```
                            
**Prefix**: n!
**Number of commands**: {len(self.bot.commands)}
**Number of servers**: {len(ctx.bot.guilds)}
**Lines of code**: {len(lines)}
                            
**Choose an option in the dropdown menu, to see all commands.**

**[Vote for the support server](https://top.gg/servers/897866866557603890/vote)**
**[Vote for me](https://top.gg/bot/868817426937184306/vote)**
                            
**New update -** {update}            
""", color=0x71368a)
      embed.set_thumbnail(url=self.bot.user.avatar_url)
      interaction1 = await ctx.reply(embed=embed,
        components=[[
            Select(
                placeholder="Select something",
                options=[
                    SelectOption(
                        label="Fun",
                        value="1",
                        description="Get all commands according to \"Fun\"", emoji=funemoji),
                    SelectOption(
                        label="Utility",
                        value="2",
                        description="Get all commands according to \"Utility\"", emoji=utilityemoji),
                    SelectOption(
                        label="Info",
                        value="3",
                        description="Get all commands according to \"Info\"", emoji=infoemoji),
                    SelectOption(
                        label="Roleplay",
                        value="4",
                        description="Get all commands according to \"Roleplay\"", emoji=rpemoji),
                    SelectOption(
                        label="Games",
                        value="5",
                        description="Get all commands according to \"Game\"", emoji=gamesemoji),
                    SelectOption(
                        label="Moderation",
                        value="6",
                        description="Get all commands according to \"Moderation\"", emoji=modemoji),
                    SelectOption(
                        label="Economy",
                        value="7",
                        description="Get all commands according to \"Economy\"", emoji=ecmoji),
                    SelectOption(
                       label="Marriage",
                        value="8",
                        description="Get all commands according to \"Marriage\"", emoji=memoji),
                ],
                custom_id="selectboxtesting")
        ], ActionRow(Button(style=ButtonStyle.URL, label="Invite Bot", url=f"https://discord.com/api/oauth2/authorize?client_id={ctx.bot.user.id}&permissions=8&scope=bot"), Button(style=ButtonStyle.URL, label="Support Server", url="https://discord.gg/XsmSy5emwt"))])
      while True:
        try:
            interaction2 = await self.bot.wait_for("select_option",check=lambda inter: inter.custom_id == "selectboxtesting", timeout=30.0)
            res = interaction2.values[0]
            if res == "1":
                await interaction2.send(embed=funembed)
            elif res == "2":
                await interaction2.send(embed=utilityembed)
            elif res == "3":
                await interaction2.send(embed=infoembed)
            elif res == "4":
                await interaction2.send(embed=roleplayembed)
            elif res == "5":
                await interaction2.send(embed=gamesembed)
            elif res == "6":
                await interaction2.send(embed=moderationembed)
            elif res == "7":
              await interaction2.send(embed=economyembed)
            elif res == "8":
              await interaction2.send(embed=marryembed)
            else:
              pass
        except discord.errors.HTTPException:
          pass
        except asyncio.TimeoutError:
          embedfail = discord.Embed(title="Help panel!", description=f"```css\n() -> means the argument is required\n[] -> means the argument is optional```\n\n**Prefix: n!\nNumber of commands: {len(self.bot.commands)}\nNumber of servers: {len(ctx.bot.guilds)}**\n**Lines of code: {len(lines)}**\n\nChoose an option in the dropdown menu, to see all commands.\n\n**[Support Server](https://discord.gg/vv6CxyBwCC)**\n**[Invite the bot](https://discord.com/api/oauth2/authorize?client_id={ctx.bot.user.id}&permissions=8&scope=bot)**\n**[Vote for me](https://top.gg/bot/868817426937184306/vote)**\n**[Vote for the support server](https://top.gg/servers/897866866557603890/vote)**\n\n**New update -** {update}", color=0x71368a)
          embedfail.set_thumbnail(url=self.bot.user.avatar_url)
          await interaction1.edit(embed=embedfail, components=[[Button(style=ButtonStyle.red, label="Time's up! ⏰", disabled=True)]])
          break


def setup(bot):
    bot.add_cog(help(bot))