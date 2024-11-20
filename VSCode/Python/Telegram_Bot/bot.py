import logging, requests
import pandas as pd
from typing import Final
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Application, ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from uuid import uuid4

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN: Final = '7390660096:AAHPAsKqqIWAp9CFI1Mg3xZb2uy29e1-aRY'
BOT_USERNAME: Final = '@page_pal_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hallo! I am PagePal!")

async def book_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Type in the genre to start.")

async def preview_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Type in the book name to preview.")

async def list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Type in the book name which you want to add or delete.")

async def reading_list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Manage your reading list or view it.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="/start - Welcome message\n/book - Enter genre\n/preview - Enter book name to preview\n/list - Enter book to add or remove\n/reading_list - Add, remove or view your reading list\n/help - List of commands")


async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=str(uuid4()),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


def main():
    application = ApplicationBuilder().token('7390660096:AAHPAsKqqIWAp9CFI1Mg3xZb2uy29e1-aRY').build()
    
    start_handler = CommandHandler('start', start_command)
    application.add_handler(start_handler)

    book_handler = CommandHandler('book', book_command)

    preview_handler = CommandHandler('preview', preview_command)

    list_handler = CommandHandler('list', list_command)

    reading_list_handler = CommandHandler('reading_list', reading_list_command)

    help_handler = CommandHandler('help', help_command)

    
    application.add_handler(start_handler)
    application.add_handler(book_handler)
    application.add_handler(preview_handler)
    application.add_handler(list_handler)
    application.add_handler(reading_list_handler)
    application.add_handler(help_handler)
    
    inline_caps_handler = InlineQueryHandler(inline_caps)
    application.add_handler(inline_caps_handler)

    # Other handlers
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)

    application.run_polling()

if __name__ == '__main__':
    main()