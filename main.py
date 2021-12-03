import discord
import json
from discord.ext.commands import Bot
from adventbot import Advent
from shitbot import ShitBot
from random import seed

seed()
with open('secrets.json', 'r') as f:
    secrets = json.load(f)
    global TOKEN, GUILD, sessionID
    TOKEN = secrets["TOKEN"]
    GUILD = secrets["GUILD"]
    sessionID = secrets["sessionID"]


# Set up Intents
intents = discord.Intents.all()
bot = Bot(command_prefix='!', intents=intents)
bot.add_cog(ShitBot(bot))
bot.add_cog(Advent(bot))
bot.run(TOKEN)