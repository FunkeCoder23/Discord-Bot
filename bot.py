from __future__ import annotations
from os import environ as config
import discord
from random import seed
from discord.ext import commands
# from cogs.utils.config import Config
# from cogs.utils.context import Context
import logging
import traceback
import aiohttp
import sys
from cogs.utils import *
# from typing import TYPE_CHECKING, Any, AsyncIterator, Iterable, Optional, Union
from collections import Counter, defaultdict

# import config

# Set up Intents
# bot = Bot(command_prefix='!', intents=intents)
initial_extensions = [
    "cogs.admin",
    "cogs.advent",
    "cogs.music",
    "cogs.shitbot",
]

description = """
This is THE Bot. I do shit. Don't ask questions.
"""

log = logging.getLogger(__name__)



class TheBot(commands.Bot):

    __TOKEN = config["TOKEN"]
    
    user: discord.ClientUser
    command_stats: Counter[str]
    socket_stats: Counter[str]
    bot_app_info: discord.AppInfo

    blacklist=[JDR]
    
    def __init__(self):
        seed()
        allowed_mentions = discord.AllowedMentions(roles=True,
                                                   everyone=True,
                                                   users=True)
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="!",
            description=description,
            pm_help=None,
            help_attrs=dict(hidden=True),
            chunk_guilds_at_startup=False,
            heartbeat_timeout=180.0,
            allowed_mentions=allowed_mentions,
            intents=intents,
            enable_debug_events=True,
        )

    async def setup_hook(self):
        self.session = aiohttp.ClientSession()

        self.bot_app_info = await self.application_info()
        self.owner_id = self.bot_app_info.owner.id

        for extension in initial_extensions:
            try:
                await self.load_extension(extension)
            except:
                print(f'Failed to load extension {extension}.',
                      file=sys.stderr)
                traceback.print_exc()
                raise
                
    @property
    def owner(self) -> discord.User:
        return self.bot_app_info.owner

    async def on_ready(self):
        if not hasattr(self, 'uptime'):
            self.uptime = discord.utils.utcnow()

        print(f'Ready: {self.user} (ID: {self.user.id})')
    
    async def get_context(self, origin):
        return await super().get_context(origin)
        
    async def process_commands(self, message: discord.Message):
        ctx = await self.get_context(message)

        if ctx.command is None:
            return

        if ctx.author.id in self.blacklist:
            await ctx.send("yeah but then I'd have to talk to you and that's the worst")
            return

        # if ctx.guild is not None and ctx.guild.id in self.blacklist:
            # return

        # bucket = self.spam_control.get_bucket(message)
        # current = message.created_at.timestamp()
        # retry_after = bucket.update_rate_limit(current)
        # author_id = message.author.id
        # if retry_after and author_id != self.owner_id:
        #     self._auto_spam_count[author_id] += 1
        #     if self._auto_spam_count[author_id] >= 5:
        #         await self.add_to_blacklist(author_id)
        #         del self._auto_spam_count[author_id]
        #         await self.log_spammer(ctx, message, retry_after, autoblock=True)
        #     else:
        #         await self.log_spammer(ctx, message, retry_after)
        #     return
        # else:
            # self._auto_spam_count.pop(author_id, None)

        await self.invoke(ctx)


    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return
        await self.process_commands(message)

    async def on_guild_join(self, guild: discord.Guild) -> None:
        if guild.id in self.blacklist:
            await guild.leave()

    async def close(self) -> None:
        await super().close()
        await self.session.close()

    async def start(self) -> None:
        await super().start(self.__TOKEN, reconnect=True)