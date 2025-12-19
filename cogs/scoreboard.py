import discord
from discord.ext import commands
from discord import app_commands
import os
import aiofiles
import json

SCORE_FILE = os.path.join(os.path.dirname(__file__), "../ressources/score.json")

class ScoreCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def update_score(self, user_id: int):
        # Read current scores
        try:
            async with aiofiles.open(SCORE_FILE, mode='r', encoding='utf-8') as f:
                data = await f.read()
                scores = json.loads(data) if data else {}
        except FileNotFoundError:
            scores = {}
        except Exception:
            scores = {}

        # Update score
        user_id_str = str(user_id)
        scores[user_id_str] = scores.get(user_id_str, 0) + 1

        # Write back to file
        async with aiofiles.open(SCORE_FILE, mode='w', encoding='utf-8') as f:
            await f.write(json.dumps(scores, indent=4))

    @app_commands.command(name='myscore', description="Show your quiz score.")
    async def myscore_command(self, interaction: discord.Interaction):
        try:
            async with aiofiles.open(SCORE_FILE, mode='r', encoding='utf-8') as f:
                data = await f.read()
                scores = json.loads(data) if data else {}
        except Exception:
            scores = {}

        user_id_str = str(interaction.user.id)
        score = scores.get(user_id_str, 0)
        await interaction.response.send_message(f"Your score: {score}")

    @app_commands.command(name='topscore', description="Show the top quiz scores.")
    async def topscore_command(self, interaction: discord.Interaction):
        try:
            async with aiofiles.open(SCORE_FILE, mode='r', encoding='utf-8') as f:
                data = await f.read()
                scores = json.loads(data) if data else {}
        except Exception:
            scores = {}

        if not scores:
            await interaction.response.send_message("No scores yet.")
            return

        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        msg = "\n".join([f"<@{uid}>: {score}" for uid, score in sorted_scores[:10]])
        await interaction.response.send_message(f"Top scores:\n{msg}")

async def setup(bot: commands.Bot):
    await bot.add_cog(ScoreCog(bot))