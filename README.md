# Moth of the Day Discord Bot

This Discord bot uses the [GBIF API](https://www.gbif.org/developer/summary) to fetch a random moth occurrence with an image and posts it to a specified Discord channel as the "Moth of the Day". While the current implementation focuses on moths, it's possible to adapt the bot for a "Plant of the Day", "Bird of the Day", or any other organism that is cataloged in the GBIF's vast database.

## About GBIF

The Global Biodiversity Information Facility (GBIF) is an international network and data infrastructure funded by the world's governments and aimed at providing access to data about all types of life on Earth. It serves as a rich resource for scientific research and conservation efforts. More information about GBIF and how to use its API can be found on their [developer resources page](https://www.gbif.org/developer/summary).

## Features

- Fetches random moth images and scientific names from GBIF.
- Configurable for other "of the Day" features.
- Daily posts to a Discord channel using automated scheduling.
## Setup

To run this bot, you need to have Python 3.11 installed along with the `requests` and `discord.py` packages. The bot uses environment variables for configuration to keep sensitive information like the bot token and channel ID secure.

### Environment Variables

- `DISCORD_BOT_TOKEN`: Your Discord bot token which you can get from the Discord developer portal.
- `DISCORD_CHANNEL_ID`: The ID of the Discord channel where you want to post the moth images.

### Installing Dependencies

Install the required packages using pip:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Usage
To run the bot locally, set the environment variables and execute the bot script:
```bash
export DISCORD_BOT_TOKEN='your_bot_token_here'
export DISCORD_CHANNEL_ID='your_channel_id_here'
python motd.py
```

### GitHub Actions Automation
This project is configured to use GitHub Actions to automatically run the bot script every day at 11 PM UTC.

The workflow is defined in .github/workflows/motd_bot.yml and includes steps to checkout the code, set up Python, install dependencies, and execute the script with the necessary environment variables provided via GitHub secrets.

### Setting GitHub Secrets
1. Go to your repository on GitHub.
2. Click on "Settings" and then "Secrets".
3. Add DISCORD_BOT_TOKEN and DISCORD_CHANNEL_ID as new secrets.

### Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.
I want to encourage people to add other "of the Day" features to this bot. If you do, please let me know so I can link to your project here.

### License
This project is licensed under the MIT License. See LICENSE for more details.