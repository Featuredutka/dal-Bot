import re
import telebot
import bot_functions as btf

# Bot token
bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, " ❓ Send me a word/phrase to get it's meaning \n\n <b>/help</b> to display options \n\n All definitions provided by <a href='https://www.urbandictionary.com/'>Urban Dictionary</a>", parse_mode="HTML", disable_web_page_preview=True)
         
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == "/random":
        rand_word = btf.random_word()

        bot.send_message(message.chat.id, f" ⭐ Your random word/phrase is - <b>{rand_word.word}</b>", parse_mode="HTML")
        bot.send_message(message.chat.id, "🔎 Definition: \n" + re.sub(r"[\[\]]", "", rand_word.definition))
        # for x in rand_word:
        #     bot.send_message(message.chat.id, x)
    elif message.text == "/help":
        bot.send_message(message.chat.id, " ℹ️ List of commands: \n\n <b>/help</b> - exactly what got you here \n <b>/random</b> - fetch a definition for a random word/phrase", parse_mode="HTML")
    else:
        definition = btf.define(message.text)
        for x, i in zip(definition, range(len(definition))):
            x = re.sub(r"[\[\]]", "", x)
            bot.send_message(message.chat.id, f" 🔎 Definition {i+1}: \n {x}", parse_mode="HTML")

bot.polling()
