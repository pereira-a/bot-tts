from nextcord.ext.commands import Cog
from bot import Bot
from nextcord import Interaction, slash_command, Embed
from .channel import join_channel
from config import *
from tts.monster import *

class TTS(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.monster = MonsterTTS()

    @slash_command(name='tts', description='Generate text to speach in channel', guild_ids=GUILD_IDS)
    async def tts(self, int: Interaction, text: str):
        self.bot.logger.debug("TTS command called")
        #await join_channel(int)
        await int.send(content="Transmitting text to speach: \"" + text + "\"", tts=True)
        try:
            await int.send(self.monster.generate(text))
        except Exception as e:
            self.bot.logger.critical("Failure while generating TTS")
            self.bot.logger.exception(e)
            embed = Embed(
                title="Error",
                description="Failed to generate TTS. Please try again later.",
                color=0xFF0000  # Red color
            )
            await int.send(embed=embed)

        
def setup(bot: Bot):
    bot.add_cog(TTS(bot))