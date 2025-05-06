import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

# Récupère le token stocké sur Railway
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user.name}")

bot.run(TOKEN)
