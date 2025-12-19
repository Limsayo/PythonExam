import discord
from discord.ext import commands
from discord import app_commands
import random
import aiofiles
import os
import json

class Quizz_Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.qna_file = os.path.join(os.path.dirname(__file__), "../ressources/qna.json")
        self.last_question = {}  # Maps user_id to (question, answer)

    async def get_random_qna(self):
        try:
            async with aiofiles.open(self.qna_file, mode='r', encoding='utf-8') as f:
                data = await f.read()
            qna_list = json.loads(data)
            if qna_list:
                qna = random.choice(qna_list)
                return qna["question"], qna["answer"]
            else:
                return None, None
        except Exception as e:
            return None, None

    @app_commands.command(name='ask', description="Ask a random mythology question!")
    async def ask_command(self, interaction: discord.Interaction):
        question, answer = await self.get_random_qna()
        if question:
            self.last_question[interaction.user.id] = (question, answer)
            embed = discord.Embed(title='Mythology Question | type /answer to respond !', description=question)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("No questions found or error reading file.")

    @app_commands.command(name='answer', description="Answer the last question asked to you.")
    @app_commands.describe(answer="Your answer to the last question")
    async def answer_command(self, interaction: discord.Interaction, answer: str):
        user_id = interaction.user.id
        if user_id not in self.last_question:
            await interaction.response.send_message("You haven't been asked a question yet. Use /ask first.")
            return
        question, correct_answer = self.last_question[user_id]
        if answer.strip().lower() == correct_answer.strip().lower():
            await interaction.response.send_message("Correct! 🎉")
        else:
            await interaction.response.send_message(f"Wrong! The correct answer was: {correct_answer}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Quizz_Cog(bot))