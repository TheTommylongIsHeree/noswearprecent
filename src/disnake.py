import disnake
from disnake.ext import commands
from . import logger, check

class Bot(commands.InteractionBot):
    def __init__(self, **kwargs):
        intents = disnake.Intents.default()
        intents.message_content = True
        super().__init__(
            intents=intents,
            **kwargs
        )

    async def on_ready(self):
        logger.info("bot ready.")
        
    async def on_message(self, message):
        if not message.author.bot and message.guild:
            logger.info(f"msg from {message.author}: {message.content}")
            await message.reply(f"{await check(message.content)}")

    @commands.slash_command(description="Sends the bot's latency.")
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"Pong! Latency is {round(self.latency * 1000)}ms")