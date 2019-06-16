# This Python file uses the following encoding: utf-8

import telebot
from telebot import types
import requests
import datetime

url = "https://api.telegram.org/bot746191373:AAELWYmwVQ9NIy2ANErfc4TAN1n3PWhah-0/"
token = '746191373:AAELWYmwVQ9NIy2ANErfc4TAN1n3PWhah-0'

bot = telebot.TeleBot(token)

def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print('Сообщение от {0} {1}. (id ={2}) \n Текст - {3}'.format(message.from_user.first_name,
                                                                    message.from_user.last_name,
                                                                        str(message.from_user.id),
                                                                            message.text))
    print(answer)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Инвенстировать','Информация','Тех.Поддержка','Отзывы']])
    message = bot.send_message(message.chat.id,'\U0001F52E Приветствуем !\n\n\U0001F525Мы представляем проект, где каждый может заработать и почувствовать себя в роли инвестора.\U0001F525 \n\n\U0001F525Реальные выплаты, никакого обмана, зарабатывать легко!\n\n Админ - @FortunaInvest'
    ,reply_markup=keyboard)


@bot.message_handler(content_types = ['text'])
def handler_text(message):

 #    if message.text == 'Инвенстировать':
 #      keyboard = types.InlineKeyboardMarkup()
 #      callback_button = types.InlineKeyboardButton(text="Поплнить баланс", url="https://my.qiwi.com/Elena-EV7XQbHXA9")
 #      keyboard.add(callback_button)
 #      bot.send_message(message.chat.id,'Для пополения балансы перейдите по ссылке и укажите свой id', reply_markup=keyboard)


    if message.text == 'Инвенстировать':
        answer = 'Инвенстировать'
        bot.send_message(message.from_user.id, '\U0001F4B2 Инвестировать \n\n\U0001F4B0 После пополнения депозита отписаться администрации!!! \n\n\U0001F4B5 Минимальная сумма - 100 \U0001F4B5\n\n\U0001F4AA QIWI - +79224013443 \n ВАЖНО: При пополнении через QIWI вручную ОБЯЗАТЕЛЬНО \n добавьте комментарий : ' + str(message.from_user.id))
        log(message, answer)
    if message.text == 'Информация':
        answer = 'Информация.'
        bot.send_message(message.from_user.id,'\U0001F52E Информация \n\n\U0001F525 Мы представляем вам проект, в котором каждый может заработать и сколотить капитал, став нашим инвестором!\U0001F525 \n\n\U0001F4AC Наш бот поможет вам приумножить ваш капитал на 25% за 3 дней \U0001F4AC \n\n\U0000267B Процедура происходит так: \n\n\U0001F311 Вы инвестируете средства на доступный QiWi \n\n\U0001F313 После перевода в течении трех часов на ваш QIWI кошелёк поступит 25% от суммы вашего депозита. Сумма депозита поступит на баланс Бота.\n\n\U0001F315 А через 3 дней на ваш QIWI поступит ваша сумма депозита. \n\n\U0001F4B0 Прибыль: 25% за 3 дня \n\n\U0001F310 Так же, есть возможность не снимать прибыль и оставлять депозит еще на 3 дней, т.е соответсвенно вы получите уже 50% к депозиту\n\n\U0001F680 Ваши средства приумножаются с помощью ставок на спорт, именно по этому вы получаете такой большой % прибыли.\n\n\U0001F60C Если у вас есть какие либо вопросы, пожалуйста задaвайте их в Лс Админу\n @Fortuna_5 \n\n\U0001F4AA Наш дружелюбный чат где вам всегда рады: https://t.me/joinchat/NIPiORPCR7Ve3J4_1GG8DQ')
        log(message, answer)
 # if message.text == 'Наш чат':
 # answer = 't.me/joinchat/JX9NvRPQXwTU_fmnoJ9mRw'
 # bot.send_message(message.from_user.id,'t.me/joinchat/JX9NvRPQXwTU_fmnoJ9mRw')
 # log(message, answer)
    if message.text == 'Тех.Поддержка':
        answer = '@Fortuna_5'
        bot.send_message(message.from_user.id,'@Fortuna_5')
        log(message, answer)
 # if message.text == 'Тарифы':
 # answer = 'з дня  \n\n ️процент:3% \n\n миниманая сумма - 1000 руб. \n\n  максимальная сумма - 3000 руб. \n\n️Qiwi:=79055767809\n\n	комментарий: 3 \n\n5 дней \n\n  процент5%\n\nминиманая сумма- 3001 руб.\n\n  максимальная сумма - 5000 руб.\n\n Qiwi:=79055767809\n\n комментарий:5 \n\n 10 дней  \n\n процент:10%\n\n  миниманая сумма - 5001 руб.\n\n  максимальная сумма - 50000 руб.\n\n  Qiwi:=79055767809 \n\n комментарий:10\n\n25 дней  \n\n процент:50% \n\n  миниманая сумма - 5001 руб. \n\n  максимальная сумма -  100000 руб.\n\n  Qiwi:=79055767809 \n\nкомментарий:25'
 # bot.send_message(message.from_user.id,'\U0001F52E з дня\n\U0001F531процент:3%\n\U0001F53Dминиманая сумма - 1000 руб.\n\U0001F53Cмаксимальная сумма - 3000 руб.\n\U0001F5C3Qiwi:=79055767809\n\U0001F510\n\n\U0001F52E 5 дней\n\U0001F531 процент:5%\n\U0001F53D миниманая сумма - 3001 руб.\n\U0001F53Cмаксимальная сумма- 5000 руб.\n\U0001F5C3Qiwi:=79055767809\n\U0001F510\n\n \U0001F52E 10 дней\n\U0001F531процент:10%\n\U0001F53D миниманая сумма - 5001 руб.\n\U0001F53Cмаксимальная сумма - 50000 руб.\n\U0001F5C3Qiwi:=79055767809\n\U0001F510\n\n\U0001F52E 25 дней\n\U0001F531процент:50%\n\U0001F53D миниманая сумма - 50001 руб.\n\U0001F53Cмаксимальная сумма - 100000 руб.\n\U0001F5C3Qiwi:=79055767809\n\U0001F510')
 # log(message, answer)
    if message.text == 'Отзывы':
        answer ='Отзывы'
        bot.send_message(message.from_user.id,'\U0001F4E3 Отзывы \n\n \U0001F4BB Наш бот очень дорожит своей репутацией и доверием наших инвесторов \U0001F4BB \n \n \U0001F607 Поэтому, для вас создан канал с реальными отзывами людей о нашем проекте : https://t.me/joinchat/NIPiOReT-bovZAfISfk63w \n\n \U0001F60E Мы вас не подведём! \n\n \U0001F4B8 Зарабатывайте деньги с нашей командой и вступайте в чат единомышленников : https://t.me/joinchat/NIPiORPCR7Ve3J4_1GG8DQ \n\n ')
        log(message, answer)

bot.polling(none_stop = True)








