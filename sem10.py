import telebot
import os.path
import datetime
from telebot import types


bot = telebot.TeleBot("TOKEH")


def OpenListW():
    check_file = os.path.isfile('log.txt')
    if check_file == False:
        file = open('log.txt', 'w', encoding='utf-8')
        file.close()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Это бот калькулятор. Посчитаем? Жми /calculator')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.from_user.id, "Введите число")
    bot.register_next_step_handler(message, number1)


def number1(message):
    number1 = message.text
    file = open('log.txt', 'a', encoding='utf-8')
    file.write(
        str(f"{datetime.datetime.now()} {message.from_user.username}: {number1}\n"))
    file.close()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton('+')
    button2 = types.KeyboardButton('-')
    button3 = types.KeyboardButton('*')
    button4 = types.KeyboardButton('/')
    markup.add(button1, button2, button3, button4)
    msg = bot.send_message(
        message.chat.id, "Выберете операцию", reply_markup=markup)
    bot.register_next_step_handler(msg, operator, number1)


def operator(message, number1):
    operator = message.text
    bot.send_message(message.from_user.id, f"Введи второе число")
    bot.register_next_step_handler(message, result, number1, operator)
    file = open('log.txt', 'a', encoding='utf-8')
    file.write(
        str(f"{datetime.datetime.now()} {message.from_user.username}: {operator}\n"))
    file.close()


def result(message, number1, operator):
    number2 = message.text
    number1 = ''.join([i for i in number1 if i in '0123456789.'])
    number2 = ''.join([i for i in number2 if i in '0123456789.'])
    operator = ''.join([i for i in operator if i in '*/-+'])

    file = open('log.txt', 'a', encoding='utf-8')
    file.write(
        str(f"{datetime.datetime.now()} {message.from_user.username}: {number2}\n"))

    if number1 != '' and number2 != '' and operator != '':
        number1, number2 = int(number1), int(number2)
        if operator == '/':
            summa = number1 / number2
            bot.send_message(
                message.from_user.id, f"Результат: {number1} {operator} {number2} = {summa}")
        elif operator == '*':
            summa = number1 * number2
            bot.send_message(
                message.from_user.id, f"Результат: {number1} {operator} {number2} = {summa}")
        elif operator == '-':
            summa = number1 - number2
            bot.send_message(
                message.from_user.id, f"Результат: {number1} {operator} {number2} = {summa}")
        elif operator == '+':
            summa = number1 + number2
            bot.send_message(
                message.from_user.id, f"Результат: {number1} {operator} {number2} = {summa}")

        bot.send_message(message.from_user.id,
                         "хотите ещё посчитать? /calculator")

        file.write(str(
            f"{datetime.datetime.now()} {message.from_user.username}: Результат: {number1} {operator} {number2} = {summa}\n"))

    else:
        bot.send_message(message.from_user.id,
                         "Что-то пошло не так. Начать сначала? /calculator")
        file.write(str(
            f"{datetime.datetime.now()} {message.from_user.username}: Что-то не так: "))

    file.close()


print('Сервер запущен...')
bot.polling()
