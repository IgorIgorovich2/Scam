import logging
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

"""
Constants for the Telegram bot token and username.

The `TOKEN` constant holds the API token for the Telegram bot, which is required for the bot to authenticate and communicate with the Telegram API.

The `BOT_USERNAME` constant holds the username of the Telegram bot, which is used to identify the bot in Telegram conversations.
"""
TOKEN: Final = '8028581214:AAFrZz_Jqr_pwQQ_nXZXIVBjZPJ-Mx7hJn4'
BOT_USERNAME: Final = '@ISK_SHEPOT_BOT'
CHANNEL_ID = -1002384512914

# List to store usernames
usernames_list = []

# Configure logging
logging.basicConfig(
    filename='bot.log',  # Log file name
    filemode='a',        # Append mode
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,    # Log level
    encoding='utf-8'      # Set encoding to UTF-8
)

# Commands
"""
Handles the /start command, which sends a message explaining the purpose of the bot.
"""


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is bot for sending anonymous messages')


"""
Handles the /write command, which prompts the user to write a message to be sent to the channel.
"""


async def write_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Write the message to the channel')


"""
Handles the /help command, which provides information about how to use the bot.
"""


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'You can add this bot to your channel to have better expierence sending anonymous messages.')


"""
Handles the /id command, which sends the user's chat ID.
"""


async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat.id
    print(chat_id)
    await update.message.reply_text(f'Your chat ID is: {chat_id}')


"""
Handles the /username command, which sends the user's username.
"""


async def get_username(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    username = user.username if user.username else "No username set"
    await update.message.reply_text(f'Your username is: {username}')


"""
Forwards the received message to the specified chat.
"""


async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.forward_message(chat_id=-1002384512914, from_chat_id=6714766716,
                                      message_id=update.message.message_id)


async def copy_and_send_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Check if the message is from a private chat
    if update.message.chat.type == 'private':
        # Get the text from the incoming message
        message_text = update.message.text

        # Send the copied text to the specified chat
        await context.bot.send_message(
            chat_id=-1002384512914,
            text=message_text
        )

    # Get the username (if available)

    username = update.message.from_user.username or "No username"

    # Log the message text and username

    logging.info(f'Received message: "{message_text}" from {username} (Chat ID: {update.message.chat.id})')

    # Add the username to the list if not already present

    if username not in usernames_list:
        usernames_list.append(username)


# Responses

"""
Handles the response to a message that contains the word "негр" (Russian for "n*****"). This function is used to filter out inappropriate language in messages.

Args:
    text (str): The message text to be processed.

Returns:
    str: The processed message text, which will be "bad boy, sent it" if the original message contained the word "негр".
"""


def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'негр' in processed:
        return 'bad boy, sent it'


# Message Handler

"""
Handles the processing of incoming messages, including determining the message type and user information.

Args:
    update (Update): The Telegram update object containing the message.
    context (ContextTypes.DEFAULT_TYPE): The context object for the update.

Returns:
    None
"""


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type  # says the type of chat
    user = update.message.from_user
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"  username: {user}')

    """
    Handles the response to a message based on the message type and content.

    If the message is in a group chat and mentions the bot, the bot will remove its own username from the message text and process the response using the `handle_response` function. If the message does not mention the bot, the function will return without doing anything.

    If the message is in a private chat, the bot will simply process the response using the `handle_response` function.

    The processed response is then printed to the console and sent back to the user.

    Args:
        update (Update): The Telegram update object containing the message.
        context (ContextTypes.DEFAULT_TYPE): The context object for the update.
    """
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'Update {update} caused error {context.error}')


"""
Initializes the Telegram bot application and sets up the handlers for various commands and message types.

The bot is configured with the following:
- Handlers for the /start, /write, /help, and /id commands
- A handler for forwarding all messages
- An error handler to log any errors that occur

The bot is then started and polls for incoming messages.
"""
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('write', write_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler("id", get_chat_id))  # Command to get chat ID

    # Messages
    app.add_handler(MessageHandler(filters.ALL, copy_and_send_message))

    # Errors
    app.add_error_handler(error_handler)

    # polls the bot
    print('Waiting for messages')
    app.run_polling(poll_interval=3)