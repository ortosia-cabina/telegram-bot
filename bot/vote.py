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
USER_VOTINGS = {}
SELECTED_VOTING = {}
USER_TOKEN = ""

def vote(bot,update):
     data = {}
     reply_keyboard = []
     reply_options = []
     NEXT_STATE = ConversationHandler.END
     global USER_VOTINGS
     global USER_VOTE
     global USER_TOKEN
     try:
          token = get_token(update.message.chat_id)
          data["token"] = token
          USER_TOKEN = token
          user = requests.post(bot_config.API_ENDPOINT + "authentication/getuser/", data)
          user_id = json.loads(user.text)["id"]
          USER_VOTE["voter"] = user_id
          r = requests.get(bot_config.API_ENDPOINT + "census/voter/" + str(user_id))
          votings = json.loads(r.text)
          USER_VOTINGS = votings

          for v in votings:
               reply_options.append("Nombre: " + v["name"] + ", Identificador: " + str(v["id"]))

          reply_keyboard.append(reply_options)
          NEXT_STATE = SELECT_VOTING

          update.message.reply_text('Escoge la votación en la que quieres votar.',
          reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
     except:
          update.message.reply_text('Tienes que iniciar sesión para poder votar.')          
     

     return NEXT_STATE

def set_voting_id(bot,update):
     global USER_VOTE
     global SELECTED_VOTING
     options = []
     USER_VOTE["voting"] = int(update.message.text.split("Identificador: ")[1])

     for v in USER_VOTINGS:
          if v["id"] == USER_VOTE["voting"]:
               voting = v
               SELECTED_VOTING = v


     for q in v["questions"]:
          for o in q["options"]:
               options.append(o["option"])

     reply_keyboard = [options]
     update.message.reply_text(q["desc"],
     reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

     return VOTE

def set_vote(bot,update):
     global SELECTED_VOTING
     global USER_VOTE
     global USER_TOKEN

     for q in SELECTED_VOTING["questions"]:
          for o in q["options"]:
               answer_id = update.message.text
               if o["option"] == answer_id:
                    USER_VOTE["vote"] = {"a":1, "b":1}

     print(USER_VOTE)

     # Send data 
     headers = {"Authorization": "Token " + USER_TOKEN}
     r = requests.post(bot_config.API_ENDPOINT + "store/", USER_VOTE, headers = headers)
     print(r.text)
     if r.status_code == 201 or r.status_code == 200:
          update.message.reply_text("Tu voto se ha enviado")
     else:
          update.message.reply_text("Hubo un error enviando el voto, inténtalo de nuevo.")

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