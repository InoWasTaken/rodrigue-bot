import json
from discord.embeds import Embed

f = open('fishes.json')
fishes = list(json.load(f).values())
f.close()

b = open('bugs.json')
bugs = list(json.load(b).values())
b.close()


def find_fish(fish_name):
    names = [fish_name.lower()]
    if " " in fish_name:
        names.append(fish_name.lower().replace(" ", "-"))
    elif "-" in fish_name:
        names.append(fish_name.lower().replace("-", " "))
    for fish in fishes:
        if fish["name"]["name-EUfr"].lower() in names:
            return fish
    return None


def find_creature(creature_name, creatures):
    for creature in creatures:
        if creature_name.lower() == creature["name"]["name-EUfr"].lower():
            return creature
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
    embed.set_author(name=fish["name"]["name-EUfr"].title(),
                     icon_url=fish['icon_uri'],)
    embed.set_image(url=fish["image_uri"])
    embed.add_field(name="📍 Localisation",
                    value=fish["availability"]['location'], inline=True)
    embed.add_field(name="🕰️ Heure", value=hour, inline=True)
    embed.add_field(name="🌟 Rareté",
                    value=fish["availability"]['rarity'], inline=True)
    embed.add_field(name="⚫ Ombre",
                    value=fish["shadow"], inline=True)
    embed.add_field(name="🌍 Mois", value=month, inline=True)
    embed.add_field(name="🪙 Prix",
                    value=f"Boutique: {fish['price']} clochettes\nPollux: {fish['price-cj']} clochettes", inline=True)
    return embed


def get_bug(bug_name):
    if bug_name is None:
        return "Merci d'entrer le nom d'un insecte."
    bug = find_creature(bug_name, bugs)
    if bug is None:
        return "Insecte non reconnu."
    if bug["availability"]["isAllDay"] is True:
        hour = "Toute la journée"
    else:
        hour = bug["availability"]["time"]
    if bug["availability"]["isAllYear"] is True:
        month = "Toute l'année"
    else:
        month = f"Nord: {bug['availability']['month-northern']}\nSud: {bug['availability']['month-southern']}"
    embed = Embed(
        colour=0xa4c9a4,
    )
    embed.set_author(name=bug["name"]["name-EUfr"].title(),
                     icon_url=bug['icon_uri'],)
    embed.set_image(url=bug["image_uri"])
    embed.add_field(name="📍 Localisation",
                    value=bug["availability"]['location'], inline=True)
    embed.add_field(name="🕰️ Heure", value=hour, inline=True)
    embed.add_field(name="🌟 Rareté",
                    value=bug["availability"]['rarity'], inline=True)
    embed.add_field(name="🌍 Mois", value=month, inline=True)
    embed.add_field(name="🪙 Prix",
                    value=f"Boutique: {bug['price']} clochettes\Djason: {bug['price-flick']} clochettes", inline=True)
    return embed
