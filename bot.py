import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="?")

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

blanquer = ["reform","réform","blanquer"]
regle = ["nouvelle règle","nouvelle regle"]
@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and not message.mention_everyone:
        await message.channel.send("je être en fonctionnement")
    for bl in blanquer:
        if bl in message.content.lower():
            await message.channel.send("https://cdn.discordapp.com/attachments/736134511930376252/774312797005021214/blanquestre2.gif")
            break
    for re in regle:
        if re in message.content.lower():
            await message.channel.send("https://cdn.discordapp.com/attachments/605018726416252929/773520458611949568/nouvelle_regle.png")
            break
    if message.content.lower().endswith("quoi"):
        await message.channel.send("feur")

discordToken = open("secret_discord.txt", "r")
bot.run(discordToken.read())