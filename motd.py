import discord
from discord.ext import commands
import requests
import random
import os
import logging

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True

# Create a bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

# GBIF API parameters
GBIF_ENDPOINT = "https://api.gbif.org/v1/occurrence/search"
GBIF_PARAMS = dict(mediaType="StillImage", taxonKey="797", limit=100)


def get_random_moth():
    """Get a random moth from the GBIF API.
    Returns a tuple of the moth name and image URL."""
    try:
        # Make a request to the GBIF API
        response = requests.get(GBIF_ENDPOINT, params=GBIF_PARAMS)
        response.raise_for_status()  # Raise an exception for HTTP error codes
        results = response.json().get('results', [])
        if not results:
            logging.error("No results found in GBIF database.")
            return None, None

        # Randomly select one of the results with an image
        valid_results = [result for result in results if 'media' in result and result['media']]
        if not valid_results:
            logging.error("No valid images found in the results.")
            return None, None

        selected_moth = random.choice(valid_results)
        moth_name = selected_moth['scientificName']
        moth_image_url = selected_moth['media'][0]['identifier']  # Assuming the first media entry is the image

        return moth_name, moth_image_url
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None, None


async def send_moth_of_the_day():
    """Send the moth of the day to the Discord channel.
    This function is called when the bot is ready."""
    channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))
    channel = bot.get_channel(channel_id)

    # Get a random moth from the GBIF API
    moth_name, moth_image_url = get_random_moth()
    if moth_name and moth_image_url:
        # Send the moth of the day as an embed
        embed = discord.Embed(title="Moth of the Day", description=moth_name)
        embed.set_image(url=moth_image_url)
        await channel.send(embed=embed)
    else:
        await channel.send("Could not retrieve the Moth of the Day. Please try again later.")


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await send_moth_of_the_day()  # Send the moth of the day when the bot is ready
    await bot.close() # Close the bot after sending the moth of the day


bot.run(os.getenv('DISCORD_BOT_TOKEN'))
