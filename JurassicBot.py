import discord
from discord.ext import commands


class JurassicBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def start(self, *args, **kwargs):
        await super().start(*args, **kwargs)

    async def close(self):
        await super().close()

cogs = [
    "cogs.functions"
]

client = JurassicBot(command_prefix="!",
                     case_insensitive=True,
                     intents=discord.Intents.all(),
                     activity=discord.Activity(type=discord.ActivityType.watching,
                                               name="over your servers"),
                     status=discord.Status.online)
