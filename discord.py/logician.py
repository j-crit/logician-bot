# Serenity/Logician

import sqlite3
import random
import os
import os.path
import discord
from discord.ext import commands

ownerIds = [
    185877810760515585
]
dbName = "logic.db"
config = "logician.cfg"
startupExtensions = ["azgame","ttt","response","status","admin","mbti","pats"]
prefix = "$"
with open(config,'r') as cfg:
    token = cfg.read()[0:-1]

bot = commands.Bot(self_bot=False,command_prefix=prefix)

@bot.event
async def on_ready():
    print("Current login: ")
    print(bot.user.name)
    print(bot.user.id)
    print("Prefix: " + prefix)
    print("Owners: " + str(ownerIds))
    bot.owners = ownerIds
    bot.token = token

    bot.dbName = dbName
    print("Connecting to database...")
    bot.db = sqlite3.connect(bot.dbName)
    print("Connected!")

    for extension in startupExtensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print("extension {} not loaded: ".format(extension))
            print("{}: {}".format(type(e).__name__,e))

    print("Ready to begin!")

@bot.command()
async def echo(msg : str):
    """Echoes the given string."""
    print("Command received: echo {}".format(msg))
    await bot.say(msg)

@bot.command(pass_context = True)
async def uid(ctx):
    await bot.say(str(ctx.message.author.id))

bot.run(token)
