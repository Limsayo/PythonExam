#!/bin/python3
import random
import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import  load_dotenv
load_dotenv() 

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!" , intents=intents)
tree=bot.tree

###############################################

@bot.event
async def on_ready():
    
    await bot.load_extension('cogs.quizz')
    await bot.load_extension('cogs.scoreboard')
    await bot.tree.sync()
    print("bot lancé")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1450077605180080148)
    embed = discord.Embed(title='', description='')
    embed.set_image(url="attachment://sphinx.jpg")  # Add image to embed
    await member.send("SPHINX WELCOMES YOU!", embed=embed, files=[discord.File("ressources/sphinx.jpg", filename="sphinx.jpg")])

####################################################    

bot.run(os.getenv('DISCORD_TOKEN'))
bot.run(os.getenv('PREMIUM_ROLE_ID '))

#cette commande ne se lance pas sauf erreur fatale
print(" OUPS PROBLEME ")
