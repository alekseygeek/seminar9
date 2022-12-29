import telebot
import bote
from telebot import types


bot = telebot.TeleBot(bote.CALC_BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "привет!")

 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    data = open('log_user.txt', 'a+', encoding='utf-8')
    data.writelines(str(message.from_user.id) + ' ' + message.text + '\n')
    data.close()


bot.polling(non_stop=False, interval=0)



# Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.

# s = [1,2,3,4,5]
# d = [1,6,7,8,9]
# print(list(set(s) - set(d)))

# калькулятор :

# calc = input('Введите математическое выражение: ')
# res = eval(calc)
# print(f'{calc} = {res}')