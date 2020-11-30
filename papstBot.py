import discord
from discord.ext import commands, tasks
from random import choice

import prayers
from secrets import token

client = commands.Bot(command_prefix='+')
statuses = ["In nomine Patris et Filii, et Spiritus Sancti. Amen.", "Gloria Patri, et Filio, et Spiritui Sancto.",
            "Misereatur vestri omnipotens Deus, et dimissis peccatis vestris, perducat vos ad vitam aeternam.", "Credo in Deum Patrem omnipotentem, Creatorem caeli et terrae."]
null = ["Bedenke, Mensch, dass du Staub bist und wieder zum Staub zurückkehren wirst.", "Der Tag des jüngsten Gerichts wird kommen.", "Vater, vergib ihnen, denn sie wissen nicht, was sie tun.", "Amen, ich sage dir: Heute noch wirst du mit mir im Paradies sein."]


@client.event
async def on_ready():
    change_status.start()
    print("Unsere hilfe ist im Namen des Herrn")
    print("Der Himmel und Erde erschaffen hat.")


@client.command(aliases=["bete"])
async def pray(ctx, arg1=None, arg2=None):

    pater_noster = ["paternoster", "pn", "vaterunser", "lordsprayer"]
    credo = ["credo", "glaubensbekenntnis", "creed"]
    ave_maria = ["avemaria", "am", "gegrüßetseistdumaria", "hailmary"]

    embed = discord.Embed(title="Command Help")
    embed.add_field(name="Nutze:",value="+bete < paternoster | credo | avemaria > < de | la | en>")

    if arg1 == None:
        await ctx.send(choice(null), tts=True)
        await ctx.send(embed=embed)
    elif arg1.lower() in pater_noster:
        await pater_noster_fun(ctx=ctx, voice=False, iso=arg2)
    elif arg1.lower() in credo:
        await ctx.send("Credo")
    elif arg1.lower() in ave_maria:
        await ave_maria_fun(ctx=ctx, voice=False, iso=arg2)

    if ctx.message.author.voice and ctx.author.voice.channel:
        channel = ctx.message.author.voice.channel
        await channel.connect()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg: str = message.content

    if ("+" in msg or "†" in msg) and len(msg) < 2:
        await message.channel.send("Amen.", tts=True)
    await client.process_commands(message)


@client.command(aliases=["taufe"])
async def baptize(ctx, member: discord.Member):
    await ctx.send(member.mention + ", ich taufe dich im Namen des Vaters, des Sohnes und des Heiligen Geistes!")


@client.command()
async def amen(ctx):
    await ctx.send("Amen", tts=True)


@tasks.loop(seconds=25)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(statuses)))


async def pater_noster_fun(ctx, voice: bool, iso: str):
    if voice:
        pass
    else:
        if iso == "de":
            await ctx.send(prayers.vater_unser_de[0], tts=True)
            await ctx.send(prayers.vater_unser_de[1], tts=True)
            await ctx.send(prayers.vater_unser_de[2], tts=True)
        elif iso == "la":
            await ctx.send(prayers.vater_unser_la[0], tts=True)
            await ctx.send(prayers.vater_unser_la[1], tts=True)
            await ctx.send(prayers.vater_unser_la[2], tts=True)
        elif iso == "en":
            await ctx.send(prayers.vater_unser_en[0], tts=True)
            await ctx.send(prayers.vater_unser_en[1], tts=True)
            await ctx.send(prayers.vater_unser_en[2], tts=True)

async def ave_maria_fun(ctx, voice: bool, iso: str):
    if voice:
        pass
    else:
        if iso == "de":
            await ctx.send(prayers.ave_maria_de[0], tts=True)
            await ctx.send(prayers.ave_maria_de[1], tts=True)
        elif iso == "la":
            await ctx.send(prayers.ave_maria_la[0], tts=True)
            await ctx.send(prayers.ave_maria_la[1], tts=True)
        elif iso == "en":
            await ctx.send(prayers.ave_maria_en[0], tts=True)
            await ctx.send(prayers.ave_maria_en[1], tts=True)

client.run(token)
