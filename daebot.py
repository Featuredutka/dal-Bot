import re
import json
import telebot
import psycopg2
import bot_functions as btf

# Bot token
bot = telebot.TeleBot('5115979492:AAE1d6aCMRU3mIGIdegKelqdk9Ckz_eK8U8')

# groups = [-875440784, -827511175, -730167135]#, -635448596]

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)

BUF_SIZE = 65536   # 64KB buffer to read images showed better results than 128 or 256
TABLE_NAME = 'accounts'
CONNECTION = psycopg2.connect(user="postgres",
                                    host="postgres-service.default.svc.cluster.local"
                             )


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, " ❓ Send me a word/phrase to get it's meaning \n\n <b>/help</b> to display options \n\n All definitions provided by <a href='https://www.urbandictionary.com/'>Urban Dictionary</a>", parse_mode="HTML", disable_web_page_preview=True)
    check = message.chat.id

    # if check not in groups:
    #     groups.append(check)
         
@bot.message_handler(commands=['id'])
def get_chatid(message):
    # bot.send_message(message.chat.id, message.chat.id)
    try:
        cursor = CONNECTION.cursor()
        cursor.execute(f"SELECT * FROM {TABLE_NAME} where chat_id like '{message.chat.id}';")
        record = cursor.fetchone()

        if record:  # Image hash in database means this image was already posted
            bot.send_message(message.chat.id, record)
        else:  # No image found - post it and add it's hash to the database
            # print("No image found")
            bot.send_message(message.chat.id, "NO DATA FOUND")
            cursor.execute(f"INSERT INTO {TABLE_NAME} (chat_id) VALUES ('{message.chat.id}');")
            return 1
        CONNECTION.commit()
        
        # bot.send_message(message.chat.id, message.chat.id)
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == "/random":
        rand_word = btf.random_word()
        bot.send_message(message.chat.id, f" ⭐ Your random word/phrase is - <b>{rand_word.word}</b>", parse_mode="HTML")
        bot.send_message(message.chat.id, "🔎 Definition: \n" + re.sub(r"[\[\]]", "", rand_word.definition))
        # for x in rand_word:
        #     bot.send_message(message.chat.id, x)
    elif message.text == "/help":
        bot.send_message(message.chat.id, " ℹ️ List of commands: \n <b>/help</b> - exactly what got you here \n <b>/random</b> - fetch a definition for a random word/phrase", parse_mode="HTML")
    else:
        definition = btf.define(message.text)
        for x, i in zip(definition, range(len(definition))):
            x = re.sub(r"[\[\]]", "", x)
            bot.send_message(message.chat.id, f" 🔎 Definition {i+1}: \n{x}", parse_mode="HTML")



bot.polling()

# with open('json_data.json', 'w') as outfile:
#     outfile.write(json_string)




# CREATE TABLE accounts (
# 	chat_id VARCHAR ( 50 ) UNIQUE NOT NULL
# );