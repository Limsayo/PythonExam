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

###############################################

@bot.event
async def on_ready():
    
    await bot.load_extension('cogs.quizz')
    await bot.load_extension('cogs.scoreboard')
    await bot.tree.sync()
    print("bot lancé")
  

bot.run(os.getenv('DISCORD_TOKEN'))

#cette commande ne se lance pas sauf erreur fatale
print(" OUPS PROBLEME ")
