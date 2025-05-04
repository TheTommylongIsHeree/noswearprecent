import discord
from discord.commands import slash_command
from . import logger, WordChecker

checker = WordChecker()

class Bot(discord.Bot):
    def __init__(self, **kwargs):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(
            # debug_guilds = [1360512592308600944],
            intents = intents,
            **kwargs
        )

    async def on_ready(self):
        logger.info("bot ready.")
        
    async def on_message(self, message):
        if not message.author.bot and message.guild:
            logger.info(f"msg from {message.author}: {message.content}")
            await message.reply(f"{await checker.check_phrase(message.content)}")

    @slash_command(description="Sends the bot's latency.", guild_ids=[1360512592308600944])
    async def ping(self, ctx):
        await ctx.respond(f"Pong! Latency is {round(self.latency * 1000)}ms")