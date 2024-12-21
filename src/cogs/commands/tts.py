from nextcord.ext.commands import Cog
from bot import Bot
from nextcord import Interaction, slash_command, Embed
from .channel import join_channel
from config import *
from tts.monster import *
import nextcord

class TTS(Cog):
    def __init__(self, bot):
        self.bot = bot
        # Create a dictionary of TTS providers to allow multiple providers integrations in the future
        self.tts_provieders = {
            "monster": MonsterTTS()
        }

    @slash_command(name="tts", description="TTS command", guild_ids=GUILD_IDS)
    async def tts(self, interaction: Interaction):
        pass    # Will never be called, just here to show the structure of a command

    @tts.subcommand(name='generate', description='Generate text to speach in channel')
    async def generate(self, int: Interaction, text: str, provider: str, voice_id: str):
        await join_channel(int)
        await int.send(content="TTS is being generated... Your message is: \"" + text + "\"")
        try:
            if provider not in self.tts_provieders:
                self.sendError("Invalid provider. Please try again.")
            self.tts_provieders[provider].generate(text, voice_id)
            await self.play(int, "tts-audio.mp3")
        except Exception as e:
            self.bot.logger.critical("Failure while generating TTS")
            self.bot.logger.exception(e)
            self.sendError("Failed to generate TTS. Please try again later.")
        
    @tts.subcommand(name='providers', description='List available TTS providers')
    async def providers(self, int: Interaction):
        provider_list = ""
        for provider in self.tts_provieders.keys():
            provider_list += str(provider) + "\n"
        embed = Embed(
            title="Available TTS Providers",
            description=provider_list,
        )
        await int.send(embed=embed)

    async def play(self, interaction: Interaction, sound_file: str):
         vc = interaction.guild.voice_client
         if vc.is_connected():
            if os.path.isfile("./" + sound_file):
                print("File exists")
                print("vc", str(vc))
                vc.play(nextcord.FFmpegPCMAudio(source=sound_file), after=lambda e: print(f'Finished playing: {e}'))
    
    def clean_up_after_play(vc):
       print("Cleaning up")

    async def sendError(msg: str):
        embed = Embed(
            title="Error",
            description=msg,
            color=0xFF0000  # Red color
        )
        await int.send(embed=embed)

        
def setup(bot: Bot):
    bot.add_cog(TTS(bot))