import logging
from os import system
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    system("python ./test.py")


if __name__ == '__main__':
    application = ApplicationBuilder().token('5597939827:AAFDtDFC7DlZvOVpso_elznxLUP1m5UL0MY').build()

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    start_handler = CommandHandler('start', start)
    test_handler = CommandHandler('test', test)
    application.add_handler(start_handler)
    application.add_handler(test_handler)


    application.run_polling()