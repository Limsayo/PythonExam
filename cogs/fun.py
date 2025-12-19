import discord
from discord.ext import commands
from discord import app_commands
import random

class Entertainment_Cog(commands.Cog):
    def __init__(self, bot):
        self.bot= bot
    @app_commands.command(name='meme', description="voici votre meme cher maitre")
    async def meme_command(self, interaction: discord.Interaction):
        meemee = ["https://media.tenor.com/images/514999795ee0021dc2a60c2110077ce2/tenor.gif", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.tenor.com%2Fc92qA2SXFnAAAAAi%2Fpepe-ban.gif&f=1&nofb=1&ipt=3dedceac55e02f3b36056c34343d6f15921e7072d248f83220d629d19f18d498"]    
        meme_hasard = random.choice(meemee)

        embed = discord.Embed(title = 'Ceci est un meme')
        # embed.add_field(name='maymay', value="ceci est un meme jaidit")
        embed.set_image(url=meme_hasard)
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Entertainment_Cog(bot))
