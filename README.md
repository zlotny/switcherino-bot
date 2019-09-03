# Golden Sun Hype Bot
Golden Sun Hype Bot is a Telegram bot made in Python 3 to send a particular message into a conversation. 

Based on [BeetlerBot](https://github.com/agnovoa2/BeetlerBot), this bot send a message with an image and a footnote to as a reply to every message containing a series of keywords.

## Setting up
```bash
# Install pyTelegramBotAPI
pip install pyTelegramBotAPI

# Clone the project
git clone https://github.com/zlotny/golden-sun-hype-bot

# Enter the project folder
cd golden-sun-hype-bot

# Ensure your python version is 3
python --version
```

## Running the software - Standalone
```bash
# If your default python version is 3
python main.py

# If it is not
python3 main.py
```

## Running the software - Docker
Just build the docker image with a tag you like. For example:

```bash

docker build -t golden-sun-hype-bot .

```

And then run it with something like:

```bash

docker run -d --restart=always --name golden-sun-hype-bot golden-sun-hype-bot

```

Golden Sun Hype Bot uses [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) to work.
