import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")

# Commande slash de test
@bot.tree.command(name="ping", description="Vérifie si le bot est en ligne")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong 🏓")

# Protection simple : kick ceux qui rejoignent trop vite
@bot.event
async def on_member_join(member):
    guild = member.guild
    recent_joins = getattr(guild, "recent_joins", [])
    recent_joins = [m for m in recent_joins if (discord.utils.utcnow() - m[1]).seconds < 10]
    recent_joins.append((member, discord.utils.utcnow()))
    guild.recent_joins = recent_joins

    if len(recent_joins) >= 5:  # si + de 5 joins en 10s
        try:
            await member.kick(reason="Anti-Raid: arrivée suspecte")
        except:
            pass

bot.run(os.getenv("TOKEN"))
