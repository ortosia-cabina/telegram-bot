# encoding: utf-8
from telegram.ext import (CommandHandler, Filters, ConversationHandler, MessageHandler)
import os
import psycopg2
import requests
import json
import datetime
from configurations import bot_config

STORE = range(1)

def main(dispatcher):
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('login', login)],

        states={
            STORE: [MessageHandler(Filters.text, store_token)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )
    
    dispatcher.add_handler(conv_handler)
    
def login(bot, update):
    update.message.reply_text("Para logearte, indica tu nombre de usuario y tu contraseña de la siguiente forma. \nUsername \nContraseña")
    
    return STORE 

def cancel(bot, update):
    update.message.reply_text('El inicio de sesión se ha cancelado :(')

    return ConversationHandler.END

def get_token(credentials):
    headers = {"Content-type": "application/json",
        "Accept": "text/plain"}
    r = requests.post(bot_config.API_ENDPOINT + "authentication/login/", credentials)
    
    return r
    
def store_token(bot,update):
    credentials = {}
    next_state = ConversationHandler.END
    for index, i in enumerate(update.message.text.split("\n")):
        if index == 0:
            credentials["username"] = i
        else:
            credentials["password"] = i
    
    print(credentials)
    response = get_token(credentials)
    print(response.status_code)
    print(response.text)
    if response.status_code == 200:
        user = save_token(credentials['username'], json.loads(response.text)["token"], update.message.chat_id)

        if user:
            update.message.reply_text("¡Ya has iniciado sesión, " + user + "!")
        else:
            update.message.reply_text("Se han guardado tus credenciales 🌚")
    else:
        update.message.reply_text("Los credenciales son incorrectos, índicalos o escribe /cancel para salir")
        next_state = STORE
        
    return next_state

def save_token(username, token, chat_id):
    conn = psycopg2.connect(dbname='dbug2e1mgmcjr9',
            user='tplmohpmvjmlaz',
            password='f9beee7b53c2358efa9e31cb5f02ebd052915955b106f56ab28b4401ef9891af',
            host='ec2-54-75-230-41.eu-west-1.compute.amazonaws.com',
            port=5432
            )
     
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user_token (username text PRIMARY KEY, token text);")
    cur.execute("CREATE TABLE IF NOT EXISTS user_chat (username text REFERENCES user_token(username), chat_id integer, last_connection timestamp);")

    # Store tables if wasn't created
    conn.commit()
    user = None

    try:
        cur.execute("SELECT * FROM user_chat WHERE username = %s AND chat_id = %s", (username, chat_id))
        user = cur.fetchone()[0];
    except:
        cur.execute("INSERT INTO user_token (username, token) VALUES (%s,%s) returning *", (username, token))
        cur.execute("INSERT INTO user_chat (username, chat_id, last_connection) VALUES (%s,%s,%s)", (username, chat_id, datetime.datetime.now()))

        # Store inserts
        conn.commit()
        
    cur.close()
    conn.close()

    return user
    
    
    