import telebot
import requests
from bote import TOKEN 
 
bot = telebot.TeleBot(TOKEN) 

@bot.message_handler(commands=['coffee'])
def send_rand_cat(message):
    r = requests.get('https://coffee.alexflipnote.dev/random.json') #откуда мы берем информацию для фотки

    url = r.json()["file"] #сама команда, чтобы получить случайнyю фотку

    bot.send_photo(message.chat.id, url) 

if __name__ == '__main__': #позволяет боту постоянно чекать ваши команды
    bot.infinity_polling()
   
