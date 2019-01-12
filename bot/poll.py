# encoding: utf-8
from telegram.ext import (CommandHandler, Filters, ConversationHandler, MessageHandler)
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import utils.logger as logger
import psycopg2
import requests
from configurations import bot_config

NAME, DESCRIPTION, QUESTION, ANSWERS, NEXT_QUESTION = range(5)

VOTING = {}
MULTIPLE_QUESTION = False
CURRENT_QUESTION = ""

def poll(bot,update):
     global VOTING
     global MULTIPLE_QUESTION
     global CURRENT_QUESTION
     VOTING = {}
     MULTIPLE_QUESTION = False
     CURRENT_QUESTION = ""
     logger.get_logger().info("Name of poll: %s", update.message.text)
     update.message.reply_text('Vas a crear una nueva votación. En primer lugar, indica el nombre de la misma :)')

     return NAME

def set_name(bot,update):
     global VOTING
     VOTING['name'] = update.message.text

     logger.get_logger().info("Name of poll: %s", update.message.text)
     update.message.reply_text('¡De acuerdo! A continuación, indica la descripción 🌈')

     return DESCRIPTION

def set_description(bot,update):
     global VOTING
     VOTING['desc'] = update.message.text
     logger.get_logger().info("Description of poll: %s", update.message.text)
     update.message.reply_text('Ahora tienes que añadir las preguntas de tu encuesta. ¿Cuál es la primera pregunta?')

     logger.get_logger().info(VOTING)
     return QUESTION

def set_question(bot,update):
     global VOTING
     global CURRENT_QUESTION

     if MULTIPLE_QUESTION == False:
          VOTING['question'] = update.message.text
     else:
          CURRENT_QUESTION = update.message.text
          VOTING["questions"].append({"desc": update.message.text, "options": []})
     update.message.reply_text('A continuación, indica las respuestas separadas por saltos de línea. Por ejemplo:\nRespuesta 1 \nRespuesta 2')

     logger.get_logger().info(VOTING)
     return ANSWERS

def set_answers(bot,update):
     global VOTING
     global CURRENT_QUESTION
     reply_keyboard = [['Sí', 'No']]
     options = []
     for i in update.message.text.split("\n"):
          options.append(i)

     if MULTIPLE_QUESTION == False:     
          VOTING['question_opt'] = options
     else:
          for i in VOTING["questions"]:
               if i["desc"] == CURRENT_QUESTION:
                    for o in options:
                         i["options"].append({"option": o})
                    break;
     
     print(VOTING)
     update.message.reply_text('La pregunta se ha guardado. ¿Quieres crear otra?',
     reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

     return NEXT_QUESTION 

def set_next_question(bot, update):
     global VOTING
     global MULTIPLE_QUESTION
     next_state = ConversationHandler.END

     if(update.message.text == 'Sí'):
          next_state = QUESTION

          if MULTIPLE_QUESTION == False:
               MULTIPLE_QUESTION = True
               VOTING["multiple"] = True
               VOTING["questions"] = []
               options = []

               for option in VOTING['question_opt']:
                    options.append({"option": option})
               VOTING["questions"].append({"desc":VOTING['question'], "options": options})
               del VOTING["question"]
               del VOTING["question_opt"]
          update.message.reply_text('¡De acuerdo! ¿Cuál es la nueva pregunta?')
     else:
          token = get_token(update.message.chat_id)
          response = save_poll(token)
          
          if response.status_code == 201:
               update.message.reply_text('¡Nos vemos! 🐼')
          else:
               update.message.reply_text('Error al crear la votación, inténtalo de nuevo')
              
     return next_state

def save_poll(token):
     global VOTING
     headers = {"Authorization": "Token " + token}
     print(token)
     r = requests.post(bot_config.API_ENDPOINT + "voting/", json=VOTING, headers=headers)
     print(VOTING)
     print(r)
     return r
    
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
          entry_points=[CommandHandler('poll', poll)],

          states={
               NAME: [MessageHandler(Filters.text, set_name)],
              
               DESCRIPTION: [MessageHandler(Filters.text, set_description)],

               QUESTION: [MessageHandler(Filters.text, set_question)],
               
               ANSWERS: [MessageHandler(Filters.text, set_answers)],
               
               NEXT_QUESTION: [MessageHandler(Filters.text, set_next_question)],
          },

          fallbacks=[CommandHandler('cancel', cancel)]
     )
     dispatcher.add_handler(conv_handler)