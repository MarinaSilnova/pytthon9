#Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000. Когда игрок угадывает его, бот выводит количество сделанных ходов
import telebot
import random

bot = telebot.TeleBot("6067113838:AAEEjzzUVYigi06vVTRWtayLh0XrWKlv-aE", parse_mode=None)

game_start = False
number=None
count = 1


@bot.message_handler(content_types=['text'])
def rt_all(message):
    global game_start
    global number
    global count
    
    if message.text == 'игра':
        game_start = True
        number = random.randint(1,10)
        bot.reply_to(message, f' Угадай число от 1 до 1000')
    l = int(message.text)
    if l > number:
        bot.reply_to(message, f' Загаданное число меньше')
    elif l < number:
        bot.reply_to(message, f' Загаданное число больше')
    elif l == number:
        bot.reply_to(message, f' Угадал с {count} попытки') 
    count+=1
bot.infinity_polling()
