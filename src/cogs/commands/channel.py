from discord import User
from nextcord.ext.commands import Cog
from bot import Bot
from config import *
from nextcord import Interaction, slash_command

class ChannelCommands(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="channel", description="Channel command", guild_ids=GUILD_IDS)
    async def channel(self, interaction: Interaction):
        pass    # Will never be called, just here to show the structure of a command

    @channel.subcommand(name="join", description="Join a channel")
    async def join(self, interaction: Interaction):
        user: User = interaction.user
        
        if user.voice is None:
            await interaction.send("You are not in a voice channel.")
            return
        
        channel = user.voice.channel

        if interaction.guild.voice_client is not None:
            await interaction.guild.voice_client.move_to(channel)
        else:
            await channel.connect()

        await interaction.send(f"Joined {channel.name}")
    
    @channel.subcommand(name="disconnect", description="Disconnect from the voice channel")
    async def disconnect(self, interaction: Interaction):
        if interaction.guild.voice_client is None:
            await interaction.send("I'm not in a voice channel.")
            return
        
        await interaction.guild.voice_client.disconnect()
        await interaction.send("Disconnected")

def setup(bot: Bot):
    bot.add_cog(ChannelCommands(bot))