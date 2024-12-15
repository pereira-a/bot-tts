from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Guild to test commands
GUILD_IDS = [int(guild_id) for guild_id in os.getenv('TESTING_GUILD_IDS', '').split(',') if guild_id]

# The cogs you don't want to load
LOAD_EXCEPTIONS = []

# The directory where your cogs are located
COGS_DIR = "cogs"

# Whether or not the bot should automatically reload cogs when a change is made
AUTO_RELOAD = True