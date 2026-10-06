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
    await ctx.send('Hola, soy tu bot retador, te dare retos para no contaminar el medio ambiente, si quieres un reto escribe "$reto".')

@bot.command()
async def reto(ctx):
    retos = random.choice(os.listdir('Retos'))
    with open(f'Retos/{retos}', 'r') as f:
        retos = f.read()
    await ctx.send(retos)

@bot.command()
async def r_completados(ctx):
    r_compt = os.listdir('Rs_Completados')
    await ctx.send(r_compt)

bot.run("Token <---")
