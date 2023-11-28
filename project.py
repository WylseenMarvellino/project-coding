from telebot import *
import re
import random

api = '6888438890:AAFulD6tXgJJqMVb72C_pBIXw3rUstY2Sdw'
bot = TeleBot(api)

# start
@bot.message_handler(commands=['start'])
def selamat_datang(message):
    bot.reply_to(message, 'Selamat Datang')
    chatid = message.chat.id
    bot.send_message(chatid, 'Selamat Datang Pengguna')

#foto
@bot.message_handler(commands=['foto'])
def kirim_foto(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('C:\\Users\\Asus\\OneDrive\\Desktop\\project coding\\bumi.jpeg', 'rb'))
    
#chatbot
sapa = ['halo juga', 'hai juga']
@bot.message_handler(content_types=['text'])
def chabot(message):
    teks = message.text
    if re.findall('halo|hai', teks):
        chatid = message.chat.id
        bot.send_message(chatid, random.choice(sapa))

    else:
        chatid = message.chat.id
        bot.sen_message(chatid, 'Saya tidak paham')
        
bot.infinity_polling()
