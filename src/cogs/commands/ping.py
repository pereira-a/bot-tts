from nextcord.ext.commands import Cog
from nextcord import Interaction, slash_command
from bot import Bot
from config import *

class PingCommand(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Ping command", force_global=True, dm_permission=True, guild_ids=GUILD_IDS)
    async def ping(self, interaction: Interaction):
        await interaction.send(f"Pong! {self.bot.latency * 1000:.2f}ms")


def setup(bot: Bot):
    bot.add_cog(PingCommand(bot))