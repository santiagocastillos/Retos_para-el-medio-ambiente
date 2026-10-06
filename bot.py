import discord
from discord.ext import commands
import random
import os

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send('Hola, soy 13298 y sere tu bot retador, si queres más información escribe "$info".')

@bot.command()
async def info(ctx):
    await ctx.send('Yo te enviare retos para no contaminar el medio ambiente y los vas a completar,si quieres un reto escribe "$reto".')

@bot.command()
async def reto(ctx):
    retos = random.choice(os.listdir('Retos'))
    with open(f'Retos/{retos}', 'r') as f:
        retos = f.read()
    await ctx.send(retos)

bot.run("Token <---")
