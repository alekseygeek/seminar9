# Напишите программу, удаляющую из текста все слова, содержащие "абв"

import telebot

bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "напиши текст содержащие слово абв и он это слово удалит")


def text_clear(text, find_str):
    abv = text.split(' ')
    result = []
    for item in abv:
        if 'абв' not in item:
            result.append(item)
    if len(result) == 0:
        result = ['пусто']
    return ' '.join(result)


@bot.message_handler(func=lambda message: True)
def echo_all(message):

    bot.reply_to(message, text_clear(message.text, 'абв'))


bot.infinity_polling()
message: True
