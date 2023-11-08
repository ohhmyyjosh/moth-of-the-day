# Moth of the Day Discord Bot

This Discord bot uses the [GBIF API](https://www.gbif.org/developer/summary) to fetch a random moth occurrence with an image and posts it to a specified Discord channel as the "Moth of the Day". While the current implementation focuses on moths, it's possible to adapt the bot for a "Plant of the Day", "Bird of the Day", or any other organism that is cataloged in the GBIF's vast database.

## About GBIF

The Global Biodiversity Information Facility (GBIF) is an international network and data infrastructure funded by the world's governments and aimed at providing access to data about all types of life on Earth. It serves as a rich resource for scientific research and conservation efforts. More information about GBIF and how to use its API can be found on their [developer resources page](https://www.gbif.org/developer/summary).

## Features

- Fetches random moth images and scientific names from GBIF.
- Configurable for other "of the Day" features.
- Daily posts to a Discord channel using automated scheduling.
- 
## Setup

To run this bot, you need to have Python 3.11 installed along with the `requests` and `discord.py` packages. The bot uses environment variables for configuration to keep sensitive information like the bot token and channel ID secure.

### Discord Bot Setup Instructions
Before running your "Moth of the Day" Discord bot, you'll need to set up a Discord application and bot, and then invite it to your server. Here's how you can do it:

**Creating a Discord Application**
1. Go to the [Discord Developer Portal](https://discord.com/build/app-developers).
2. Click on the "New Application" button.
3. Give your application a name and confirm the creation.
4. Navigate to the "Bot" tab and click on "Add Bot".
5. Here, you can set the bot's name and profile picture.

**Getting Your Discord Bot Token**
1. Under the bot's settings, you will find the token under the "TOKEN" section.
2. Click "Copy" to copy your bot token and save it securely. You'll use this token as the DISCORD_BOT_TOKEN environment variable.
3. Inviting Your Bot to a Server
4. In the application's settings, navigate to the "OAuth2" tab.
5. Under "Scopes," select "bot" to generate an invite link.
6. In the "Bot Permissions" section, select the permissions your bot will need. For this aplication you will need 'Send Messages' and 'Embed Links' permissions.
7. Copy the generated link and open it in your browser.
8. Choose the server to invite your bot to and confirm.
Make sure you have the required permissions on the Discord server to add a bot.

**Adding the Bot to Your Channel**
To ensure that your bot operates correctly within your designated channel:

- The bot must have permission to view the channel where it will post the moth images.
- The bot must also have permission to send messages and embed links in that channel.
- Once you have completed these steps, your bot should be fully set up and operational within your Discord server. Follow the rest of the setup instructions to get your "Moth of the Day" bot running and configured with the environment variables.

*Never share your bot token with anyone or publish it in a public place.*
*Always use environment variables or secure app configuration services to handle tokens and other sensitive data.*

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
