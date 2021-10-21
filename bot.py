import datetime
import discord
from discord.embeds import Embed
from discord.ext import commands
import json
import os

RODRIGUE_TOKEN = os.getenv("RODRIGUE_TOKEN")

bot = commands.Bot(command_prefix='!')
f = open('villagers.json')
villagers = json.load(f)
f.close()


@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))


def find_villager(villager_name):
    for villager in villagers:
        if villager_name.lower() == villager["name"]["name-EUfr"].lower():
            return villager
    return None


@bot.command()
async def hab(ctx, villager_name=None):
    print(f"{datetime.datetime.now()} - !hab {villager_name} made by {ctx.author}")
    if villager_name is None:
        await ctx.send("Merci d'entrer le nom d'un habitant.")
        return
    villager = find_villager(villager_name)
    if villager is None:
        await ctx.send("Habitant non reconnu.")
        return
    if villager["gender"] == "Male":
        description = f"**{villager['name']['name-EUfr']}** est un habitant de personnalité **{villager['personality']}**, né le **{villager['birthday']}**."
    else:
        description = f"**{villager['name']['name-EUfr']}** est une habitante de personnalité **{villager['personality']}**, née le **{villager['birthday']}**."
    embed = Embed(
        title=villager["name"]["name-EUfr"],
        colour=int(villager["bubble-color"][1:], base=16),
        description=description,
    )
    embed.set_thumbnail(url=villager["image_uri"])
    embed.add_field(name="🇬🇧 Nom Anglais",
                    value=villager['name']['name-USen'], inline=False)
    embed.add_field(name="Espèce",
                    value=villager['species'], inline=True)
    embed.add_field(name="Phrase de signature",
                    value=villager['catch-translations']['catch-EUfr'], inline=True)
    embed.add_field(name="Hobby",
                    value=villager['hobby'], inline=True)
    embed.add_field(name="Couleurs favorites",
                    value=villager['colors'], inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def maison(ctx, villager_name=None):
    print(f"{datetime.datetime.now()} - !maison {villager_name} made by {ctx.author}")
    if villager_name is None:
        await ctx.send("Merci d'entrer le nom d'un habitant.")
        return
    villager = find_villager(villager_name)
    if villager is None:
        await ctx.send("Habitant non reconnu.")
        return
    embed = Embed(
        colour=int(villager["bubble-color"][1:], base=16),
    )
    embed.set_author(
        name=f"Maison de {villager['name']['name-EUfr']}.", icon_url=villager['icon_uri'])
    embed.set_image(url=villager["house"])
    await ctx.send(embed=embed)

bot.run(RODRIGUE_TOKEN)
