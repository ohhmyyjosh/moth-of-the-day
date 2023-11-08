# Moth of the Day Discord Bot

This Discord bot uses the GBIF API to fetch a random moth with an image and posts it to a specified Discord channel as the "Moth of the Day".

## Features

- Fetches a random moth image and its scientific name from the GBIF (Global Biodiversity Information Facility) API.
- Posts the moth image and name to the configured Discord channel daily.

## Setup

To run this bot, you need to have Python 3.11 installed along with the `requests` and `discord.py` packages. The bot uses environment variables for configuration to keep sensitive information like the bot token and channel ID secure.

### Environment Variables

- `DISCORD_BOT_TOKEN`: Your Discord bot token which you can get from the Discord developer portal.
- `DISCORD_CHANNEL_ID`: The ID of the Discord channel where you want to post the moth images.

### Installing Dependencies

Install the required packages using pip:

```bash
python -m pip install --upgrade pip
pip install requests discord.py
```

## Usage
To run the bot locally, set the environment variables and execute the bot script:
```bash
export DISCORD_BOT_TOKEN='your_bot_token_here'
export DISCORD_CHANNEL_ID='your_channel_id_here'
python bot.py
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

### License
This project is licensed under the MIT License. See LICENSE for more details.