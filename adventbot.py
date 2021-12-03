# commands.py
import json
from ratelimit import limits
from ratelimit import RateLimitException
import requests
from discord.ext import commands
from discord import Embed, Emoji
from time import time, timezone
from datetime import datetime
from dateutil import tz

NYC = tz.gettz('America/New_York')


class Advent(commands.Cog, name="Advent of Code"):
    async def record_usage(self, ctx):
        t = datetime.fromtimestamp(time()).strftime('%I:%M:%S %p')
        print(t, ":", ctx.author, 'used', ctx.command)

    def __init__(self, bot):
        self.current_time = time()
        self.updated = datetime.fromtimestamp(
            self.current_time, NYC).strftime('%I:%M:%S %p')
        self.nextupdate = datetime.fromtimestamp(
            900 + self.current_time, NYC).strftime('%I:%M:%S %p')
        with open('secrets.json', 'r') as f:
            secrets = json.load(f)
            global TOKEN, GUILD, sessionID
            self.token = secrets["TOKEN"]
            self.guild = secrets["GUILD"]
            self.sessionID = secrets["sessionID"]
        self.leaderboardID = 974092
        self.adventurl = "https://adventofcode.com/2021"
        self.url = f"{self.adventurl}/leaderboard/private/view/{self.leaderboardID}.json"
        self.cookies = dict(session=self.sessionID)
        self.commands = commands

        self.bot = bot

    #     self.setup()

    # def setup(self):
    #     self.bot.add_command()

    def extract_score(self, json):
        try:
            return (int(json['local_score']))
        except KeyError:
            return 0

    def extract_stars(self, json):
        try:
            return (int(json['stars']))
        except KeyError:
            return 0

    @limits(calls=1, period=900)
    def update_json(self):
        print("Updated")
        self.current_time = time()
        r = requests.get(self.url, cookies=self.cookies)
        global data
        data = r.json()
        with open('../data.json', 'w') as f:
            json.dump(data, f)
        with open('../last_update', 'w') as f:
            f.write(str(self.current_time))

    def update_json_local(self):
        print("Updated from cache")
        try:
            f = open('../last_update', 'r')
            self.current_time = float(f.read())
        except:
            self.update_json()
        global data
        try:
            f = open('../data.json', 'r')
            data = json.load(f)
        except:
            self.update_json()

    def update(self):
        self.updated = datetime.fromtimestamp(
            self.current_time, NYC).strftime('%I:%M:%S %p')
        self.nextupdate = datetime.fromtimestamp(
            900 + self.current_time, NYC).strftime('%I:%M:%S %p')
        if (time() - self.current_time > 900):
            self.update_json()
        else:
            self.update_json_local()

    @commands.command(name='score', help="Get score of user")
    @commands.before_invoke(record_usage)
    async def score(self, ctx, *, name):
        self.update()
        members = data["members"]
        name_num = 0
        for member_num in members:
            if members[member_num]["name"] == name:
                name_num = member_num
                break
        if (name_num == 0):
            await ctx.send(name + " not found in leaderboard. 😑")
            return
        score = members[name_num]["local_score"]
        levels = members[name_num]["completion_day_level"]
        embed = Embed(title="{}\n{} Points".format(name, score),
                      color=0x990000)
        embed.set_author(name="Advent of Code Leaderboard")
        for day in range(1, 26):
            if str(day) in levels:
                stars = "2" if "2" in levels[str(day)] else "1"
                value = "⭐⭐\n" if stars == "2" else "⭐\n"
                value += datetime.fromtimestamp(
                    int(levels[str(day)][stars]["get_star_ts"])).strftime(
                        '%b %d\n %I:%M %p')
                embed.add_field(name="Day " + str(day),
                                value=value,
                                inline=True)

        embed.set_footer(text="Updated at " + self.updated +
                         "\nNext update available at " + self.nextupdate)
        await ctx.send(embed=embed)

    @commands.command(
        name='join',
        help='Shows information on how to join the Advent of Code Leaderboard')
    @commands.before_invoke(record_usage)
    async def join_us(self, ctx):
        embed = Embed(title="Join the Leaderboard",
                      url=self.adventurl,
                      description="Leaderboard Code: 974092-d0365788",
                      color=0x226d1c)
        embed.set_author(name="Advent of Code Leaderboard",
                         icon_url="https://i.imgur.com/Jlp3GB8.png")
        embed.set_thumbnail(url="https://i.stack.imgur.com/ArhPo.gif")
        await ctx.send(embed=embed)

    @commands.command(name='day',
                      help="Get the rankings (time) for individual days")
    @commands.before_invoke(record_usage)
    async def day(self, ctx, day=None):
        max_day = 0
        if (day == None):
            await ctx.send("usage: !day <day>")
            return

        embed = Embed(title="Day " + day + " Leaderboard", color=0x9a8623)
        embed.set_author(name="Advent of Code Leaderboard",
                         icon_url="https://i.imgur.com/Jlp3GB8.png")
        embed.set_thumbnail(url="https://i.stack.imgur.com/ArhPo.gif")
        self.update()

        part1 = {}
        part2 = {}
        members = data["members"]
        for member in members:
            if members[member]["name"] == None:
                name = "Anonymous #" + members[member]["id"]
            else:
                name = members[member]["name"]
            levels = members[member]["completion_day_level"]
            if day in levels:
                max_day = day
                for part in levels[day]:
                    # print(levels[day][part])
                    if part == '1':
                        part1.update({name: levels[day][part]["get_star_ts"]})
                    if part == '2':
                        part2.update({name: levels[day][part]["get_star_ts"]})
        if max_day == 0:
            await ctx.send("No data available for day " + day)
            return
        part1 = dict(sorted(part1.items(), key=lambda item: item[1]))
        part2 = dict(sorted(part2.items(), key=lambda item: item[1]))

        response = ""
        place = 0
        for name in part1:
            place += 1
            response += str(place)+'. ' + name + '\n⠀' + \
                datetime.fromtimestamp(int(part1[name]), NYC).strftime(
                    '%m/%d %I:%M:%S %p') + '\n'
        embed.add_field(name="Part 1", value=response, inline=True)

        response = ""
        place = 0
        for name in part2:
            place += 1
            response += str(place)+'. ' + name + '\n⠀' + \
                datetime.fromtimestamp(int(part2[name]), NYC).strftime(
                    '%m/%d %I:%M:%S %p') + '\n'

        embed.add_field(name="Part 2", value=response, inline=True)
        embed.set_footer(text="Updated at " + self.updated +
                         "\nNext update available at " + self.nextupdate)
        await ctx.send(embed=embed)

    @commands.command(name='leaderboard',
                      help='Show the Advent of Code Top 10')
    @commands.before_invoke(record_usage)
    async def board(self, ctx, top10=True):
        embed = Embed(title="Join the Leaderboard",
                      url=self.adventurl,
                      description="Leaderboard Code: 974092-d0365788",
                      color=0x226d1c)
        embed.set_author(name="Advent of Code Leaderboard",
                         icon_url="https://i.imgur.com/Jlp3GB8.png")
        embed.set_thumbnail(url="https://i.stack.imgur.com/ArhPo.gif")
        lines = []
        self.update()
        members = data["members"]
        i = 0

        for member_num in members:
            lines.append(members[member_num])
        lines.sort(key=self.extract_score, reverse=True)
        lines.sort(key=self.extract_stars, reverse=True)

        for leader in lines:
            i += 1
            if (top10 and i > 10):
                break
            if leader["name"] == None:
                name = "Anonymous #" + str(leader["id"]) + " "
            else:
                name = str(leader["name"]) + "  "
            if (i == 1):
                name += "<:platinum:752979216592797836>"
            elif (i == 2):
                name += "<:gold:752979203078619186>"
            elif (i == 3):
                name += "<:silver:752979184367698041>"

            response = "‎‎⠀" + str(leader["stars"]) + " ⭐ | "
            response += str(leader["local_score"]) + str(" points")
            response += "!" if (leader["local_score"] != 0
                                ) else " <:sunglass_cry:757783574232694906>"
            embed.add_field(name=str(i) + ". " + name,
                            value=response,
                            inline=False)
        embed.set_footer(text="Updated at " + self.updated +
                         "\nNext update available at " + self.nextupdate)
        await ctx.send(embed=embed)

    @commands.command(name='all',
                      help='Show the full Advent of Code Leaderboard')
    @commands.before_invoke(record_usage)
    async def fullboard(self, ctx):
        await self.board(ctx, top10=False)
