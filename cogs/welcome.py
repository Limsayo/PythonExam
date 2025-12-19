import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!" , intents=intents)


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1450077605180080148)
    embed = discord.Embed(title='', description='')
    embed.set_image(url="attachment://sphinx.jpg")  # Add image to embed
    await member.send("SPHINX WELCOMES YOU!", embed=embed, files=[discord.File("ressources/sphinx.jpg", filename="sphinx.jpg")])

####################################################  