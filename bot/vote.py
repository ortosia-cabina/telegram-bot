# encoding: utf-8
from telegram.ext import (CommandHandler, Filters, ConversationHandler, MessageHandler)
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import utils.logger as logger
import psycopg2
import requests
from configurations import bot_config
import json

SELECT_VOTING, VOTE = range(2)

USER_VOTE = {}

def vote(bot,update):
     data = {}
     reply_keyboard = []
     reply_options = []
     NEXT_STATE = ConversationHandler.END

     try:
          token = get_token(update.message.chat_id)
          data["token"] = token
          user = requests.post(bot_config.API_ENDPOINT + "authentication/getuser/", data)
          user_id = json.loads(user.text)["id"]
          r = requests.get(bot_config.API_ENDPOINT + "census/voter/" + str(user_id))
          votings = json.loads(r.text)

          for v in votings:
               reply_options.append("Nombre: " + v["name"] + ", Identificador: " + str(v["id"]))
               print(reply_options)

          reply_keyboard.append(reply_options)
          print(reply_keyboard)
          NEXT_STATE = SELECT_VOTING

          update.message.reply_text('Escoge la votación en la que quieres votar.',
          reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
     except:
          update.message.reply_text('Tienes que iniciar sesión para poder votar.')          
     

     return NEXT_STATE

def set_vote(bot,update):
     global VOTING
     VOTING['desc'] = update.message.text
     logger.get_logger().info("Description of poll: %s", update.message.text)
     update.message.reply_text('Ahora tienes que añadir las preguntas de tu encuesta. ¿Cuál es la primera pregunta?')

     logger.get_logger().info(VOTING)
     return ConversationHandler.END

def get_token(chat_id):    
#     conn = psycopg2.connect(dbname='d3i8n8a3vv0nst',
#             user='qzxvwbjdcmhnsy',
#             password='39cb3668dfac02f210f27e0d813167519ccf63309560bca7f93d2d79be46f308',
#             host='ec2-54-246-85-234.eu-west-1.compute.amazonaws.com',
#             port=5432
#             )
     conn = psycopg2.connect(dbname='telegram',
               user='telegram',
               password='telegram',
               port=5432
     )

     cur = conn.cursor()
     cur.execute("SELECT token from user_token where username = (SELECT username FROM user_chat WHERE last_connection = (SELECT MAX(last_connection) FROM user_chat) AND chat_id =" + str(chat_id) + ");")

     token = cur.fetchone()[0]

     cur.close()
     conn.close()

     return token

def cancel(bot, update):
     update.message.reply_text('La creación de la votación se ha cancelado :(')

     return ConversationHandler.END

def main(dispatcher):
     conv_handler = ConversationHandler(
          entry_points=[CommandHandler('vote', vote)],

          states={
               SELECT_VOTING: [MessageHandler(Filters.text, set_voting_id)],
              
               VOTE: [MessageHandler(Filters.text, set_vote)],

          },

          fallbacks=[CommandHandler('cancel', cancel)]
     )
     dispatcher.add_handler(conv_handler)