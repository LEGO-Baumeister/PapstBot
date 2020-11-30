import discord
from discord.ext import commands, tasks
from random import choice
from secrets import token

client = commands.Bot(command_prefix='+')
statuses = ["In nomine Patris et Filii, et Spiritus Sancti. Amen.", "Gloria Patri, et Filio, et Spiritui Sancto.",
            "Misereatur vestri omnipotens Deus, et dimissis peccatis vestris, perducat vos ad vitam aeternam.", "Credo in Deum Patrem omnipotentem, Creatorem caeli et terrae."]
null = ["Bedenke, Mensch, dass du Staub bist und wieder zum Staub zurückkehren wirst.", "Der Tag des jüngsten Gerichts wird kommen.", "Vater, vergib ihnen, denn sie wissen nicht, was sie tun.", "Amen, ich sage dir: Heute noch wirst du mit mir im Paradies sein."]


@client.event
async def on_ready():
    change_status.start()
    print("Unsere hilfe ist im Namen des Herrn\n")
    print("Der Himmel und Erde erschaffen hat.")


@client.command(aliases=["bete"])
async def pray(ctx, arg1=None, arg2=None):

    pater_noster = ["paternoster", "pn", "vaterunser", "lordsprayer"]
    credo = ["credo", "glaubensbekenntnis", "creed"]
    ave_maria = ["avemaria", "am", "gegrüßetseistdumaria", "hailmary"]

    if arg1 == None:
        await ctx.send(choice(null), tts=True)
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
            await ctx.send("""Vater unser im Himmel, geheiligt werde dein Name.
Dein Reich komme.
Dein Wille geschehe,
wie im Himmel so auf Erden.
Unser tägliches Brot gib uns heute.""", tts=True)
            await ctx.send("""Und vergib uns unsere Schuld,
wie auch wir vergeben unsern Schuldigern.
Und führe uns nicht in Versuchung,
sondern erlöse uns von dem Bösen.""", tts=True)
            await ctx.send("""Denn dein ist das Reich und die Kraft
und die Herrlichkeit in Ewigkeit.
Amen.""", tts=True)
        elif iso == "la":
            await ctx.send("""Pater noster, qui es in caelis:
sanctificetur nomen tuum.
Adveniat regnum tuum.
Fiat voluntas tua, sicut in caelo, et in terra.
Panem nostrum catidianum da nobis hodie""", tts=True)
            await ctx.send("""Et dimitte nobis debita nostra,
sicut et nos dimittimus debitoribus nostris.
Et ne nos inducas in tentationem,
sed libera nos a malo.""", tts=True)
            await ctx.send("""Quia tuum est regnum et potestas et gloria
in saecula.
Amen.""", tts=True)
        elif iso == "en":
            await ctx.send("""Our Father, who art in heaven, hallowed be thy name;
thy kingdom come; thy will be done on earth as it is in heaven.
Give us this day our daily bread;""", tts=True)
            await ctx.send("""and forgive us our trespasses,
as we forgive those who trespass against us;
and lead us not into temptation,
but deliver us from evil.""", tts=True)
            await ctx.send("""For the kingdom,
the power and the glory are yours
now and for ever.
Amen.""", tts=True)

async def ave_maria_fun(ctx, voice: bool, iso: str):
    if voice:
        pass
    else:
        if iso == "de":
            await ctx.send("""Gegrüßet seist du, Maria, voll der Gnade,
der Herr ist mit dir.
Du bist gebenedeit unter den Frauen,
und gebenedeit ist die Frucht deines Leibes, Jesus.""", tts=True)
            await ctx.send("""Heilige Maria, Mutter Gottes,
bitte für uns Sünder
jetzt und in der Stunde unseres Todes.
Amen.""", tts=True)
        elif iso == "la":
            await ctx.send("""Ave Maria, gratia plena,
Dominus tecum.
Benedicta tu in mulieribus,
et benedictus fructus ventris tui, Iesus.""", tts=True)
            await ctx.send("""Sancta Maria, Mater Dei,
ora pro nobis peccatoribus
nunc et in hora mortis nostrae.
Amen""", tts=True)
        elif iso == "en":
            await ctx.send("""Hail Mary, full of grace,
the Lord is with thee.
Blessed art thou amongst women,
and blessed is the fruit of thy womb, Jesus.""", tts=True)
            await ctx.send("""Holy Mary, Mother of God,
pray for us sinners,
now and at the hour of our death.
Amen.""", tts=True)


client.run(token)
