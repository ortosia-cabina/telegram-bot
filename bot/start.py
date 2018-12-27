# encoding: utf-8
from telegram.ext import CommandHandler

def main(dispatcher):
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="""Soy el bot de Decide-Ortosia :) \n ¡Utiliza /help para saber más!""")