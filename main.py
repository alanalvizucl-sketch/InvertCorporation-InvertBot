import os
from threading import Thread
import discord
from discord.ext import commands
from flask import Flask

# 1. Mini servidor web para mantener vivo a Render
app = Flask('')

@app.route('/')
def home():
    return "InvertBot está vivo!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# 2. Configuración del Bot de Discord
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    # Sincroniza los comandos slash (/) con Discord
    await bot.tree.sync()
    print(f'Bot conectado como {bot.user} y comandos / sincronizados!')

# 3. Comando Slash: /test
@bot.tree.command(name="test", description="testing.")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("hi fellow user")

# 4. Arrancar servidor web y bot
Thread(target=run_web).start()
bot.run(os.environ["DISCORD_TOKEN"])
