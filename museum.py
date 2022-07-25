import json
from discord.embeds import Embed

f = open('fishes.json')
fishes = list(json.load(f).values())
f.close()


def find_fish(fish_name):
    for fish in fishes:
        if fish_name.lower() == fish["name"]["name-EUfr"].lower():
            return fish
    return None


def get_fish(fish_name):
    if fish_name is None:
        return "Merci d'entrer le nom d'un poisson."
    fish = find_fish(fish_name)
    if fish is None:
        return "Poisson non reconnu."
    if fish["availability"]["isAllDay"] is True:
        hour = "Toute la journée"
    else:
        hour = fish["availability"]["time"]
    if fish["availability"]["isAllYear"] is True:
        month = "Toute l'année"
    else:
        month = f"Nord: {fish['availability']['month-northern']}\nSud: {fish['availability']['month-southern']}"
    embed = Embed(
        colour=0xbeb360,
    )
    embed.set_author(name=fish["name"]["name-EUfr"],
                     icon_url=fish['icon_uri'],)
    embed.set_image(url=fish["image_uri"])
    embed.add_field(name="📍 Localisation",
                    value=fish["availability"]['location'], inline=True)
    embed.add_field(name="🕰️ Heure", value=hour, inline=True)
    embed.add_field(name="🌟 Rareté",
                    value=fish["availability"]['rarity'], inline=True)
    embed.add_field(name="⚫ Ombre",
                    value=fish["shadow"], inline=True)
    embed.add_field(name="🌍 Période", value=month, inline=True)
    embed.add_field(name="🪙 Prix",
                    value=f"Boutique: {fish['price']} clochettes\nPollux: {fish['price-cj']} clochettes", inline=True)
    return embed
