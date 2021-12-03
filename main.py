import os
import discord
from discord.ext.commands import Bot
import asyncio

from discord.colour import Color
from discord.ext.commands.core import is_owner
from uwuify import uwu
from discord.ext import commands
from time import time
from datetime import datetime
from random import randint, seed

JAV = 203211179613487106
JRN = 307353668695621633
ADT = 310479313814159364
VG = 883135611907735582
JB = 215188148882243584
GL = 256993314174271489
ADMIN = [ADT, JAV, JRN, GL]

global TOKEN
TOKEN = os.environ['TOKEN']

# Set up Intents
intents = discord.Intents.all()
bot = Bot(command_prefix='!', intents=intents)
CHAT = 638163732920270889
EEMSG = 789236911364505600
CPEMSG = 789236918872703018
CSMSG = 789236932693459014
COLORMSG = 789281035657412619
SDMSG = 789241290411868170
WELCOME = 694552494172536833

Color_Emoji = {
    "<:invisible:789271633343807488>": ["invisible",
                                        Color.dark_theme()],
    "<:greyple:789271633352589352>": ["greyple", Color.greyple()],
    "<:white:789271633360977960>": ["white",
                                    Color.from_rgb(255, 255, 255)],
    "<:teal:789271633373298718>": ["teal", Color.teal()],
    "<:darkteal:789271633356521473>": ["darkteal",
                                       Color.dark_teal()],
    "<:darkgreen:789271633336205342>": ["darkgreen",
                                        Color.dark_green()],
    "<:blurple:789271633356783666>": ["blurple", Color.blurple()],
    "<:darkblue:789271633373954048>": ["darkblue",
                                       Color.dark_blue()],
    "<:darkpurple:789271633386405908>": ["darkpurple",
                                         Color.dark_purple()],
    "<:purple:789271633436737586>": ["purple", Color.purple()],
    "<:darkorange:789271633332142091>": ["darkorange",
                                         Color.dark_orange()],
    "<:gold:789271633415503902>": ["gold", Color.gold()],
}

SD_Emoji = {
    "<:SD0:789240178191368212>": "SD0",
    "<:SD1:789240178077466644>": "SD1",
    "<:SD2:789240178198970448>": "SD2"
}

EE_Emoji = {
    "<:340:789183456466567198>": "Signals",
    "<:341:789183456398802974>": "Comms",
    "<:353:789183456461848577>": "EMag1",
    "<:354:789183456100745217>": "EMag2",
    "<:360:789183456016859177>": "PhysElec",
    "<:361:789183456504446986>": "EDesign",
    "<:371:789183456558841876>": "Controls",
    "<:441:789183456331956246>": "DigitalComms",
    "<:453:789183456566968330>": "Antennas",
    "<:483:789183456193282119>": "Power",
    "<:434:797999706600898591>": "ActiveCircuits",
    "<:445:797999707133444107>": "WirelessComms",
    "<:485:798052353327759380>": "ElectricMotorDrives"
}

CPE_Emoji = {
    "<:320:789183456181092433>": "CompSys",
    "<:410:789183456210583573>": "ESC",
    "<:415:789183456147931167>": "SystemSim",
    "<:420:789183456268648501>": "CSD",
    "<:427:789183456482820106>": "CN",
    "<:440:789183456608780308>": "DSP",
    "<:442:789183456671825951>": "ESI",
    "<:462:789183456315572226>": "AnalogIC",
    "<:467:789183456504053792>": "VLSI",
    "<:4981:789183456479150101>": "IS",
    "<:4980:789183456433012817>": "NES",
}

CS_Emoji = {
    "<:316:789183456231948338>": "DS",
    "<:426:789183456500252732>": "OS",
    "<:475:789183456449396746>": "DB",
}


async def record_usage(ctx):
    t = datetime.fromtimestamp(time()).strftime('%I:%M:%S %p')
    print(t, ":", ctx.author, 'used', ctx.command)


seed()
custom = {
    "@": ["<:at:759418946570027028>"],
}
lookup = {
    "A": ["a", "regional_indicator_a"],
    "B": ["b", "regional_indicator_b"],
    "C": [
        "regional_indicator_c", "copyright", "call_me", "ocean",
        "star_and_crescent", "arrow_right_hook", "compression"
    ],
    "D": ["regional_indicator_d", "leftwards_arrow_with_hook", "dizzy"],
    "E": ["email", "regional_indicator_e"],
    "F": ["regional_indicator_f", "flags"],
    "G": ["regional_indicator_g"],
    "H": ["regional_indicator_h", "pisces"],
    "I": [
        "lipstick", "spoon", "regional_indicator_i", "information_source",
        "gemini", "warning"
    ],
    "J": ["regional_indicator_j", "arrow_heading_up", "field_hockey"],
    "K": ["regional_indicator_k"],
    "L": ["mechanical_arm", "regional_indicator_l", "boot"],
    "M": [
        "m", "regional_indicator_m", "virgo", "scorpius",
        "part_alternation_mark"
    ],
    "N": [
        "regional_indicator_n",
        "capricorn",
    ],
    "O": [
        "ring", "ok_hand", "yarn", "full_moon_with_face", "soccer",
        "basketball", "baseball", "volleyball", "cd", "o2", "o",
        "regional_indicator_o"
    ],
    "P": ["parking", "regional_indicator_p"],
    "Q": ["regional_indicator_q"],
    "R": ["regional_indicator_r", "registered"],
    "S": ["regional_indicator_s", "heavy_dollar_sign", "zap", "moneybag"],
    "T": ["regional_indicator_t", "cross"],
    "U": ["regional_indicator_u", "metal", "ophiuchus"],
    "V": ["regional_indicator_v", "v", "aries"],
    "W": ["regional_indicator_w", "love_you_gesture", "wavy_dash"],
    "X": [
        "x", "regional_indicator_x", "twisted_rightwards_arrows", "scissors",
        "crossed_swords", "tools"
    ],
    "Y": ["regional_indicator_y", "chart"],
    "Z": ["regional_indicator_z", "zzz"],
    '1': ["first_place", "one"],
    '2': ["second_place", "two"],
    '3': ["third_place", "three"],
    '4': ["four"],
    '5': ["five"],
    '6': ["six"],
    '7': ["seven"],
    '8': [
        "eight",
    ],
    '9': ["nine"],
    '0': ["zero", "arrows_clockwise"],
    '!': ["exclamation", "grey_exclamation", "heart_exclamation"],
    '?': ["question", "grey_question"],
}


def emojify(text):
    newText = ""
    for i in text:
        if i == ' ':
            newText += "⠀"
            continue
        if i.upper() not in custom and i.upper() not in lookup:
            newText += i
            continue
        for key, val in custom.items():
            if i.upper() == key:
                randInt = randint(0, len(val) - 1)
                newText = newText + " " + val[randInt]
                continue
        for key, val in lookup.items():
            if i.upper() == key:
                randInt = randint(0, len(val) - 1)
                newText = newText + ":" + val[randInt] + ":"
    return newText


def sarcastify(text):
    newText = ""
    for i in text:
        randInt = randint(0, 100)
        if i == ' ':
            newText += " "
            continue
        if randInt > 50:
            newText += i.upper()
        else:
            newText += i.lower()
    return newText


global hugs
hugs = [
    "https://tenor.com/view/milk-and-mocha-hug-cute-kawaii-love-gif-12535134",
    "https://tenor.com/view/love-couple-hug-cute-cat-gif-16032768",
    "https://tenor.com/view/hugs-hugging-hearts-love-hug-you-gif-12853824",
    "https://giphy.com/gifs/editingandlayout-the-office-hug-michael-scott-yidUzriaAGJbsxt58k",
    "https://giphy.com/gifs/hug-love-winnie-the-pooh-llmZp6fCVb4ju",
    "https://giphy.com/gifs/cheezburger-hug-baymax-lXiRKBj0SAA0EWvbG",
    "https://giphy.com/gifs/Friends-friends-episode-16-tv-VbawWIGNtKYwOFXF7U",
    "https://giphy.com/gifs/duck-animal-friendship-pals-4No2q4ROPXO7T6NWhS",
    "https://giphy.com/gifs/etredcarpet--golden-globes-2017-3o6ZtbGDpbSMEbffiM",
    "https://giphy.com/gifs/Friends-season-6-friends-tv-episode-602-eMIGPdZ77kPgD7nf4j",
    "https://giphy.com/gifs/homer-simpson-the-simpsons-season-12-1GJRIgTY4sS6k",
    "https://giphy.com/gifs/hug-cat-love-NhjPhBQIIxdxm",
    "https://giphy.com/gifs/martin-hug-lawrence-4vDQtFRvx5ZSM",
    "https://giphy.com/gifs/hug-brother-bbxTrFmeoM7aU"
]

global kicks
kicks = [
    "https://giphy.com/gifs/qiiimDJtLj4XK",
    "https://giphy.com/gifs/7YDt9L1xHnTMMqTxb9",
    "https://giphy.com/gifs/guy-poor-craigslist-m1O4GT06grh7y",
    "https://giphy.com/gifs/rickandmorty-season-1-adult-swim-rick-and-morty-SsZViiaRCjgp8fVexU",
    "https://giphy.com/gifs/LICtqQ1K8ClIQ",
    "https://giphy.com/gifs/slow-kicking-zfpYRDqJuCy1G",
    "https://giphy.com/gifs/3doorsdown-music-video-dark-3-doors-down-l4KhOQepZPT78KOnS",
    "https://giphy.com/gifs/running-jump-12S5BqrFL93xxC",
    "https://giphy.com/gifs/fail-fall-12U7o1559rI7Nm",
]

global nope
nope = [
    "no", "nein", "nyet", "I don't think I will", "nah", "nope", "NEVER",
    "uh uh", "uh uh uh", "dude...", "fuck that", "yeah, right",
    "nope on a rope", "yes, but no", "I'lL gEt RigHt On ThAT", "lol", ":|",
    "meh", "Try Again Later", "Not likely", "Command not found", "ehhhhh. no"
]

global lastrand
lastrand = []


def prand(min, max):
    global lastrand
    rand = randint(min, max)
    if (max - min) > len(lastrand):
        while rand in lastrand:
            rand = randint(min, max)
    lastrand.append(rand)
    if len(lastrand) > 3:
        lastrand.pop(0)
    return rand


def randresponse(links):
    rand = prand(0, len(links) - 1)
    return links[rand]


def check_role(roles, name):
    for role in roles:
        if name == role.name:
            return True
    return False


@bot.command(name="randnum")
@is_owner()
async def randomnum(ctx, min=0, max=6):
    rand = prand(int(min), int(max))
    await ctx.send(f"Randomly Rolled {rand}")


@bot.command(name='Roles', command_prefix='$')
@is_owner()
@commands.before_invoke(record_usage)
async def create_roles(ctx):
    guild = ctx.guild
    # print(guild)
    # print(guild.roles)
    for role in SD_Emoji.values():
        if not check_role(guild.roles, role):
            await guild.create_role(name=role, mentionable=True)
    for role in Color_Emoji.values():
        if not check_role(guild.roles, role[0]):
            await guild.create_role(name=role[0], color=role[1])
    for role in EE_Emoji.values():
        if not check_role(guild.roles, role):
            await guild.create_role(name=role, mentionable=True)
    for role in CPE_Emoji.values():
        if not check_role(guild.roles, role):
            await guild.create_role(name=role, mentionable=True)
    for role in CS_Emoji.values():
        if not check_role(guild.roles, role):
            await guild.create_role(name=role, mentionable=True)


@bot.command(name='SD', command_prefix='$')
@is_owner()
@commands.before_invoke(record_usage)
async def add_SD_Emojis(ctx):
    chan = ctx.channel
    msg = discord.PartialMessage(id=SDMSG, channel=chan)
    for emoji in SD_Emoji:
        await msg.add_reaction(emoji)


@bot.command(name='Colors', command_prefix='$')
@is_owner()
@commands.before_invoke(record_usage)
async def add_Color_Emojis(ctx):
    chan = ctx.channel
    msg = discord.PartialMessage(id=COLORMSG, channel=chan)
    for emoji in Color_Emoji:
        await msg.add_reaction(emoji)


@bot.command(name='EE', command_prefix='$')
@is_owner()
@commands.before_invoke(record_usage)
async def add_EE_Emojis(ctx):
    chan = ctx.channel
    msg = discord.PartialMessage(id=EEMSG, channel=chan)
    for emoji in EE_Emoji:
        await msg.add_reaction(emoji)


@bot.command(name='CPE', command_prefix='$')
@is_owner()
@commands.before_invoke(record_usage)
async def add_CPE_Emojis(ctx):
    chan = ctx.channel
    msg = discord.PartialMessage(id=EEMSG, channel=chan)
    for emoji in CPE_Emoji:
        await msg.add_reaction(emoji)


@bot.command(name='WELCOME', command_prefix='$')
@is_owner()
@commands.before_invoke(record_usage)
async def add_welcome_Emojis(ctx):
    chan = ctx.channel
    msg = discord.PartialMessage(id=WELCOME, channel=chan)
    await msg.add_reaction('✅')


@bot.command(name='CS', command_prefix='$')
@is_owner()
@commands.before_invoke(record_usage)
async def add_CS_Emojis(ctx):
    chan = ctx.channel
    msg = discord.PartialMessage(id=CSMSG, channel=chan)
    for emoji in CS_Emoji:
        await msg.add_reaction(emoji)


@bot.event
async def on_raw_reaction_add(payload):
    member = payload.member
    if member.bot:
        return
    emoji = str(payload.emoji)
    msg = payload.message_id
    message = await bot.get_channel(payload.channel_id
                                    ).fetch_message(payload.message_id)
    if msg == WELCOME:
        if emoji == '✅':
            role = discord.utils.get(member.guild.roles, name='Initiated')
            await member.add_roles(role)
            role = discord.utils.get(member.guild.roles, name='Uninitiated')
            await member.remove_roles(role)
    if msg == CSMSG:
        if emoji in CS_Emoji:
            role = discord.utils.get(member.guild.roles, name=CS_Emoji[emoji])
            await member.add_roles(role)
        else:
            await message.remove_reaction(emoji, member)
    elif msg == CPEMSG:
        if emoji in CPE_Emoji:
            role = discord.utils.get(member.guild.roles, name=CPE_Emoji[emoji])
            await member.add_roles(role)
        else:
            await message.remove_reaction(emoji, member)
    elif msg == EEMSG:
        if emoji in EE_Emoji:
            role = discord.utils.get(member.guild.roles, name=EE_Emoji[emoji])
            await member.add_roles(role)
        else:
            await message.remove_reaction(emoji, member)
    elif msg == SDMSG:
        if emoji in SD_Emoji:
            role = discord.utils.get(member.guild.roles, name=SD_Emoji[emoji])
            await member.add_roles(role)
        else:
            await message.remove_reaction(emoji, member)
    elif msg == COLORMSG:
        if emoji in Color_Emoji:
            role = discord.utils.get(member.guild.roles,
                                     name=Color_Emoji[emoji][0])
            await member.add_roles(role)
        else:
            await message.remove_reaction(emoji, member)


@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(id=payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)
    if member.bot:
        return
    emoji = str(payload.emoji)
    msg = payload.message_id
    if msg == CSMSG and emoji in CS_Emoji:
        role = discord.utils.get(member.guild.roles, name=CS_Emoji[emoji])
        await member.remove_roles(role)

    elif msg == CPEMSG and emoji in CPE_Emoji:
        role = discord.utils.get(member.guild.roles, name=CPE_Emoji[emoji])
        await member.remove_roles(role)
    elif msg == EEMSG and emoji in EE_Emoji:
        role = discord.utils.get(member.guild.roles, name=EE_Emoji[emoji])
        await member.remove_roles(role)
    elif msg == SDMSG and emoji in SD_Emoji:
        role = discord.utils.get(member.guild.roles, name=SD_Emoji[emoji])
        await member.remove_roles(role)
    elif msg == COLORMSG and emoji in Color_Emoji:
        role = discord.utils.get(member.guild.roles,
                                 name=Color_Emoji[emoji][0])
        await member.remove_roles(role)


@bot.command(name='emojify', help='Emojify text')
@commands.before_invoke(record_usage)
async def emoji(ctx, *, arg):
    response = emojify(arg)
    r = []
    while len(response) >= 2000:
        s = response.rfind('⠀', 0, 2000)
        res = response[:s]
        response = response[s + 1:]
        r.append(res)
    r.append(response)
    for res in r:
        await ctx.send(res)


@bot.command(name='sarcastify', help='SaRcaStiFy tExT')
@commands.before_invoke(record_usage)
async def sarcastic(ctx, *, arg):
    await ctx.send(sarcastify(arg))


@bot.command(name='hi-vinnie', help='@\'s vinnie')
@commands.before_invoke(record_usage)
async def atvinnie(ctx):
    response = '<@!{}>'.format(VG)
    await ctx.send(response)


@bot.command(name='uwu', help='You already know')
@commands.before_invoke(record_usage)
async def uwuify(ctx, *, args):
    await ctx.send(uwu(args))


@bot.command(name='test', help='Test shit out')
@commands.before_invoke(record_usage)
async def echo(ctx, *, name):
    msg = ctx.message
    await msg.delete()
    await ctx.send(name)


@bot.command(name='say')
@commands.before_invoke(record_usage)
@is_owner()
async def repeat(ctx, *, text):
    channel = bot.get_channel(CHAT)
    await channel.send(text)


@bot.command(name='kick', help='Kick something')
@commands.before_invoke(record_usage)
async def kick(ctx, args=None):
    if args is None:
        args = f"<@!{ctx.author.id}>"
        response = "Unsure who to kick"
        await ctx.send(response)
        await ctx.send(f"Kicking {args} instead")
    response = randresponse(kicks)
    await ctx.send(args + " has been kicked. ")
    await ctx.send(response)


@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id=798949146055934053)
    await member.add_roles(role)


@bot.command(name='owner', help="Display bot owner")
@commands.before_invoke(record_usage)
async def owner(ctx):
    auth = ctx.message.author.id
    print(auth)
    if auth == JRN:
        response = "Just kidding... fuck off, Josh"
        await ctx.send(f"<@{JRN}> created me")
        await asyncio.sleep(5)
    elif auth == ADT:
        response = "You made me, master"
    else:
        response = "<@{}> created me".format(ADT)
    await ctx.send(response)


@bot.command(name='hug', help="Sends a hug")
@commands.before_invoke(record_usage)
async def hugA(ctx, *, args=None):
    response = randresponse(hugs)
    if (args != None):
        await ctx.send(args)
    await ctx.send(response)


def loadPasta(pasta):
    pastas = []
    with open('./pastas/' + str(pasta), 'r') as pf:
        spaghet = []
        for line in pf.readlines():
            line = line.strip()
            # print(line)
            if line == '':
                pastas.append(spaghet)
                spaghet = []
                continue
            spaghet.append(line)
        pf.close()
    return pastas


def savePasta(pasta, spaghet):
    spaghet = "".join(spaghet)
    print(spaghet)

    with open('./pastas/' + str(pasta), 'a') as pf:
        pf.write(spaghet)
        pf.write("\n\n")
    pf.close()


def parseArgs(args):
    num = None
    mod = None
    if args:
        for i in range(len(args)):
            if i > 1:
                break
            if args[i].isnumeric():
                num = int(args[i])
            else:
                mod = args[i]
    return (num, mod)


EMOJIFY = ['e', '-e', 'emojify', 'emoji']
SARCASTIFY = ['s', '-s', 'sarcastify', 'sarcastic']
UWUIFY = ['u', '-u', 'uwuify', 'uwu']


def getIdFromAt(arg):
    id = arg[3:-1]
    good = id.isnumeric()
    return (id, good)


@bot.command(name='mimic', help='Muahaha')
@is_owner()
async def mimic(ctx, u, *, txt="Hello", d=True):
    if d:
        await ctx.message.delete()
    if u.isnumeric():
        id = int(u)
        print(id)
        good = True
    else:
        (id, good) = getIdFromAt(u)
    if not good:
        await ctx.send(randresponse(nope) + "")
        return
    user = bot.get_user(int(id))
    if user is None:
        await ctx.send(randresponse(nope) + "")
        return
    hook = await ctx.channel.create_webhook(name="mimic")
    name = ctx.message.guild.get_member(int(id))
    await hook.send(txt, username=name.nick, avatar_url=user.avatar_url)
    await hook.delete()


@bot.command(name='timer', help='We\'ll see about that')
@commands.before_invoke(record_usage)
async def timer(ctx, amt=0, unit=None, name="<@0>", *, txt):
    (id, good) = getIdFromAt(name)
    t = amt
    if not good:
        id = ctx.author.id
    if amt < 0:
        return
    if unit is None:
        return
    if unit[0].lower() == 's':
        unit = 'Seconds'
    elif unit[0].lower() == 'm':
        amt *= 60
        unit = 'Minutes'
    elif unit[0].lower() == 'h':
        amt *= 3600
        unit = 'Hours'
    elif unit[0].lower() == 'd':
        amt *= 3600
        amt *= 24
        unit = 'Days'
    await asyncio.sleep(amt)
    await ctx.send(f"<@!{id}>! it's been {t} {unit}. {txt}")



@bot.command(
    name='pasta',
    help=
        """!pasta @user [num] [-e, -s, -u]
    Sends a user's copypasta
    args:
        num to select
    modifiers:
        -e emojify 
        -s sarcastify 
        -u uwuify"""
)
@commands.before_invoke(record_usage)
async def pasta(ctx, u=None, *args):
    (num, mod) = parseArgs(args)
    if u is None:
            id = ctx.author.id
            good=True
    else:
        (id, good) = getIdFromAt(u)
    if not good:
            await ctx.send(randresponse(nope)+ f", {u} is a bad username")
            return
    user = bot.get_user(int(id))
    if user is None:
        await ctx.send(randresponse(nope) + f", user {u} not found")
        return
    CP = loadPasta(id)
    e = mod in EMOJIFY
    s = mod in SARCASTIFY
    u = mod in UWUIFY

    i = randint(0, len(CP) - 1)

    if num is not None:
        i = num
    cp = CP[i % len(CP)]
    id = f'<@!{id}>'
    for line in cp:
        if s:
            line = sarcastify(line)
        elif e:
            line = emojify(line)
        elif u:
            line = uwu(line)
        await mimic(ctx, id, txt=line, d=False)

@bot.command(
    name='vinniepasta',
    help=
    """!vinniepasta [num] [-e, -s, -u]
    Sends a vinnie copypasta
    args:
        num to select
    modifiers:
        -e emojify 
        -s sarcastify 
        -u uwuify"""
)
@commands.before_invoke(record_usage)
async def vinniepastaa(ctx, *args):
   await pasta(ctx, f'<@!{VG}>', *args)




@bot.command(
    name='shitpasta',
    help=
        """!shitpasta [num] [-e, -s, -u]
    Sends a bodenshit copypasta
    args:
        num to select
    modifiers:
        -e emojify 
        -s sarcastify 
        -u uwuify"""
)
@commands.before_invoke(record_usage)
async def shitpasta(ctx, *args):
    await pasta(ctx, f'<@!{JB}>', *args)
    


@bot.command(name='lmgtfy', help='... search it yourself')
@commands.before_invoke(record_usage)
async def lmgtfy(ctx, *, args=randresponse(nope) + ""):
    txt = args.split(' ')
    term = "+".join(txt)
    await ctx.send(f"https://www.google.com/search?q={term}")


@bot.command(name='ud', help='search urban dictionary')
@commands.before_invoke(record_usage)
async def ud(ctx, *, args=randresponse(nope) + ""):
    txt = args.split(' ')
    term = "+".join(txt)
    await ctx.send(f"https://www.urbandictionary.com/define.php?term={term}")


@bot.command(name='@', help='do the thing')
@commands.before_invoke(record_usage)
async def at(ctx, arg0=None, num=1):
    if ctx.author.id in ADMIN:
        if num not in range(5):
            num = 1
            await ctx.send(f"Don't be a dick, <@!{ctx.author.id}>")
        if arg0 == "@everyone":
            for i in range(num):
                await ctx.send('@everyone', delete_after=0.5)
                return
        (id, good) = getIdFromAt(arg0)
        if good:
            await ctx.message.delete()
            for i in range(num):
                await ctx.send(f'<@!{id}>', delete_after=0.5)
    else:
        await ctx.send(randresponse(nope))
        await ctx.send("Must be an admin to annoy")


@bot.command(name='kickjosh', help="you sunovabitch")
@commands.before_invoke(record_usage)
@is_owner()
async def kickjosh(ctx):
    guild = bot.get_guild(638163732463222786)
    josh = guild.get_member(JRN)
    await kick(ctx, f"<@{JRN}>")
    try:
        await josh.kick()
    except:
        await ctx.send("You got lucky, punk")


@bot.command(name='newpasta', help='Save a new pasta')
@commands.before_invoke(record_usage)
async def newpasta(ctx, *, args):
    savePasta(ctx.author.id, args)
    response = 'Saved pasta for {}'.format(ctx.author.name)
    await ctx.send(response)

annoys=["dododobobobobgjubgjubgjubdododobobobobgjubgjubgjub",
"lurl lurl lurl lurl",
"My sprinkler goes like thisstststststststststststststststststststststststst and comes back like titttttttttttttttttttttttttttttttttttttte",
"@@@@@@@@@@@@@@@@@@@@@@@@@@",
"anununununununununununaunauanuanaunauanaunauanuanaunauanaunauanaunauanaunauanaunauanaunauanaunaaunauanuananuannuannuannua",
"My ROFLCopter goes soi soi soi soi soi soi soi soi soi soi",
"A rofl Train goes tichdvdxtche tichdvdxtche tichdvdxtche tichdvdxtche tichdvdxtche wuuu wuuu wuuu tichdvdxtche tichdvdxtche",
"The ting goes skrrrahh, pap pap ka-ka-ka Skidiki-pap-pap, and a puu-puu-poudrrr-boom Skiya, du-du-ku-ku-doom doom Poom poom, you dun now"]

@bot.command(name='annoyjosh', help='oops, sorry')
@is_owner()
async def annoyjosh(ctx):
    await ctx.send(f"<@{JRN}>", delete_after=0.5)
    await asyncio.sleep(5)

    for i in range(1):
        await ctx.send(randresponse(annoys), tts=True)


bot.run(TOKEN)
