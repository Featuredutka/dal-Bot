import telebot
import bot_functions as btf
import PIL
from PIL import Image
from requests import get

# Bot token
bot = telebot.TeleBot('5115979492:AAE1d6aCMRU3mIGIdegKelqdk9Ckz_eK8U8')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Пришли мне Emoji, который необходимо сделать размытым.')
                     
@bot.message_handler(content_types=['text'])
def send_text(message):
    word = btf.test()
    bot.send_message(message.chat.id, word.word.strip("[]"))
    # Definition
    bot.send_message(message.chat.id, word.definition.strip("[]"))
    # 
    bot.send_message(message.chat.id, word.example.strip("[]"))
    #     bot.send_document(message.chat.id, img) 
    # elif message.text.lower() == 'наш второй смайлик':
    #     img = open('Смайлики и люди 2.png', 'rb')
    #     bot.send_document(message.chat.id, img)    

bot.polling()
