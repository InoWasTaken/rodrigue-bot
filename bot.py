import datetime
import discord
from discord.embeds import Embed
from discord.ext import commands
import os
from villagers import get_villager, get_house
from museum import get_fish

RODRIGUE_TOKEN = os.getenv("RODRIGUE_TOKEN")

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))


@bot.command()
async def hab(ctx, villager_name=None):
    print(f"{datetime.datetime.now()} - !hab {villager_name} made by {ctx.author} in {ctx.guild}")
    villager = get_villager(villager_name)
    if type(villager) == str:
        await ctx.send(villager)
    else:
        await ctx.send(embed=villager)


@bot.command()
async def maison(ctx, villager_name=None):
    print(f"{datetime.datetime.now()} - !maison {villager_name} made by {ctx.author} in {ctx.guild}")
    house = get_house(villager_name)
    if type(house) == str:
        await ctx.send(house)
    else:
        await ctx.send(embed=house)


@bot.command()
async def poisson(ctx, fish_name=None):
    print(f"{datetime.datetime.now()} - !poisson {fish_name} made by {ctx.author} in {ctx.guild}")
    fish = get_fish(fish_name)
    if type(fish) == str:
        await ctx.send(fish)
    else:
        await ctx.send(embed=fish)

bot.run(RODRIGUE_TOKEN)
