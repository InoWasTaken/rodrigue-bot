import json
from discord.embeds import Embed


f = open('villagers.json')
villagers = json.load(f)
f.close()


def find_villager(villager_name):
    for villager in villagers:
        if villager_name.lower() == villager["name"]["name-EUfr"].lower():
            return villager
    return None


def get_villager(villager_name):
    if villager_name is None:
        return "Merci d'entrer le nom d'un habitant."
    villager = find_villager(villager_name)
    if villager is None:
        return "Habitant non reconnu."
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
    return embed


def get_house(villager_name):
    if villager_name is None:
        return "Merci d'entrer le nom d'un habitant."
        return
    villager = find_villager(villager_name)
    if villager is None:
        return "Habitant non reconnu."
        return
    embed = Embed(
        colour=int(villager["bubble-color"][1:], base=16),
    )
    embed.set_author(
        name=f"Maison de {villager['name']['name-EUfr']}.", icon_url=villager['icon_uri'])
    embed.set_image(url=villager["house"])
    return embed
