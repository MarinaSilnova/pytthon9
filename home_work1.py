#Добавьте telegram-боту возможность вычислять выражения

import telebot

bot = telebot.TeleBot("6067113838:AAEEjzzUVYigi06vVTRWtayLh0XrWKlv-aE", parse_mode=None)

@bot.message_handler(content_types=['text'])
def echo_all(message):
    msg = message.text
    bot.reply_to(message, eval(msg))

bot.infinity_polling()