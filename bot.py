import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("oui")

@bot.command()
async def emotes(ctx):
    emotes = {}
    serv = ctx.guild
    for emoji in serv.emojis:
        if not emoji.animated:
            emotes.update({emoji.name : 0})
    nbSalons = len(serv.text_channels)
    i = 0
    for chan in serv.text_channels:
        messages = await chan.history(limit=None).flatten()
        for message in messages:
            for emote in emotes:
                if emote in message.content:
                    emotes[emote] +=1
        i += 1
        if i == 1:
            await ctx.send("silenss, on analyz lé salon(" + str(i) + "/" + str(nbSalons) + ")" + "\n(ça risque d'être long)")
        else:
            await ctx.send(str(i) + "/" + str(nbSalons))
    await ctx.send("analyz fini!!!")
    emotes = sorted(emotes.items(), key=lambda x:x[1])
    retour = ""
    for cle, valeur in emotes:
        retour += str(cle + ": " + str(valeur) + "\n")
    await ctx.send(retour)

discordToken = open("secret_discord.txt", "r")
bot.run(discordToken.read())