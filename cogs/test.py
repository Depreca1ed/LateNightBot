import discord
import requests
import json
import random
import datetime
import giphy_client
from animec import kao
from discord.ext import commands
from discord_components import *
from aiohttp import request
from giphy_client.rest import ApiException
from PIL import Image
from io import BytesIO

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    
      

def setup(bot):
    bot.add_cog(test(bot))