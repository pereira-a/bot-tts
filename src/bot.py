import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file


DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
TESTING_GUILD_ID = int(os.getenv('TESTING_GUILD_ID'))

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello with dotenv!")

bot.run(DISCORD_TOKEN)