#!/usr/bin/env python3

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from token_generator import generate_token

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Please use /token to request token.')

def send_token(update, context):
    """Send a message when the command /token is issued."""
    # Set user pin for stoken
    user_pin = "000000"
    # Pass pin to generate_token and return token result
    generated_token = generate_token(pin=user_pin)
    # Build token message
    message = "Your token is: " + generated_token + "."
    # Send token
    update.message.reply_text(message)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    # Put the telegram bot token here
    updater = Updater("123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    # command answer for /start
    dp.add_handler(CommandHandler("start", start))
    # command answer for /token
    dp.add_handler(CommandHandler("token", send_token))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
