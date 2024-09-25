from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '8028581214:AAFrZz_Jqr_pwQQ_nXZXIVBjZPJ-Mx7hJn4'
BOT_USERNAME: Final = '@ISK_SHEPOT_BOT'


# Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is bot for sending anonymous messages')


async def write_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Write the message to the channel')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('You can add this bot to your channel to have better expierence sending anonymous messages.')


async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat.id
    print(chat_id)
    await update.message.reply_text(f'Your chat ID is: {chat_id}')

async def get_username(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    username = user.username if user.username else "No username set"
    await update.message.reply_text(f'Your username is: {username}')

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Forward the received message to the specified chat
    await context.bot.forward_message(chat_id=1002384512914, from_chat_id=get_chat_id, message_id=update.message.message_id)


# Message Handler

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type #says the type of chat
    user = update.message.from_user
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"  username: {user}')