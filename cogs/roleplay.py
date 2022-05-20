import animec
import discord
from discord.ext import commands

class roleplay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def slap(self, ctx, user: discord.Member=None):
        if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="Get slapped!", description=f"{ctx.author.mention} just slapped {user.mention}!", color=0x71368a)
            embed.set_image(url=waifu.slap())
            await ctx.reply(embed=embed)
        else:
          await ctx.reply("You need to mention a user to slap!")
    @slap.error
    async def slap_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def kiss(self, ctx, user: discord.Member=None):
        if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="Kissing!", description=f"{ctx.author.mention} just kissed {user.mention}!",color=0x71368a)
            embed.set_image(url=waifu.kiss())
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("You need to mention someone to kiss!")
    @kiss.error
    async def kiss_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def bonk(self, ctx, user: discord.Member = None):
        if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="Get bonked!", description=f"{ctx.author.mention} just bonked {user.mention}! **BONK**", color=0x71368a)
            embed.set_image(url=waifu.bonk())
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("You need to mention someone to bonk!")
    @bonk.error
    async def bonk_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def cuddle(self, ctx, user: discord.Member = None):
      if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="Awww!", description=f"{ctx.author.mention} is cuddling with {user.mention}", color=0x71368a)
            embed.set_image(url=waifu.cuddle())
            await ctx.reply(embed=embed)
      else:
            await ctx.reply("You need to mention someone to cuddle with!")
    @cuddle.error
    async def cuddle_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)

  
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def bully(self, ctx, user: discord.Member = None):
      if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="Get bullied nerd!", description=f"{ctx.author.mention} is bullying {user.mention}", color=0x71368a)
            embed.set_image(url=waifu.bully())
            await ctx.reply(embed=embed)
      else:
            await ctx.reply("You need to mention someone to bully!")
    @bully.error
    async def bully_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def cry(self, ctx):
      waifu = animec.waifu.Waifu
      embed = discord.Embed(title="Waaaaaaa", description=f"{ctx.author.mention} just started sobbing, how sad", color=0x71368a)
      embed.set_image(url=waifu.cry())
      await ctx.reply(embed=embed)
    @cry.error
    async def cry_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")

  
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def hug(self, ctx, user: discord.Member = None):
      if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="How sweet!", description=f"{ctx.author.mention} just hugged {user.mention}!", color=0x71368a)
            embed.set_image(url=waifu.hug())
            await ctx.reply(embed=embed)
      else:
            await ctx.reply("You need to mention someone to hug!")
    @hug.error
    async def hug_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)

  
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def lick(self, ctx, user: discord.Member = None):
      if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="Lick, mhh", description=f"{ctx.author.mention} just licked {user.mention}! *Tasty*", color=0x71368a)
            embed.set_image(url=waifu.lick())
            await ctx.reply(embed=embed)
      else:
            await ctx.reply("You need to mention someone to lick!")
    @lick.error
    async def lick_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)

  
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def pat(self, ctx, user: discord.Member = None):
      if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="Pat, pat!", description=f"{ctx.author.mention} pats {user.mention}!", color=0x71368a)
            embed.set_image(url=waifu.pat())
            await ctx.reply(embed=embed)
      else:
            await ctx.reply("You need to mention someone to pat!")
    @pat.error
    async def pat_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def smug(self, ctx, user: discord.Member = None):
      if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="Smug!", description=f"{ctx.author.mention} smugs at {user.mention}!", color=0x71368a)
            embed.set_image(url=waifu.smug())
            await ctx.reply(embed=embed)
      else:
            await ctx.reply("You need to mention someone to smug to!")
    @smug.error
    async def smug_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def yeet(self, ctx, user: discord.Member = None):
      if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="Yeet!", description=f"{ctx.author.mention} yeets {user.mention}! **YEET**", color=0x71368a)
            embed.set_image(url=waifu.yeet())
            await ctx.reply(embed=embed)
      else:
            await ctx.reply("You need to mention someone to yeet!")
    @yeet.error
    async def yeet_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def blush(self, ctx):
      waifu = animec.waifu.Waifu
      embed = discord.Embed(title="Hm....", description=f"{ctx.author.mention} started to blush.... *What did you do?!*", color=0x71368a)
      embed.set_image(url=waifu.blush())
      await ctx.reply(embed=embed)
    @blush.error
    async def blush_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def highfive(self, ctx, user: discord.Member = None):
      if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="Gimme a highfive!", description=f"{ctx.author.mention} gives {user.mention} a highfive! **Wooo**", color=0x71368a)
            embed.set_image(url=waifu.highfive())
            await ctx.reply(embed=embed)
      else:
            await ctx.reply("You need to mention someone to give a highfive to!")
    @highfive.error
    async def highfive_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)



    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def bite(self, ctx, user: discord.Member = None):
      if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="Ouchie!", description=f"{ctx.author.mention} bites {user.mention}! *You should be careful about what you say*", color=0x71368a)
            embed.set_image(url=waifu.bite())
            await ctx.reply(embed=embed)
      else:
            await ctx.reply("You need to mention someone to bite!")
    @bite.error
    async def bite_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)



    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def glomp(self, ctx, user: discord.Member = None):
      if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="Glomp!", description=f"{ctx.author.mention} glomps {user.mention}!", color=0x71368a)
            embed.set_image(url=waifu.glomp())
            await ctx.reply(embed=embed)
      else:
            await ctx.reply("You need to mention someone to glomp!")
    @glomp.error
    async def glomp_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)



    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def kill(self, ctx, user: discord.Member = None):
      if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="Looks like someone got murder on their mind.", description=f"{ctx.author.mention} kills {user.mention}!", color=0x71368a)
            embed.set_image(url=waifu.kill())
            await ctx.reply(embed=embed)
      else:
            await ctx.reply("You need to mention someone to kill!")
    @kill.error
    async def kill_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def happy(self, ctx):
      waifu = animec.waifu.Waifu
      embed = discord.Embed(title="Woo, happy!", description=f"Looks like {ctx.author.mention} is really happy!", color=0x71368a)
      embed.set_image(url=waifu.happy())
      await ctx.reply(embed=embed)
    @happy.error
    async def happy_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")



    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def wink(self, ctx, user: discord.Member = None):
      if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="Looks like you got someone in your eye...", description=f"{ctx.author.mention} winks at {user.mention}!", color=0x71368a)
            embed.set_image(url=waifu.wink())
            await ctx.reply(embed=embed)
      else:
            await ctx.reply("You need to mention someone to wink to!")
    @wink.error
    async def wink_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def poke(self, ctx, user: discord.Member = None):
      if user:
            waifu = animec.waifu.Waifu
            embed = discord.Embed(title="Looks like you're provocating!", description=f"{ctx.author.mention} pokes {user.mention}!", color=0x71368a)
            embed.set_image(url=waifu.poke())
            await ctx.reply(embed=embed)
      else:
            await ctx.reply("You need to mention someone to poke!")
    @poke.error
    async def poke_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")
      elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Error has been issued!", description=f"```{error}```\n*Looks like the member wasn't found.*", 
        color=discord.Colour.dark_red())
        embed.set_footer(text="commands.MemberNotFound")
        await ctx.reply(embed=embed)


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def dance(self, ctx):
      waifu = animec.waifu.Waifu
      embed = discord.Embed(title="Woo, dance with me!", description=f"Looks like {ctx.author.mention} is having fun!", color=0x71368a)
      embed.set_image(url=waifu.dance())
      await ctx.reply(embed=embed)
    @dance.error
    async def dance_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def cringe(self, ctx):
      waifu = animec.waifu.Waifu
      embed = discord.Embed(title="That was cringe.", description=f"{ctx.author.mention} is having a cringe attack.", color=0x71368a)
      embed.set_image(url=str(waifu.cringe()))
      await ctx.reply(embed=embed)
    @cringe.error
    async def cringe_error(self, ctx, error):
      if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.reply("I'm missing permissions. Make sure that I have the `embed_links` permission.")


def setup(bot):
    bot.add_cog(roleplay(bot))