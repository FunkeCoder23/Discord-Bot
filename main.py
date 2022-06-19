from bot import TheBot
import logging
from logging.handlers import RotatingFileHandler
import asyncio
import contextlib


class RemoveNoise(logging.Filter):
    def __init__(self):
        super().__init__(name='discord.state')

    def filter(self, record):
        if record.levelname == 'WARNING' and 'referencing an unknown' in record.msg:
            return False
        return True
        
@contextlib.contextmanager
def setup_logging():
    log = logging.getLogger()

    try:
        #__enter__
        max_bytes = 32 * 1024 * 1024  # 32 MiB
        logging.getLogger('discord').setLevel(logging.INFO)
        logging.getLogger('discord.http').setLevel(logging.WARNING)
        logging.getLogger('discord.state').addFilter(RemoveNoise())

        log.setLevel(logging.INFO)
        handler = RotatingFileHandler(filename='thebot.log',
                                      encoding='utf-8',
                                      mode='w',
                                      maxBytes=max_bytes,
                                      backupCount=5)
        dt_fmt = '%Y-%m-%d %H:%M:%S'
        fmt = logging.Formatter(
            '[{asctime}] [{levelname:<7}] {name}: {message}',
            dt_fmt,
            style='{')
        handler.setFormatter(fmt)
        log.addHandler(handler)

        yield
    finally:
        #__exit__
        handlers = log.handlers[:]
        for hdlr in handlers:
            hdlr.close()
            log.removeHandler(hdlr)


def main():
    """Launches the bot."""
    with setup_logging():
        asyncio.run(run_bot())


async def run_bot():
    log = logging.getLogger()
    kwargs = {
        'command_timeout': 60,
        'max_size': 20,
        'min_size': 20,
    }

    bot = TheBot()
    await bot.start()


if __name__ == '__main__':
    main()
