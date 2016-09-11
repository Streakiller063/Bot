from telegram.ext import Updater
updater = Updater(token='264752864:AAEN9egRenApcM5l7yGifFLHKTCv4qahbZM')
dispatcher = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
def start(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
#echo_handler = MessageHandler([Filters.text], echo)
#dispatcher.add_handler(echo_handler)

from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Siapa',
            input_message_content=InputTextMessageContent(query.upper())
            
            )
        )
    bot.answerInlineQuery(update.inline_query.id, results)
    bot.sendMessage(chat_id=update.message.chat_id, text="Hello, Albert emg oon ")

from telegram.ext import InlineQueryHandler
inline_caps_handler=InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Gw ga ngerti lu ngapain dah")
    unknown_handler = MessageHandler([Filters.command], unknown)
    dispatcher.add_handler(unknown_handler)

#updater.start_polling()

updater.stop()
