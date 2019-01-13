# encoding: utf-8
from telegram.ext import (CommandHandler, Filters, ConversationHandler, MessageHandler)
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import utils.logger as logger
import psycopg2
import requests
from configurations import bot_config
# import sys
import json
import js2py
# sys.path.append('../assets/crypto')
# import elgamal

SELECT_VOTING, VOTE = range(2)
USER_VOTE = {}
USER_VOTINGS = []
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

     USER_VOTINGS = []
     SELECTED_VOTING = {}
     USER_TOKEN = ""
     try:
          token = get_token(update.message.chat_id)
          data["token"] = token
          USER_TOKEN = token
          user = requests.post(bot_config.API_ENDPOINT + "authentication/getuser/", data)
          user_id = json.loads(user.text)["id"]
          USER_VOTE["voter"] = user_id
          r = requests.get(bot_config.API_ENDPOINT + "census/voter/" + str(user_id))
          all_votings = json.loads(r.text)

          print(all_votings)
          for voting in all_votings:
               print(voting)
               if voting["start_date"] is not None and voting["end_date"] is None: # Select open polls
                    USER_VOTINGS.append(voting)

          if len(USER_VOTINGS) > 0:
               for v in USER_VOTINGS:
                    reply_options.append("Nombre: " + v["name"] + ", Identificador: " + str(v["id"]))
                    reply_keyboard.append(reply_options)
                    NEXT_STATE = SELECT_VOTING

               update.message.reply_text('Escoge la votación en la que quieres votar 🦄',
               reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
          else:
               update.message.reply_text('No hay votaciones en las que puedes votar.')
     except Exception as e:
          print(e)
          update.message.reply_text('Tienes que iniciar sesión para poder votar.')          

     return NEXT_STATE

def set_voting_id(bot,update):
     global USER_VOTE
     global SELECTED_VOTING
     NEXT_STATE = VOTE
     options = []
     USER_VOTE["voting"] = int(update.message.text.split("Identificador: ")[1])

     for v in USER_VOTINGS:
          if v["id"] == USER_VOTE["voting"]:
               voting = v
               SELECTED_VOTING = v

     print(v)
     if len(v["questions"]) == 0:
          NEXT_STATE = ConversationHandler.END
          update.message.reply_text("No hay preguntas para esta votación aún.")
     else:
          for q in v["questions"]:
               question = q["desc"]
               for o in q["options"]:
                    options.append(o["option"])
               reply_keyboard = [options]
          update.message.reply_text(question,
               reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

     return NEXT_STATE

def set_vote(bot,update):
     global SELECTED_VOTING
     global USER_VOTE
     global USER_TOKEN
     global USER_VOTINGS
     
     # js2py.translate_file('bot\crypto\elgamal.js', 'elgamal.py')
     # js2py.translate_file('bot\crypto\sjcl.js', 'sjcl.py')
     # js2py.translate_file('bot\crypto\\bigint.js', 'bigint.py')
     # from elgamal import elgamal
     # from sjcl import sjcl
     # sjcl =  js2py.require("sjcl");
     # from bigint import bigint
     # print(sjcl.random.randomWords(2, 0))

     for q in SELECTED_VOTING["questions"]:
          for o in q["options"]:
               answer_id = update.message.text
               if o["option"] == answer_id:
                    # bigmsg = BigInt.fromJSONObject(o["option"]);
                    # print(bigmsg)
                    # cipher = elgamal.ElGamal.encrypt(SELECTED_VOTING["pub_key"], 2)
                    # print(cipher)
                    USER_VOTE["vote"] = {"a":str(o["option"]), "b":str(o["option"])}

     print(USER_VOTE)
     print(USER_TOKEN)

     # Send data 
     headers = {"Authorization": "Token " + USER_TOKEN,
                "Content-Type": "application/json"}
     r = requests.post(bot_config.API_ENDPOINT + "store/", json=USER_VOTE, headers = headers)
     print(r.text)
     print(r.status_code)
     if r.status_code == 201 or r.status_code == 200:
          update.message.reply_text("Tu voto se ha enviado ✨")
     else:
          USER_VOTINGS = []
          update.message.reply_text("Hubo un error enviando el voto, inténtalo de nuevo.")

     return ConversationHandler.END

# def encrypt(option):
#      bigmsg = option ** 10
#      pk = SELECTED_VOTING["pub_key"]

#      q = 2**256
#      q1 = q - 1
#      bit_length = q1.bit_length()
#      rw = RandomWords()
#      random = rw.random_words(count=bit_length)
#      rand_bi = hex(int('10000011101000011010100010010111', 16))

#      return { alpha: alpha, beta: beta };

def get_token(chat_id):    
     conn = psycopg2.connect(dbname='dbug2e1mgmcjr9',
            user='tplmohpmvjmlaz',
            password='f9beee7b53c2358efa9e31cb5f02ebd052915955b106f56ab28b4401ef9891af',
            host='ec2-54-75-230-41.eu-west-1.compute.amazonaws.com',
            port=5432
            )

     cur = conn.cursor()
     cur.execute("SELECT token from user_token where username = (SELECT username FROM user_chat WHERE last_connection = (SELECT MAX(last_connection) FROM user_chat) AND chat_id =" + str(chat_id) + ");")

     token = cur.fetchone()[0]

     cur.close()
     conn.close()

     return token

def cancel(bot, update):
     global USER_VOTINGS
     global USER_VOTE
     global USER_TOKEN

     USER_VOTINGS = []
     SELECTED_VOTING = {}
     USER_TOKEN = ""

     update.message.reply_text('La votación se ha cancelado 🌾')

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