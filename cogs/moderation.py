import discord
from discord.ext import commands
from discord import app_commands
"""
Un cog est une classe pour ranger des evenements et commandes d'une catégorie ex: modération

"""
ADMINISTRATOR_ROLE_ID = 1450105413595828317

class ModerationCog(commands.Cog):
    
    def __init__(self,bot):
        self.bot= bot

    @app_commands.command(name='ciao', description='Expulse un membre du server')
    @app_commands.checks.has_role(ADMINISTRATOR_ROLE_ID)
    async def ciao_command(self, interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(title="dégagement" )    
        embed.add_field(name='message', value='Degagement en cours')
        embed.set_image(url="https://media.tenor.com/images/514999795ee0021dc2a60c2110077ce2/tenor.gif")

        await member.send("Dégage !")
        await member.kick()
        await interaction.response.send_message(embed=embed)

    #on s'assure que l'erreur est bien due a l'absence de perimission
    @ciao_command.error
    async def ciao_error(self, interaction: discord.Interaction, error):
        if isinstance(error, app_commands.errors.MissingRole):
            await interaction.response.send_message("Vous n'avez pas les droits !")  


    @commands.Cog.listener()
    async def on_message(self, message):
        #verifier que l'auteur du message n'est pas le bot pour qu'il ne se reponde pas a l'infini
        if message.author == self.bot.user:
            return 
        #verifier la présence d'un mot dans un message le .lower met le message en minuscule pour eviter de bypass en jouant sur la case
        if 'zizi' in message.content.lower():
            await message.channel.send("On dit pas ces choses la ici")

    @app_commands.command(name='adios', description='Expulse un membre du server')
    @app_commands.checks.has_role(ADMINISTRATOR_ROLE_ID)
    async def adios_command(self, interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(title="dégagement" )    
        embed.add_field(name='message', value='Exil en cours')
        embed.set_image(url="https://media.tenor.com/images/514999795ee0021dc2a60c2110077ce2/tenor.gif")

        await member.send("BEGONE !")
        await member.ban()
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name='hola', description='Expulse un membre du server')
    @app_commands.checks.has_role(ADMINISTRATOR_ROLE_ID)
    async def hola_command(self, interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(title="Rappatriement en cours" )    
        embed.add_field(name='message', value='HO HO HO')
        embed.set_image(url="https://tenor.com/view/dr-evil-mike-myers-austin-powers-hug-come-here-gif-6096007716994172871")

        await member.send("Welcome back friend !")
        await member.unban()
        await interaction.response.send_message(embed=embed)

    


async def setup(bot: commands.Bot):
    await bot.add_cog(ModerationCog(bot))

