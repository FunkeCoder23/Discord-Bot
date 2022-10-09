from discord.ext import commands
from random import randint
import re
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class RPG(commands.Cog, name="RPG Helper"):
    DICE_RE = re.compile(
        "(\d*)([D|d]\d*)((?:[+*-](?:\d+|\([A-Z]*\)))*)(?:\+(D\d*))?")
    SIMPLE_RE = re.compile("(\d*)[Dd](\d*)(?:([+*-])(\d+))?")

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="roll", help="Roll [#]d#[±#]")
    async def roll(self, ctx, *, args=None):
        dice_roll = self.SIMPLE_RE.match(args)
        rolls = dice_roll.groups("1")
        if not rolls:
            return await ctx.send(f"{args} is not in the valid format #d#±#")

        detailed_rolls = False
        full_roll = dice_roll.string
        num_dice = int(rolls[0])
        die_size = int(rolls[1])
        operation = rolls[2]
        modifier = int(rolls[3])
        dice_string = ""

        if (num_dice+die_size+modifier) > 3e4:
            return await ctx.send("Nice try :triumph:")
            
        for num in (num_dice, die_size, modifier):
            if num == 420 or num == 69:
                dice_string += "Nice!\n"

        detailed_rolls = num_dice <= 12
        total_roll = 0
        log.debug(
            f"{full_roll} {num_dice} D {die_size} {operation} {modifier}")

        for i in range(num_dice):
            roll = randint(1, die_size)
            if detailed_rolls:
                roll_string = f"[{i+1}] Rolled a {roll}\n"
                log.debug(roll_string)
                dice_string += roll_string
            total_roll += roll

        modified = operation != "1"
        if not modified:
            pass
        elif operation == "*":
            operation = "\*"
            mod_roll = total_roll * modifier
        elif operation == "+":
            mod_roll = total_roll + modifier
        elif operation == "-":
            mod_roll = total_roll - modifier

        name = ctx.author.nick if ctx.author.nick else ctx.author.name
        dice_string += f"{name} rolled {num_dice}d{die_size}: {total_roll}"
        if modified:
            dice_string += f" with {operation}{modifier} modifier: {mod_roll}"

        await ctx.send(dice_string)


async def setup(bot):
    await bot.add_cog(RPG(bot))
