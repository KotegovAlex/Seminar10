import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from commands import *

TOKEN = '5630119738:AAE1fSRlZKFqHRTflJMsjcXUG9mvtbA6bgw'
bot = telegram.Bot(token=TOKEN)
print(bot.get_me())

updater = Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('weather', weather))

updater.dispatcher.add_handler(CommandHandler('help', help))

print('server start')
updater.start_polling()
updater.idle()