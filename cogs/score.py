import discord
from discord.ext import commands
import aiofiles
import os
import json

class ScoreCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.score_file = os.path.join(os.path.dirname(__file__), "../ressources/score.json")

    async def add_point(self, user_id: int):
        # Read current scores
        try:
            async with aiofiles.open(self.score_file, mode='r', encoding='utf-8') as f:
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
        async with aiofiles.open(self.score_file, mode='w', encoding='utf-8') as f:
            await f.write(json.dumps(scores, indent=4))
async def setup(bot: commands.Bot):
    await bot.add_cog(ScoreCog(bot))