import discord
from discord.ext import commands

import giphy_client
from giphy_client.rest import ApiException
import random

bot = commands.Bot(command_prefix='!',description='Bot de moninho')
#Comandos
#
# Comando !moninho (Muestra el meme de Moninho)
@bot.command()
async def moninho(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/545316153644548106/971146809042927616/unknown.png')

#Comando !coscorron manda un mensaje de coscorron al usuario tageado
@bot.command()
#@commands.has_permissions(administrator=True) Permisos admin
async def coscorron (ctx, mention: discord.User):
    user = ctx.message.author.id
    await ctx.send(f"<@{user}> Le ha dado tremendo Coscorrón cuchiflús en le esquina inferior derecha del talon de aquiles a <@{mention.id}> que lo dejo morido bien muerto.")
#Comando !monke manda un mensaje de coscorron al usuario tageado
@bot.command()
async def monke(ctx,*,q="Monkey"):
    api_key = "WbkD0H5BGbui8J2nFeVs29SUM1g5LA4v"
    api_instance = giphy_client.DefaultApi()

    try:
        api_responce = api_instance.gifs_search_get(api_key, q, limit=100, rating="g")
        lst = list(api_responce.data)
        giff = random.choice(lst)

        emb = discord.Embed(title='Mi loco wachate tremendos monos CSM', color=discord.Color.green())
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send(embed=emb)
    except ApiException as e:
        print("Exepcion en el llamado de la API")

#eventos
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Ser facha 😎'))
    print('Bot Corrriendo')

bot.run('OTc3MzEyNDU3MzQzMjM4MjI0.GQhemf.RBiwo8KaMLV3_Vk7iRTXmAtbbpngQpgxbt4Ar8')