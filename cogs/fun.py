import discord
import datetime
import asyncio
from animec import kao
import random
import requests
import lxml
from bs4 import BeautifulSoup
from discord.ext import commands
from pycatapi import Client
import json
import aiohttp
from discord_components import *

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def waifu(self, ctx, *, user: discord.Member = None):
        c = random.randint(1, 100)
        if user:
            if int(c) >= 80:
                embed = discord.Embed(title="Waifu!", description=f"{user.mention} is {c}% Waifu!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="Damn, i think i'm in love...")
                await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="Waifu!", description=f"{user.mention} is {c}% Waifu!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="Not even desperate weebs will like you")
                await ctx.reply(embed=embed)
        else:
            if int(c) >= 80:
                embed = discord.Embed(title="Waifu!", description=f"{ctx.author.mention} is to {c}% a Waifu!",
                                      color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="Damn, i think i'm in love...")
                await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="Waifu!", description=f"{ctx.author.mention} is to {c}% a Waifu!",
                                      color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="Not even desperate weeb will like you")
                await ctx.reply(embed=embed)
    # Waifu command, fun category.
    @waifu.error
    async def waifu_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)

  
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def dummy(self, ctx, *, user: discord.Member = None):
        c = random.randint(1, 100)
        if user:
            if int(c) >= 80:
                embed = discord.Embed(title="Dummy!", description=f"{user.mention} is {c}%  Dumb!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="Ew, nerd spotted!")
                await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="Dummy!", description=f"{user.mention} is {c}%  Dumb!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="You're about as much use as a condom machine in the Vatican.")
                await ctx.reply(embed=embed)
        else:
            if int(c) >= 80:
                embed = discord.Embed(title="Dummy!", description=f"{ctx.author.mention} is {c}%  Dumb!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="Ew, nerd spotted!")
                await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="Dummy!", description=f"{ctx.author.mention} is {c}%  Dumb!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="You're about as much use as a condom machine in the Vatican.")
                await ctx.reply(embed=embed)
    # Dummy command, fun category.
    @dummy.error
    async def dummy_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)

  
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def cute(self, ctx, *, user: discord.Member = None):
        c = random.randint(1, 100)
        if user:
            if int(c) >= 80:
                embed = discord.Embed(title="Cute!", description=f"{user.mention} is {c}%  Cute uwu!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="If you were a vegetable, you’d be a cute-cumber.")
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Cute!", description=f"{user.mention} is {c}%  Cute uwu!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="Ughhh, who invited this pile of trash?")
                await ctx.send(embed=embed)
        else:
            if int(c) >= 80:
                embed = discord.Embed(title="Cute!", description=f"{ctx.author.mention} is {c}% Cute!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="If you were a vegetable, you’d be a cute-cumber.")
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Cute!", description=f"{ctx.author.mention} is {c}% Cute!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="Ughhh, who invited this pile of trash?")
                await ctx.reply(embed=embed)
    # Cute function , fun Group
    @cute.error
    async def cute_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)

  
    @commands.command(aliases=["gay"])
    @commands.bot_has_permissions(embed_links=True)
    async def howgay(self, ctx, *, user: discord.Member = None):
        c = random.randint(1, 100)
        if user:
            if int(c) >= 80:
                embed = discord.Embed(title="How Gay!", description=f"{user.mention} is {c}%  Gay!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="Run away, hide your butts!")
                await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="Dummy!", description=f"{user.mention} is {c}%  Gay!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="You are still gay.")
                await ctx.reply(embed=embed)
        else:
            if int(c) >= 80:
                embed = discord.Embed(title="How Gay!", description=f"{ctx.author.mention} is {c}%  Gay!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="Run away, hide your butts!")
                await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="How Gay!", description=f"{ctx.author.mention} is {c}%  Gay!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="You are still gay.")
                await ctx.reply(embed=embed)
    # how gay func, Fun category
    @howgay.error
    async def howgay_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)

  
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def simp(self, ctx, *, user: discord.Member = None):
        c = random.randint(1, 100)
        if user:
            if int(c) >= 50:
                embed = discord.Embed(title="Simp!", description=f"{user.mention} is {c}% Simp!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="If you're a simp, just remember, it means Suckers Idolizing Mediocre Pussy.")
                await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="Simp!", description=f"{user.mention} is {c}% Simp!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="I see you're a chad like me.")
                await ctx.reply(embed=embed)
        else:
            if int(c) >= 50:
                embed = discord.Embed(title="Simp!", description=f"{ctx.author.mention} is {c}% Simp!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="If you're a simp, just remember, it means Suckers Idolizing Mediocre Pussy.")
                await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="Simp!", description=f"{ctx.author.mention} is {c}% Simp!", color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="I see you're a chad like me.")
                await ctx.reply(embed=embed)
    # Simp command, fun category
    @simp.error
    async def simp_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)

  
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def pp(self, ctx, *, user: discord.Member = None):
        c = random.randint(1, 20)
        d = c / 2
        st = '8' + '=' * int(d) + 'D'
        if user:
            if c >= 15:
                embed = discord.Embed(title="PP!", description=f"{user.mention} has a {c} cm big pp!\n\t{st}",
                                      color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="I almost mistook it for Burj Khalifa.")
                await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="PP!", description=f"{user.mention} has a {c} cm big pp!\n\t{st}",
                                      color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="I'm gonna need my microscope to see that.")
                await ctx.reply(embed=embed)
        else:
            if c >= 15:
                embed = discord.Embed(title="PP!", description=f"{ctx.author.mention} has a {c} cm big pp!\n\t{st}",
                                      color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="I almost mistook it for Burj Khalifa.")
                await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="PP!", description=f"{ctx.author.mention} has a {c} cm big pp!\n\t{st}",
                                      color=0x71368a)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="I'm gonna need my microscope to see that.")
                await ctx.reply(embed=embed)
    @pp.error
    async def pp_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)

  
    @commands.command(aliases=["8b", "8", "8ball"])
    @commands.bot_has_permissions(embed_links=True)
    async def eightball(self, ctx, *, message):
        variable = ["Yes",
                    f"{ctx.author.mention} idk bro, you hella sus",
                    "No",
                    "Maybe",
                    "No hablo inglés",
                    "Don't count on it",
                    "Very doubtful",
                    "My sources say no",
                    "Most likely",
                    "Signs point to yes",
                    "Yes, definetly",
                    "Without a doubt",
                    "Better not tell you now",
                    "Ask again later",
                    "Concentrate and ask again"]
        c = random.choice(variable)
        embed = discord.Embed(title="8Ball", description=f"**Question:** |  {message} \n **Answer:** | {c}", color=0x71368a)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text="Magik")
        await ctx.reply(embed=embed)
    @eightball.error
    async def eightball_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)
      elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like you forgot to enter a question.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MissingRequiredArgument")
        await ctx.reply(embed=embed)

  
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def cat(self, ctx):
      c = Client()
      catto = c.get_cat()
      embed = discord.Embed(title="Meow!", description="", color=0x71368a)
      embed.set_image(url=catto)
      embed.set_footer(text=f"Issued by {ctx.author}")
      msg = await ctx.reply(embed=embed)
    @cat.error
    async def catt_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def meme(self, ctx):
      ctx.bot.session = aiohttp.ClientSession()
      meme = await ctx.bot.session.get("https://www.reddit.com/r/memes/.json")
      data = random.choice((await meme.json())["data"]["children"])["data"]
      memeembed = discord.Embed(title="Meme", description=str(data["title"]), colour=discord.Colour.random())
      print(data["url"])
      memeembed.set_image(url=data["url"])
      await ctx.send(embed=memeembed)
    @meme.error
    async def meme_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def facts(self, ctx):
      ctx.bot.session = aiohttp.ClientSession()
      meme = await ctx.bot.session.get("https://www.reddit.com/r/facts/.json")
      data = random.choice((await meme.json())["data"]["children"])["data"]
      if data['selftext'].startswith('https://') == True:
        detailsoffact = ''
      else:
        detailsoffact = data['selftext']
      embed = discord.Embed(title="Fun fact", description=f"Did you know, {str(data['title'])}\n\n{detailsoffact}", colour=discord.Colour.random())
      await ctx.send(embed=embed)
      await ctx.bot.session.close()
    @facts.error
    async def facts_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")

  
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def caught(self, ctx, user: discord.Member):
      if user is None:
        await ctx.reply("Who did you caught simping?")
      else:
        await ctx.send(user.mention)
        embed = discord.Embed(title="Simp alert!", description=f"{user.mention} has been caught simping by {ctx.author.mention}!", color=discord.Colour.purple())
        embed.set_footer(text="May god forgive your sins...")
        embed.set_thumbnail(url="https://th.bing.com/th/id/OIP.2loiaxfdldMdvDUk57bGEwHaHa?w=185&h=185&c=7&r=0&o=5&pid=1.7")
        await ctx.send(embed=embed)
    @caught.error
    async def caught_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")

  
    @commands.command(aliases=["ff"])
    @commands.bot_has_permissions(embed_links=True)
    async def funfact(self, ctx):
      a = ["As RainBoT (Head-Developer) once said, \"Otaku? More like attack u\"", "LateNight was meant to be a bot for a community server, but as it got deleted the developers decided to make it public, aaaaaand it turned out to be a good choice!", "down bad (Head-Developer) had many mental breakdowns while developing me, especially due the fact that message-intents got disabled and you need to apply for them.", "down bad is cooler than RainBoT ngl.", "LateNight will receive slash commands soon! :D", "https://i.imgur.com/9YVEldj.png", "Both developers are underage.", "LateNight exists since 25th July 2021, 1:30 PM, and the community server since ed, 13th October 2021, 03:22 PM (Which you can btw join [Here](https://discord.gg/2TXcFa57rR)", "Kiki (Server designer) is a designer for 5 different bots.", "It took LateNight around 7 months to get verified.", "The whole LateNight team is from different countries, not even everyone lives in europe!", "https://i.imgur.com/SMOQEWQ.png", "Hussain (Ex-Admin) rejoined the LateNight staff team 3 times within 2 months."]
      x = random.choice(a)
      embed = discord.Embed(title="Funfact!", description=x, color=discord.Colour.random())
      await ctx.reply(embed=embed)
    @funfact.error
    async def funfact_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")

  
    @commands.command()
    async def emojify(self, ctx, *, text = None):
      if text is None:
        await ctx.reply("You need to input a text to emojify.")
        return
      emojis = []
      for s in text.lower():
        if s.isdecimal():
          num2emo = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"} 
          emojis.append(f":{num2emo.get(s)}:")
        elif s.isalpha():
          emojis.append(f":regional_indicator_{s}:")
        else:
          emojis.append(s)
      await ctx.send("".join(emojis))



    async def web_scrape(self, text):
      async with aiohttp.ClientSession() as session:
        async with session.get(text) as r:
          status = r.status
          if status == 200:
            text = await r.text()
            return text
  
    @commands.command(aliases=["wouldyourather"])
    @commands.bot_has_permissions(embed_links=True, add_reactions=True)
    async def wyr(self, ctx):
      text = await self.web_scrape("https://either.io/")
      soup = BeautifulSoup(text, "lxml")
      l = []
      for choice in soup.find_all("span", {"class": "option-text"}):
        l.append(choice.text)
      e = discord.Embed(color=discord.Colour.random())
      e.set_author(name="Would you rather...", url="https://either.io/", icon_url=self.bot.user.avatar_url)
      e.add_field(name="Either...", value=f":regional_indicator_a: {l[0]}", inline=False)
      e.add_field(name="Or...", value=f":regional_indicator_a: {l[1]}", inline=False)
      msg = await ctx.reply(embed=e)
      await msg.add_reaction("1️⃣")
      await msg.add_reaction("2️⃣")
    @wyr.error
    async def wyr_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` and `add_reactions` permissions.")


    @commands.command()
    async def count(self, ctx):
      r1 = random.randint(1, 5)
      await self.start_counting(ctx.author)
      users = await self.get_counting_data()
      users[str(ctx.author.id)]["count"] += r1
      with open("json_files/count.json", "w") as f:
        json.dump(users, f)
      count = users[str(ctx.author.id)]["count"]
      await ctx.send(f"+{str(r1)}! Your new counter is {count}")

    @commands.command()
    async def kao(self, ctx):
      kaomojis = kao(5)
      await ctx.reply(" \n".join(kaomojis))
  
    @commands.command(aliases = ["clb"])
    @commands.bot_has_permissions(embed_links=True)
    async def countingleaderboard(self, ctx, x=5):
      users = await self.get_counting_data()
      leader_board = {}
      total = []
      for user in users:
        name = int(user)
        count = users[user]["count"]
        leader_board[count] = name
        total.append(count)
      total = sorted(total,reverse=True) 
      x = int(x)
      embed = discord.Embed(title = f"Top {x} people who should touch grass!" , description="Top counting players!", color=discord.Colour.purple())
      index = 1
      for amt in total:
          id_ = leader_board[amt]
          member = self.bot.get_user(id_)
          name = member
          embed.add_field(name = f"{index}. {name}" , value = f"{amt:,}",  inline = False)
          if index == x:
              break
          else:
              index += 1
      await ctx.send(embed=embed)
    @countingleaderboard.error
    async def countingleaderboard_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      

    async def start_counting(self, user):
      users = await self.get_counting_data()
      if str(user.id) in users:
        return False
      else:
        users[str(user.id)] = {}
        users[str(user.id)]["count"] = 0
      with open("json_files/count.json", "w") as f:
        json.dump(users, f)
      return True
      
    async def get_counting_data(self):
      with open("json_files/count.json") as f:
        users = json.load(f)
      return users

    async def update_count(self, user, change=0, mode="count"):
      users=await self.get_counting_data()
      users[str(user.id)][mode] += change
      with open("json_files/count.json", "w") as f:
        json.dump(users, f)
      count = [users[str(user.id)]]
      return count


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def insult(self, ctx, user: discord.Member = None):
      response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
      if response.status_code == 200:
        if user is None:
          embeda = discord.Embed(title=f"Yo {ctx.author.name}", description=response.json()["insult"], color=discord.Colour.random())
          await ctx.reply(embed=embeda)
        elif user:
          embedu = discord.Embed(title=f"Yo {user.name}", description=response.json()["insult"], color=discord.Colour.random())
          await ctx.reply(embed=embedu)
      else:
        await ctx.reply("Something went wrong. Please DM a developer.")
        print("Something went wrong!\n\n")
        print(response.status_code)
    @insult.error
    async def insult_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(fun(bot))