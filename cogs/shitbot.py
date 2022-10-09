import discord
import asyncio
from discord.ext.commands.core import is_owner
from uwuify import uwu
from discord.ext import commands
from time import time
from datetime import datetime
from random import randint
from cogs.utils import *
import re

import logging

log = logging.getLogger(__name__)

uid = re.compile('[0-9]+')


class ShitBot(commands.Cog, name="Shit meme bot"):
    def __init__(self, bot):
        self.bot = bot

    async def record_usage(self, ctx):
        t = datetime.fromtimestamp(time()).strftime('%I:%M:%S %p')
        print(t, ":", ctx.author, 'used', ctx.command)

    def emojify(self, text):
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

    def sarcastify(self, text):
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

    def clapbackify(self, text):
        newText = ":clap: "
        for i in text:
            if i == ' ':
                newText += " :clap: "
            else:
                newText += i.upper()
        newText += " :clap:"
        return newText

    def prand(self, min, max):
        global lastrand
        rand = randint(min, max)
        if (max - min) > len(lastrand):
            while rand in lastrand:
                rand = randint(min, max)
        lastrand.append(rand)
        if len(lastrand) > 3:
            lastrand.pop(0)
        return rand

    def randresponse(self, links):
        rand = self.prand(0, len(links) - 1)
        return links[rand]

    def check_role(self, roles, name):
        for role in roles:
            if name == role.name:
                return True
        return False

    @commands.command(name='Roles', command_prefix='$')
    @is_owner()
    @commands.before_invoke(record_usage)
    async def create_roles(self, ctx):
        guild = ctx.guild
        # print(guild)
        # print(guild.roles)
        for role in SD_Emoji.values():
            if not self.check_role(guild.roles, role):
                await guild.create_role(name=role, mentionable=True)
        for role in Color_Emoji.values():
            if not self.check_role(guild.roles, role[0]):
                await guild.create_role(name=role[0], color=role[1])
        for role in EE_Emoji.values():
            if not self.check_role(guild.roles, role):
                await guild.create_role(name=role, mentionable=True)
        for role in CPE_Emoji.values():
            if not self.check_role(guild.roles, role):
                await guild.create_role(name=role, mentionable=True)
        for role in CS_Emoji.values():
            if not self.check_role(guild.roles, role):
                await guild.create_role(name=role, mentionable=True)

    @commands.command(name='SD', command_prefix='$')
    @is_owner()
    @commands.before_invoke(record_usage)
    async def add_SD_Emojis(self, ctx):
        chan = ctx.channel
        msg = discord.PartialMessage(id=SDMSG, channel=chan)
        for emoji in SD_Emoji:
            await msg.add_reaction(emoji)

    @commands.command(name='Colors', command_prefix='$')
    @is_owner()
    @commands.before_invoke(record_usage)
    async def add_Color_Emojis(self, ctx):
        chan = ctx.channel
        msg = discord.PartialMessage(id=COLORMSG, channel=chan)
        for emoji in Color_Emoji:
            await msg.add_reaction(emoji)

    @commands.command(name='EE', command_prefix='$')
    @is_owner()
    @commands.before_invoke(record_usage)
    async def add_EE_Emojis(self, ctx):
        chan = ctx.channel
        msg = discord.PartialMessage(id=EEMSG, channel=chan)
        for emoji in EE_Emoji:
            await msg.add_reaction(emoji)

    @commands.command(name='CPE', command_prefix='$')
    @is_owner()
    @commands.before_invoke(record_usage)
    async def add_CPE_Emojis(self, ctx):
        chan = ctx.channel
        msg = discord.PartialMessage(id=EEMSG, channel=chan)
        for emoji in CPE_Emoji:
            await msg.add_reaction(emoji)

    @commands.command(name='WELCOME', command_prefix='$')
    @is_owner()
    @commands.before_invoke(record_usage)
    async def add_welcome_Emojis(self, ctx):
        chan = ctx.channel
        msg = discord.PartialMessage(id=WELCOME, channel=chan)
        await msg.add_reaction('✅')

    @commands.command(name='CS', command_prefix='$')
    @is_owner()
    @commands.before_invoke(record_usage)
    async def add_CS_Emojis(self, ctx):
        chan = ctx.channel
        msg = discord.PartialMessage(id=CSMSG, channel=chan)
        for emoji in CS_Emoji:
            await msg.add_reaction(emoji)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        member = payload.member
        if member.bot:
            return
        emoji = str(payload.emoji)
        msg = payload.message_id
        message = await self.bot.get_channel(payload.channel_id
                                             ).fetch_message(payload.message_id
                                                             )
        if msg == WELCOME:
            if emoji == '✅':
                role = discord.utils.get(member.guild.roles, name='Initiated')
                await member.add_roles(role)
                role = discord.utils.get(member.guild.roles,
                                         name='Uninitiated')
                await member.remove_roles(role)
        if msg == CSMSG:
            if emoji in CS_Emoji:
                role = discord.utils.get(member.guild.roles,
                                         name=CS_Emoji[emoji])
                await member.add_roles(role)
            else:
                await message.remove_reaction(emoji, member)
        elif msg == CPEMSG:
            if emoji in CPE_Emoji:
                role = discord.utils.get(member.guild.roles,
                                         name=CPE_Emoji[emoji])
                await member.add_roles(role)
            else:
                await message.remove_reaction(emoji, member)
        elif msg == EEMSG:
            if emoji in EE_Emoji:
                role = discord.utils.get(member.guild.roles,
                                         name=EE_Emoji[emoji])
                await member.add_roles(role)
            else:
                await message.remove_reaction(emoji, member)
        elif msg == SDMSG:
            if emoji in SD_Emoji:
                role = discord.utils.get(member.guild.roles,
                                         name=SD_Emoji[emoji])
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

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        guild = self.bot.get_guild(id=payload.guild_id)
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

    @commands.command(name='emojify', help='Emojify text')
    @commands.before_invoke(record_usage)
    async def emoji(self, ctx, *, arg):
        response = self.emojify(arg)
        r = []
        while len(response) >= 2000:
            s = response.rfind('⠀', 0, 2000)
            res = response[:s]
            response = response[s + 1:]
            r.append(res)
        r.append(response)
        for res in r:
            await ctx.send(res)

    @commands.command(name='clapback',
                      help=':clap: YOU :clap: ALREADY :clap: KNOW')
    @commands.before_invoke(record_usage)
    async def clapback(self, ctx, *, arg):
        await ctx.send(self.clapbackify(arg))

    @commands.command(name='sarcastify', help='SaRcaStiFy tExT')
    @commands.before_invoke(record_usage)
    async def sarcastic(self, ctx, *, arg):
        await ctx.send(self.sarcastify(arg))

    @commands.command(name='hi-vinnie', help='@\'s vinnie')
    @commands.before_invoke(record_usage)
    async def atvinnie(self, ctx):
        response = '<@!{}>'.format(VG)
        await ctx.send(response)

    @commands.command(name='flashbang', help='Think fast chucklenuts')
    @commands.before_invoke(record_usage)
    async def flashbang(self, ctx):
        response = '<@!{}>'.format(VG)
        await ctx.send(response)
        await ctx.send(file=discord.File(r'vids/thinkfast.mp4'))

    @commands.command(name='uwuify', help='You already know')
    @commands.before_invoke(record_usage)
    async def uwuify(self, ctx, *, args):
        await ctx.send(uwu(args))

    @commands.command(name='test', help='Test shit out')
    @commands.before_invoke(record_usage)
    async def echo(self, ctx, *, name):
        msg = ctx.message
        await msg.delete()
        await ctx.send(name)

    @commands.command(name='say')
    @commands.before_invoke(record_usage)
    @is_owner()
    async def repeat(self, ctx, *, text):
        channel = self.bot.get_channel(CHAT)
        await channel.send(text)

    @commands.command(name='kick', help='Kick something')
    @commands.before_invoke(record_usage)
    async def kick(self, ctx, args=None):
        if args is None:
            args = f"<@!{ctx.author.id}>"
            response = "Unsure who to kick"
            await ctx.send(response)
            await ctx.send(f"Kicking {args} instead")
        response = self.randresponse(kicks)
        await ctx.send(args + " has been kicked. ")
        await ctx.send(response)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, id=798949146055934053)
        await member.add_roles(role)

    @commands.command(name='owner', help="Display self.bot owner")
    @commands.before_invoke(record_usage)
    async def owner(self, ctx):
        auth = ctx.message.author.id
        print(auth)
        if auth == JRN:
            response = "Just kidding... fuck off, Josh"
            await ctx.send(f"<@!{JRN}> created me")
            await asyncio.sleep(5)
        elif auth == ADT:
            response = "You made me, master"
        else:
            response = "<@!{}> created me".format(ADT)
        await ctx.send(response)

    @commands.command(name='hug', help="Sends a hug")
    @commands.before_invoke(record_usage)
    async def hugA(self, ctx, *, args=None):
        response = self.randresponse(hugs)
        if (args != None):
            await ctx.send(args)
        await ctx.send(response)

    def loadPasta(self, id):
        pastas = []
        print(f"In loadpasta, id is {id}")
        try:
            with open(f'pastas/{id}', 'r') as pf:
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
            # raise
            return pastas
        except:
            print(f"Could not find pasta at ./pastas/{id}")
            return None

    def savePasta(self, pasta, spaghet):
        spaghet = "".join(spaghet)
        print(spaghet)

        with open('./pastas/' + str(pasta), 'a') as pf:
            pf.write(spaghet)
            pf.write("\n\n")
        pf.close()

    def parseArgs(self, args):
        num = None
        mods = []
        if args:
            for i in range(len(args)):
                if args[i].isnumeric():
                    num = int(args[i])
                else:
                    mods.append(args[i])
        return (num, mods)

    def getIdFromAt(self, username):
        print(username)
        id = re.findall(uid, username)
        if id:
            print(id)
            return id[0]
        else:
            print(f"No good ID: {username}")
            return None

    @commands.command(name='mimic', help='Muahaha')
    @is_owner()
    async def mimic(self, ctx, u, *, txt="Hello", d=True):
        if d:
            await ctx.message.delete()
        if u.isnumeric():
            id = int(u)
            print(id)
        else:
            id = self.getIdFromAt(u)
        if not id:
            await ctx.send(self.randresponse(nope) + "")
            return
        user = self.bot.get_user(int(id))
        if user is None:
            await ctx.send(self.randresponse(nope) + "")
            return
        hook = await ctx.channel.create_webhook(name="mimic")
        name = ctx.message.guild.get_member(int(id))
        if name:
            nick = name.nick
        else:
            nick = user.name
        await hook.send(txt, username=nick, avatar_url=user.avatar_url)
        asyncio.sleep(1)
        await hook.delete()

    @commands.command(name='timer', help='We\'ll see about that')
    @commands.before_invoke(record_usage)
    async def timer(self, ctx, amt=0, unit=None, name="<@0>", *, txt):
        id = self.getIdFromAt(name)
        t = amt
        if not id:
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

    @commands.command(name='pasta',
                      help="""!pasta @user [num] [-e, -s, -u]
        Sends a user's copypasta
        args:
            num to select
        modifiers:
            -e emojify 
            -s sarcastify 
            -u uwuify""")
    @commands.before_invoke(record_usage)
    async def pasta(self, ctx, user=None, *args):
        (num, mods) = self.parseArgs(args)
        if user is None:
            id = ctx.author.id
            print(f"from no name pasta:{id}")
        else:
            id = self.getIdFromAt(user)
            print(f"from name pasta: {id}")

        if not id:
            await ctx.send(
                self.randresponse(nope) + f", {user} is a bad username")
            return
        CP = self.loadPasta(int(id))
        if CP is None:
            await ctx.send(
                self.randresponse(nope) + f", user {user} not found")
            return

        e, s, u = False, False, False
        for mod in mods:
            e = (mod in EMOJIFY) or e
            s = (mod in SARCASTIFY) or s
            u = (mod in UWUIFY) or u

        i = randint(0, len(CP) - 1)

        if num is not None:
            i = num
        cp = CP[i % len(CP)]
        id = f'<@!{id}>'
        pasta = ''
        for line in cp:

            if s:
                line = self.sarcastify(line)
            if e:
                line = self.emojify(line)
            if u:
                line = uwu(line)
            pasta += line + '\n'
        print(pasta)
        await self.mimic(ctx, id, txt=pasta, d=False)

    @commands.command(name='vinniepasta',
                      help="""!vinniepasta [num] [-e, -s, -u]
        Sends a vinnie copypasta
        args:
            num to select
        modifiers:
            -e emojify 
            -s sarcastify 
            -u uwuify""")
    @commands.before_invoke(record_usage)
    async def vinniepastaa(self, ctx, *args):
        await self.pasta(ctx, f'<@!{VG}>', *args)

    @commands.command(name='shitpasta',
                      help="""!shitpasta [num] [-e, -s, -u]
        Sends a bodenshit copypasta
        args:
            num to select
        modifiers:
            -e emojify 
            -s sarcastify 
            -u uwuify""")
    @commands.before_invoke(record_usage)
    async def shitpasta(self, ctx, *args):
        await self.pasta(ctx, f'<@!{JB}>', *args)

    @commands.command(name='lmgtfy', help='... search it yourself')
    @commands.before_invoke(record_usage)
    async def lmgtfy(self, ctx, *, args):
        txt = args.split(' ')
        term = "+".join(txt)
        await ctx.send(f"https://googlethatforyou.com/?q={term}")

    @commands.command(name='ud', help='search urban dictionary')
    @commands.before_invoke(record_usage)
    async def ud(self, ctx, *, args):
        txt = args.split(' ')
        term = "+".join(txt)
        await ctx.send(
            f"https://www.urbandictionary.com/define.php?term={term}")

    @commands.command(name='wiki', help='search wikipedia')
    @commands.before_invoke(record_usage)
    async def wiki(self, ctx, *, args):
        txt = args.split(' ')
        term = "+".join(txt)
        await ctx.send(f"https://en.wikipedia.org/w/index.php?search={term}")

    @commands.command(name='@', help='do the thing')
    @commands.before_invoke(record_usage)
    async def at(self, ctx, user=None, times=1):
        if ctx.author.id in ADMIN:
            if times not in range(6):
                times = 1
                await ctx.send(f"Don't be a dick, <@!{ctx.author.id}>")
            if user == "everyone":
                for i in range(times):
                    await ctx.send('@everyone', delete_after=0.5)
                    return
            id = self.getIdFromAt(user)
            if id:
                await ctx.message.delete()
                for i in range(times):
                    await ctx.send(f'<@!{id}>', delete_after=0.5)
        else:
            await ctx.send(self.randresponse(nope))
            await ctx.send("Must be an admin to annoy")

    @commands.command(name='kickjosh', help="you sunovabitch")
    @commands.before_invoke(record_usage)
    @is_owner()
    async def kickjosh(self, ctx):
        guild = self.bot.get_guild(638163732463222786)
        josh = guild.get_member(JRN)
        await self.kick(ctx, f"<@!{JRN}>")
        try:
            await josh.kick()
        except:
            await ctx.send("You got lucky, punk")

    @commands.command(name='newpasta', help='Save a new pasta')
    @commands.before_invoke(record_usage)
    async def newpasta(self, ctx, *, args):
        print(ctx.author.id)
        self.savePasta(ctx.author.id, args)
        response = 'Saved pasta for {}'.format(ctx.author.name)
        await ctx.send(response)

    @commands.command(name='annoyjosh', help='oops, sorry')
    @is_owner()
    async def annoyjosh(self, ctx):
        await ctx.send(f"<@!{JRN}>", delete_after=0.5)
        await asyncio.sleep(5)

        for i in range(1):
            await ctx.send(self.randresponse(annoys), tts=True)


async def setup(bot):
    await bot.add_cog(ShitBot(bot))
