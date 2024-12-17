from nextcord.ext.commands import Cog
from bot import Bot
from nextcord import Interaction, slash_command
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
        await int.send("Transmitting text to speach: \"" + text + "\"")
        await int.send(self.monster.generate(text))
        
def setup(bot: Bot):
    bot.add_cog(TTS(bot))