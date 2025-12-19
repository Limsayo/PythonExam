#!/bin/python3
import random
import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import  load_dotenv
load_dotenv() #dotenv marche pas sinon
################################

#donne les permissions
intents = discord.Intents.all()
#crée le bot
bot = commands.Bot(command_prefix="!" , intents=intents)
#arborescence des commandes assignées au bot
tree=bot.tree
#constantes donc en MAJ (ici click droit sur les roles pour prendre leurs id)
PREMIUM_ROLE_ID = 1450105929759592448

###############################################


#COMPORTEMENTS DU BOT SUR COMMANDE = @bot.tree -> async def
@bot.tree.command(name='sdv', description='Lien vers le site de sup de vinci')
async def sdv_command(interaction: discord.Interaction):
    await interaction.response.send_message("https://www.supdevinci.fr/")



##################################################################

#COMPORTEMENTS AUTOMATIQUES DU BOT = @bot.event -> async def
#actions du bot
@bot.event
async def on_ready():
    #fetch les fonctions/classes et autres depuis un autre fichier
    await bot.load_extension('cogs.moderation')
    await bot.load_extension('cogs.fun')
    #synchronise les commandes a l'api discord
    await bot.tree.sync()
    print("bot lancé")

@bot.event
async def on_member_join(member):
#envoie un message dans un salon spécifique (ici pour les nouveaux membres)
    channel = bot.get_channel(1450077605180080148)
    await channel.send(f"Nouveau membre : {member.mention}")
#envoie un message privé await le fait attendre qu'un nouveau membre join avant d'agire plutot que de tout le temps soliciter les servers de discord
    await member.send("Bienvenue copain !")

####################################################    

#lancement du bot TOUTES ACTIONS AVANT LANCEMENT
bot.run(os.getenv('DISCORD_TOKEN'))

#cette commande ne se lance donc pas sauf erreur fatale
print(" tu as fait caca ")
