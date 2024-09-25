# Overview

This is a simple Telegram bot designed for sending anonymous messages. 
The bot allows users to interact with it through various commands, 
providing a straightforward interface for sending and managing messages.

# Features
* /start: Introduces the bot and its purpose.
* /write: Prompts the user to write a message to be sent to the channel.
* /help: Provides instructions on how to use the bot.
* /id: Returns the user's chat ID.
* /username: Returns the user's username.
* Message Filtering: Filters out inappropriate language from incoming messages.
* Message Forwarding: Forwards messages to a specified chat.

# Installation

To run this bot, you need to have Python installed along with 
the python-telegram-bot library. You can install the required
library using pip:

```
pip install python-telegram-bot
```

# Configuration

Before running the bot, you need to configure the 
following constants in the code:

* TOKEN: Your bot's API token from the BotFather.
* BOT_USERNAME: The username of your bot, prefixed with '@'.

```
TOKEN: Final = 'YOUR_BOT_TOKEN_HERE'
BOT_USERNAME: Final = '@YOUR_BOT_USERNAME_HERE'
```

# Usage

1. Clone or download the repository.
2. Open the file and set your bot's token and username.
3. Run the script:
```
python your_bot_script.py
```
4. Interact with your bot on Telegram by sending commands.

# Commands 

* /start: "This is a bot for sending anonymous messages."
* /write: "Write the message to the channel."
* /help: "You can add this bot to your channel to have a better experience sending anonymous messages."
* /id: Returns your chat ID.
* /username: Returns your username.

# Message Handling

The bot handles incoming messages and responds based on the context:


* In group chats, it checks if the bot is mentioned and processes the message accordingly.
* In private chats, it directly processes the message.

The bot also filters out messages containing inappropriate language.

# Error Handling

Any errors that occur during the operation of the bot are logged for troubleshooting.

---

Enjoy using your Telegram bot!