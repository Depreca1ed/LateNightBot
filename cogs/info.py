import discord
import datetime
import random
import os
import animec
import time
import asyncio
import psutil
import humanize
from discord_components import *
from discord.ext import commands
load_time = datetime.datetime.utcnow()
n = datetime.datetime.utcnow().timestamp()

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.process = psutil.Process(os.getpid())


    @commands.command(aliases=["botinfos"])
    @commands.bot_has_permissions(embed_links=True)
    async def botinfo(self, ctx):
      o = random.randrange(0, 999)
      m = str(0)
      x = load_time - datetime.datetime.utcnow()
      y = humanize.precisedelta(x, minimum_unit="seconds")
      ramUsage = self.process.memory_full_info().rss / 1024**2
      embed = discord.Embed(title="Botinfos!", description=f"""
              **Ping** 🏓\nThe bots ping is {(round(self.bot.latency * 1000))}ms!\n\n**Uptime** 📡\nThe bots uptime is {y} / <t:{round(n)}:R> / <t:{round(n)}>\n\n**Servers** 🖥️\n{str(len(self.bot.guilds))}\n
**Ram usage** 🧬
{ramUsage:.2f} MB
              """, color=0x71368a)
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_footer(text="haha botinfos go brrrr")
      msg = await ctx.reply(embed=embed, components=[Select(
        placeholder="Select something",
        options=[
          SelectOption(label="Team", value="1", description="Get infos about the LateNight Development/Server Team!"),
          SelectOption(label="Infos", value="2", description="Get infos about the bot!"),
          SelectOption(label="Misc", value="3", description="Get infos about non-category stuff")],
          custom_id=m)])
      while True:
        try:
          msg = await self.bot.wait_for("select_option", check=lambda
          inter: inter.custom_id == m and inter.user == ctx.author, timeout=15.0)
          res = msg.values[0]
          if res == "1":
              eembed = discord.Embed(title="**LateNight Team!**", description="**Head-Devs:**\n`down bad#8487`, `Deprecated#8292`\n**Admins:**\n`zimin#1777`\n**Server Designer**\n`KikiLovesYa uwu#7252`", color=discord.Colour.random())
              eembed.timestamp = datetime.datetime.utcnow()
              eembed.set_footer(text="haha botinfos go brrrr")
              await msg.edit_origin(embed=eembed)
          elif res == "2":
              embed1 = discord.Embed(title="Botinfos!", description=f"""
              **Ping** 🏓\nThe bots ping is {(round(self.bot.latency * 1000))}ms!\n\n**Uptime** 📡\nThe bots uptime is {y} / <t:{round(n)}:R> / <t:{round(n)}>\n\n**Servers** 🖥️\n{str(len(self.bot.guilds))}\n
**Ram usage** 🧬
{ramUsage:.2f} MB
              """, color=discord.Colour.random())
              embed1.timestamp = datetime.datetime.utcnow()
              embed1.set_footer(text="haha botinfos go brrrr")
              await msg.edit_origin(embed=embed1)
          elif res == "3":
              embed2 = discord.Embed(title="Misc!", description=f"**Commands 📂** \nThe bot has {len(ctx.bot.commands)} commands\n\n**Users 📢\n** The bot is visible to {len(list(map(str, [p.id for p in ctx.bot.users])))} users", color=discord.Colour.random()) 
              embed2.timestamp = datetime.datetime.utcnow()
              embed2.set_footer(text="haha botinfos go brrrr")
              await msg.edit_origin(embed=embed2)
        except discord.errors.HTTPException:
          pass
        except asyncio.TimeoutError:
          pass
    @botinfo.error
    async def botinfo_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` and `external_emojis` permission.")

  
    @commands.command(aliases=["ei", "ej", "einfo"])
    @commands.bot_has_permissions(embed_links=True, external_emojis=True)
    async def emojiinfo(self, ctx, emoji: discord.Emoji = None):
      if emoji is None:
        await ctx.reply("Please input the emoji that you want to get information about.")
        return
      try:
            emoji = await emoji.guild.fetch_emoji(emoji.id)
      except discord.NotFound:
            await ctx.reply("I could not find this emoji in the given guild.")
      is_managed = "Yes" if emoji.managed else "No"
      is_animated = "Yes" if emoji.animated else "No"
      requires_colons = "Yes" if emoji.require_colons else "No"
      creation_time = emoji.created_at.strftime("%I:%M %p %B %d, %Y")
      can_use_emoji = "Everyone" if not emoji.roles else " ".join(role.name for role in emoji.roles)

      description = f"""
**__General:__**
**Name:** {emoji.name}
**ID:** {emoji.id}
**URL:** [Link to emoji]({emoji.url})
**Author:** {emoji.user.mention}
**Time Created:** {creation_time}
**Usable by:** {can_use_emoji}

**__Other:__**
**Animated:** {is_animated}
**Managed:** {is_managed}
**Requires colons:** {requires_colons}
**Guild Name:** {emoji.guild.name}
**Guild ID:** {emoji.guild.id}
        """
      embed = discord.Embed(title=f"**Emoji information for** `{emoji.name}`", description=description, color=0x71368a)
      embed.set_thumbnail(url=emoji.url)
      await ctx.reply(embed=embed)
    @emojiinfo.error
    async def emojiinfo_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` and `external_emojis` permission.")
      elif isinstance(error, commands.EmojiNotFound):
        eeembed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the emoji wasn't found*\nMake sure to only use custom emojis.", color=discord.Colour.dark_red())
        eeembed.set_footer(text="commands.EmojiNotFound")
        await ctx.reply(embed=eeembed)


    @commands.command(aliases=["userinfo", "ui"])
    @commands.bot_has_permissions(embed_links=True)
    async def whois(self, ctx, user: discord.Member = None):
      if user is None:
        foundere = "<:LateNightFounder:966355172102115420>"
        deve = """
<:LateNightDeveloper:966356003320918107>
        """
        votere = "<a:6_LN_tickyellow:951619262798262382>"
        buge = "<:LateNightBugHunter:966356933839835156>"
        desginere = "<:1_LN_zerotwopeace:901462836071522334>"
        admine = "<:LateNightAdministration:966350801012416632>"
        zimin = ctx.author.id == 802551341963673650
        lean = ctx.author.id == 703671503954378782
        kiki = ctx.author.id == 317708760535793686
        rainbot = ctx.author.id == 688293803613880334
        zulk = ctx.author.id == 892327232398319656
        vron = ctx.author.id == 879574308266070016
        tth = ctx.author.id == 749172471290134579
        ts  = ctx.author.created_at.timestamp()
        tsj = ctx.author.joined_at.timestamp()
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in ctx.author.guild_permissions if p[1]])
        voice_state = None if not ctx.author.voice else ctx.author.voice.channel
        embed = discord.Embed(title="Userinfo!", description=f"""
**Select something from the dropdown menu to see infos about yourself!**
        """, color=discord.Colour.random())
        embed.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
        embed.set_footer(text=ctx.guild.name)
        embed.timestamp = datetime.datetime.utcnow()
        a = random.randrange(1, 10000)
        b = ["a", "b", "c", "d", "f", "g"]
        c = random.choice(b)
        d = str(a)+c
        userinfo1 = await ctx.reply(embed=embed, components=[Select(placeholder="Select something", options=[SelectOption(label="General info", value="1", description="Get general information about yourself!"), SelectOption(label="Guild member informations", value="2", description="Get infos about yourself according to this guild!"), SelectOption(label="Permissions", value="3", description="Get infos about your permissions!")], custom_id=f"{d}")])
        while True:
          try:
            userinfo1 = await self.bot.wait_for("select_option", check=lambda inter: inter.custom_id == f"{d}" and inter.user == ctx.author)
            res1 = userinfo1.values[0]
            if res1 == "1":
              embed1 = discord.Embed(title="", description=f"""
**User Nickname** - {ctx.author.nick}
**User ID** - {ctx.author.id}
**Link to Avatar** - [Here]({ctx.author.avatar_url})
**Status** - {str(ctx.author.status).title()}
**Activity** - {ctx.author.activity}
**Account age** - <t:{round(ts)}:R>
              """, color=discord.Colour.random())
              embed1.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
              embed1.set_footer(text=ctx.guild.name)
              embed1.set_thumbnail(url=ctx.author.avatar_url)
              embed1.timestamp = datetime.datetime.utcnow()
              if rainbot:
                embed1.add_field(name="**Special acknowledgements**", value=f"<:LateNightDeveloper:966356003320918107> - LateNight Head-Developer")
              elif lean:
                embed1.add_field(name="Special acknowledgements", value=f"{foundere} - LateNight Server Founder\n<:LateNightDeveloper:966356003320918107> - LateNight Head-Developer")
              elif zulk:
                embed1.add_field(name="Special acknowledgements", value=f"{foundere} - LateNight Server Founder")
              elif vron:
                embed1.add_field(name="Special acknowledgements", value=f"{votere} - LateNight Top Voter")
              elif tth:
                embed1.add_field(name="Special acknowledgements", value=f"{buge} - LateNight Bug Hunter")
              elif kiki:
                embed1.add_field(name="Special acknowledgements", value=f"{desginere} - LateNight Server Designer")
              elif zimin:
                embed1.add_field(name="Special acknowledgements", value=f"{admine} - LateNight Administrator")
              await userinfo1.edit_origin(embed=embed1)
            elif res1 == "2":
              embed2 = discord.Embed(title="", description=f"""
**Highest Role** - {ctx.author.top_role.mention}
**Roles** - {len(ctx.author.roles)}
**In voice channel** - {voice_state}
**Joined server** - <t:{round(tsj)}:R>
**Join position** - {str(members.index(ctx.author)+1)}
              """, color=discord.Colour.random())
              embed2.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
              embed2.set_footer(text=ctx.guild.name)
              embed2.set_thumbnail(url=ctx.author.avatar_url)
              embed2.timestamp = datetime.datetime.utcnow()
              await userinfo1.edit_origin(embed=embed2)
            elif res1 == "3":
              embed1 = discord.Embed(title="asd3", description="asd3", color=discord.Colour.random())
              await userinfo1.send(f"**Every permission that you have:**\n\n`{perm_string}`")
          except discord.errors.HTTPException:
            pass

      elif user:
        foundere = "<:LateNightFounder:966355172102115420>"
        deve = "<:LateNightDeveloper:966356003320918107>"
        votere = "<a:6_LN_tickyellow:951619262798262382>"
        buge = "<:LateNightBugHunter:966356933839835156>"
        desginere = "<:1_LN_zerotwopeace:901462836071522334>"
        admin = "<:LateNightAdministration:966350801012416632>"
        zimin = user.id == 802551341963673650
        kiki = user.id == 317708760535793686
        lean = user.id == 703671503954378782
        rainbot = user.id == 688293803613880334
        zulk = user.id == 892327232398319656
        vron = user.id == 879574308266070016
        tth = user.id == 749172471290134579
        ts  = user.created_at.timestamp()
        tsj = user.joined_at.timestamp()
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        voice_state = None if not user.voice else user.voice.channel
        embed = discord.Embed(title="Userinfo!", description=f"""
**Select something from the dropdown menu to see infos about the mentioned member!**
        """, color=discord.Colour.random())
        embed.set_author(name=f"{user}", icon_url=f"{user.avatar_url}")
        embed.set_footer(text=ctx.guild.name)
        embed.timestamp = datetime.datetime.utcnow()
        a = random.randrange(1, 10000)
        b = ["a", "b", "c", "d", "f", "g"]
        c = random.choice(b)
        d = str(a)+c
        userinfo2 = await ctx.reply(embed=embed, components=[Select(placeholder="Select something", options=[SelectOption(label="General info", value="1", description="Get general informations about this user!"), SelectOption(label="User guild infos", value="2", description="Get informations about this user according to this guild!"), SelectOption(label="Permissions", value="3", description="Get infos about this users permissions!")], custom_id=f"{d}")])
        while True:
          try:
            userinfo2 = await self.bot.wait_for("select_option", check=lambda inter: inter.custom_id == f"{d}" and inter.user == ctx.author)
            res1 = userinfo2.values[0]
            if res1 == "1":
              embed1 = discord.Embed(title="", description=f"""
**User Nickname** - {user.nick}
**User ID** - {user.id}
**Link to Avatar** - [Here]({user.avatar_url})
**Status** - {str(user.status).title()}
**Activity** - {user.activity}
**Account age** - <t:{round(ts)}:R>
              """, color=discord.Colour.random())
              embed1.set_author(name=f"{user}", icon_url=f"{user.avatar_url}")
              embed1.set_footer(text=ctx.guild.name)
              embed1.set_thumbnail(url=user.avatar_url)
              embed1.timestamp = datetime.datetime.utcnow()
              if rainbot:
                embed1.add_field(name="Special acknowledgements", value=f"{deve} - LateNight Head-Developer")
              elif lean:
                embed1.add_field(name="Special acknowledgements", value=f"{foundere} - LateNight Server Founder\n{deve} - LateNight Head-Developer")
              elif zulk:
                embed1.add_field(name="Special acknowledgements", value=f"{foundere} - LateNight Server Founder")
              elif vron:
                embed1.add_field(name="Special acknowledgements", value=f"{votere} - LateNight Top Voter")
              elif tth:
                embed1.add_field(name="Special acknowledgements", value=f"{buge} - LateNight Bug Hunter")
              elif kiki:
                embed1.add_field(name="Special acknowledgements", value=f"{desginere} - LateNight Server Designer")
              elif zimin:
                embed1.add_field(name="Special acknowledgements", value=f"{admin} - LateNight Administrator")
              await userinfo2.edit_origin(embed=embed1)
            elif res1 == "2":
              embed2 = discord.Embed(title="", description=f"""
**Highest Role** - {user.top_role.mention}
**Roles** - {len(user.roles)}
**In voice channel** - {voice_state}
**Joined server** - <t:{round(tsj)}:R>
**Join position** - {str(members.index(user)+1)}
              """, color=discord.Colour.random())
              embed2.set_author(name=f"{user}", icon_url=f"{user.avatar_url}")
              embed2.set_footer(text=ctx.guild.name)
              embed2.set_thumbnail(url=user.avatar_url)
              embed2.timestamp = datetime.datetime.utcnow()
              await userinfo2.edit_origin(embed=embed2)
            elif res1 == "3":
              embed1 = discord.Embed(title="asd3", description="asd3", color=discord.Colour.random())
              await userinfo2.send(f"**Every permission that the mentioned user has:**\n\n`{perm_string}`")
          except discord.errors.HTTPException:
            pass
    @whois.error
    async def whois_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)
            
  
    @commands.command(aliases=["si", "sv"])
    @commands.bot_has_permissions(embed_links=True)
    async def serverinfo(self, ctx):
        emoji_count = len(ctx.guild.emojis)
        online = 0
        for i in ctx.guild.members:
          if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
            online += 1
        created_at = ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
        bot = 0
        human = 0
        for member in ctx.guild.members:
          if member.bot:
            bot=bot+1
          else:
            human = human+1
        a = random.randrange(1, 10000)
        b = ["a", "b", "c", "d", "f", "g"]
        c = random.choice(b)
        d = str(a)+c      
        gembed = discord.Embed(title="Server information", description="**Choose a category from the dropdown menu, to see specific information about this server.**", color=discord.Colour.random())
        gembed.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
        gembed.set_footer(text=ctx.guild.name)
        gembed.timestamp = datetime.datetime.utcnow()
        serverinfo1 = await ctx.reply(embed=gembed, components=[Select(placeholder="Select something", options=[SelectOption(label="General server information", value="1", description="Get general information about this server."), SelectOption(label="Premium information", value="2", description="Get information about the premium status of this server.")], custom_id=d)])
        while True:
            serverinfo1 = await self.bot.wait_for("select_option", check=lambda inter: inter.custom_id == f"{d}" and inter.user == ctx.author)
            res1 = serverinfo1.values[0]
            if res1 == "1":
              sembed = discord.Embed(title=f"General information about {ctx.guild.name}!", color=discord.Colour.random())
              sembed.set_thumbnail(url=f"{ctx.guild.icon_url}")
              sembed.set_author(name=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon_url}")
              sembed.add_field(name="Server Owner", value=f"{str(ctx.guild.owner)} / {ctx.guild.owner.id}", inline=False)
              sembed.add_field(name="Total Channels", value=f"Voice Channels: {len(ctx.guild.voice_channels)} / Text Channels: {len(ctx.guild.text_channels)} / Categories: {len(ctx.guild.categories)}", inline=False)
              sembed.add_field(name="Total Members", value=f"Humans: {human} / Bots: {bot}", inline=False)
              sembed.add_field(name="Banned Users", value=len(str(ctx.guild.bans)))
              sembed.add_field(name="Verification Level", value=f"{str(ctx.guild.verification_level).title()}", inline=False)
              sembed.add_field(name="Emojis", value=f"Emoji Limit: {ctx.guild.emoji_limit} / Total Emojis: " + ', '.join(str(e) for e in ctx.guild.emojis[:3]) + f" +{len(ctx.guild.emojis)-3}", inline=False)
              sembed.add_field(name="Created at", value=f"<t:{round(ctx.guild.created_at.timestamp())}> / <t:{round(ctx.guild.created_at.timestamp())}:R>", inline=False)
              await serverinfo1.edit_origin(embed=sembed)
            elif res1 == "2":
              s2embed = discord.Embed(title=f"Premium infos about {ctx.guild.name}", color=discord.Colour.random())
              s2embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
              s2embed.set_author(name=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon_url}")
              s2embed.add_field(name="Server Boosters", value=f"{ctx.guild.premium_subscription_count}", inline=False)
              s2embed.add_field(name="Server Level", value=f"{ctx.guild.name} is on level {ctx.guild.premium_tier}.", inline=False)
              try:
                s2embed.add_field(name="Booster role", value=f"<@&{(ctx.guild.premium_subscriber_role.id)}>", inline=False)
              except:
                s2embed.add_field(name="Booster role", value="No booster role on this server", inline=False)
              emptys = "<:StartEmpty:966364615753732116>"
              emptym = "<:MiddleEmpty:966364941768622100>"
              emptye = "<:EndEmpty:966365284917211186>"
              fulls = "<:StartFull:966365680565903480>"
              fullm = "<:MiddleFull:966365696617484319>"
              fulle = "<:EndFull:966365710924251186>"
              x = ctx.guild.premium_subscription_count
              if x == 0:
                s2embed.add_field(name="Server Boosts", value=f"{emptys}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptye} (0/2)", inline=False)
              elif x == 1:
                s2embed.add_field(name="Server Boosts", value=f"{fulls}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptye} (1/2)", inline=False)
              elif x == 2:
                s2embed.add_field(name="Server Boosts", value=f"{fulls}{fullm}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptye} (2/2)", inline=False)
              elif x == 3:
                s2embed.add_field(name="Server Boosts", value=f"{fulls}{fullm}{fullm}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptye} (3/7)", inline=False)
              elif x == 4:
                s2embed.add_field(name="Server Boosts", value=f"{fulls}{fullm}{fullm}{fullm}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptye} (4/7)", inline=False)
              elif x == 5:
                s2embed.add_field(name="Server Boosts", value=f"{fulls}{fullm}{fullm}{fullm}{fullm}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptye} (5/7)", inline=False)
              elif x == 6:
                s2embed.add_field(name="Server Boosts", value=f"{fulls}{fullm}{fullm}{fullm}{fullm}{fullm}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptye} (6/7)", inline=False)
              elif x == 7:
                s2embed.add_field(name="Server Boosts", value=f"{fulls}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{emptym}{emptym}{emptym}{emptym}{emptym}{emptym}{emptye} (7/7)", inline=False)
              elif x == 8:
                s2embed.add_field(name="Server Boosts", value=f"{fulls}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{emptym}{emptym}{emptym}{emptym}{emptym}{emptye} (8/14)", inline=False)
              elif x == 9:
                s2embed.add_field(name="Server Boosts", value=f"{fulls}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{emptym}{emptym}{emptym}{emptym}{emptye} (9/14)", inline=False)
              elif x == 10:
                s2embed.add_field(name="Server Boosts", value=f"{fulls}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{emptym}{emptym}{emptym}{emptye} (10/14)", inline=False)
              elif x == 11:
                s2embed.add_field(name="Server Boosts", value=f"{fulls}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{emptym}{emptym}{emptye} (11/14)", inline=False)
              elif x == 12:
                s2embed.add_field(name="Server Boosts", value=f"{fulls}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{emptym}{emptye} (12/14)", inline=False)
              elif x == 13:
                s2embed.add_field(name="Server Boosts", value=f"{fulls}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{emptye} (13/14)", inline=False)
              elif x == 14:
                s2embed.add_field(name="Server Boosts", value=f"{fulls}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fulle} (14/14)", inline=False)
              else:
                s2embed.add_field(name="Server Boosts", value=f"{fulls}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fullm}{fulle} ({x})", inline=False)
              await serverinfo1.edit_origin(embed=s2embed)
    @serverinfo.error
    async def serverinfo_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")

  
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def anime(self, ctx, *, query = None):
      async with ctx.typing():
        if query is None:
          await ctx.reply("You need to input an anime to search for!")
          return
        try:
            anime = animec.Anime(query)
        except:
            embederror = discord.Embed(title="Error!", description="No corresponding Anime is found for the search query!", color=0xFF0000)
            await ctx.reply(embed=embederror)
            return
        async with ctx.typing():
          embedanime = discord.Embed(title=f"ENG Name: {anime.title_english} / Japanese Name: {anime.title_jp} / Alt Names: {anime.alt_titles}", url=anime.url, description=f"{anime.description[:300]}[...]({anime.url})", color=0x71368a)
          animeprod = ", ".join(anime.producers)
          embedanime.add_field(name="Producers", value=f"{animeprod[:50]}[...]({anime.url})")
          embedanime.add_field(name="Broadcast", value=str(anime.broadcast))
          embedanime.add_field(name="Rating", value=str(anime.rating))
          embedanime.add_field(name="Status", value=str(anime.status))
          embedanime.add_field(name="Genres", value=", ".join(anime.genres))
          embedanime.add_field(name="Top Anime List", value=str(anime.popularity))
          embedanime.add_field(name="Type", value=str(anime.type))
          embedanime.add_field(name="NSFW Status", value=str(anime.is_nsfw()))
          embedanime.add_field(name="Episodes", value= str(anime.episodes))
          embedanime.set_thumbnail(url=anime.poster)
          animerec = ", ".join(anime.recommend())
          embedanime.set_footer(text=f"Similar animes: {animerec[:50]}...")
          if str(anime.is_nsfw()) == "True":
            if ctx.channel.is_nsfw() == True:
              await ctx.reply(embed=embedanime)
            elif ctx.channel.is_nsfw() != True:
              embedee = discord.Embed(title="Error!", description="Due the fact that this command is marked as NSFW, you need to use this command in an NSFW channel. If you don't know how you're able to make a channel available for NSFW commands/set the channel to NSFW, click [Here](https://www.minitool.com/news/nsfw-discord.html) to see a tutorial for it.", color=discord.Colour.dark_red())
              await ctx.reply(embed=embedee)
          else:
            embedanime.set_thumbnail(url=anime.poster)
            await ctx.reply(embed=embedanime)
            pass
    @anime.error
    async def anime_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


    @commands.command(alises=["aw", "awaifu", "animew"])
    @commands.bot_has_permissions(embed_links=True)
    async def animewaifu(self, ctx, *, query = None):
        if query is None:
          await ctx.reply("You need to input a waifu to search for!")
          return
        try:
            char = animec.Charsearch(query)
        except:
            embederror = discord.Embed(title="Error!", description="No corresponding Anime Character is found for the search query!", color=0xFF0000)
            await ctx.reply(embed=embederror)
            return
        embedchar = discord.Embed(title=char.title, url=char.url, color=0x71368a)
        embedchar.set_image(url=char.image_url)
        embedchar.set_footer(text=f", ".join(list(char.references.keys())[:2]))
        await ctx.reply(embed=embedchar)
    @animewaifu.error
    async def animewaifu_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")

  
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def animenews(self, ctx, amount:int=5):
      async with ctx.typing():
          news = animec.Aninews(amount)
          links = news.links
          titles = news.titles
          descriptions = news.description
          embed = discord.Embed(title="Latest Anime News", color=0x71368a)
          embed.set_thumbnail(url=news.images[0])
          for i in range(amount):
              embed.add_field(name=f"{i+1}) {titles[i]}", value=f"{descriptions[i][:100]}...\n[Read more]({links[i]})", inline=False)
          await ctx.reply(embed=embed)
    @animenews.error
    async def animenews_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


    @commands.command(aliases=["ri"])
    @commands.bot_has_permissions(embed_links=True)
    async def roleinfo(self, ctx, role: discord.Role = None):
      x = random.randint(0, 999)
      m = str(x)
      if role is None:
        await ctx.reply("Mention an existing role!")
        return
      perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in role.permissions if p[1]])
      embedm = discord.Embed(title=f"Role Infos", color=role.color)
      embedm.add_field(name="Role Name / ID", value=f"<@&{role.id}> / {role.id}", inline=False)
      embedm.add_field(name="Role Created At", value=f"<t:{round(role.created_at.timestamp())}> / <t:{round(role.created_at.timestamp())}:R>", inline=False)
      embedm.add_field(name="Role Members", value=len(role.members), inline=False)
      embedm.add_field(name="Role Position", value=role.position, inline=False)
      embedm.add_field(name="Hexa Color", value=f"{str(role.color)}")
      embedm.set_thumbnail(url=ctx.guild.icon_url)
      msg = await ctx.reply(embed=embedm, components=[Select(
        placeholder="Select something",
        options=[
          SelectOption(label="Infos", value="1", description="Get infos about the mentioned role!"),
          SelectOption(label="Values", value="2", description="Get the values about the mentioned role!"),
          SelectOption(label="Permissions", value="3", description="Get the permissions about the mentioned role!")],
          custom_id=m)])
      while True:
        try:
          msg = await self.bot.wait_for("select_option", check=lambda inter: inter.custom_id == m and inter.user == ctx.author, timeout=30.0)
          res = msg.values[0]
          if res == "1":
            await msg.edit_origin(embed=embedm)
          if res == "2":
            embedv = discord.Embed(title="Role Values", color=role.color)
            embedv.add_field(name="Role Mentionable by everyone?", value=role.mentionable, inline=False)
            embedv.add_field(name="Displayed from others?", value=f"{role.hoist}", inline=False)
            embedv.add_field(name="Nitro Role", value=role.is_premium_subscriber(), inline=False)
            embedv.add_field(name="Bot Role", value=role.is_bot_managed(), inline=False)
            embedv.set_thumbnail(url=ctx.guild.icon_url)
            await msg.edit_origin(embed=embedv)
          if res == "3":
            embedp = discord.Embed(title="Role Permissions", description=perm_string, color=role.color)
            await msg.send(embed=embedp)
        except asyncio.TimeoutError:
          pass
    @roleinfo.error
    async def roleinfo_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.RoleNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the role wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.RoleNotFound")
        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(info(bot))