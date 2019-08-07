import requests
import telebot
from telebot import types
import random

bot = telebot.TeleBot("922418168:AAEFI83dVftH4ZIg2U_xnXqaKH0cpfCSuj0")



keyboard = types.InlineKeyboardMarkup()
key_yes = types.InlineKeyboardButton(text='Узнать о нашем курсе',callback_data='yes')
keyboard.add(key_yes)
key_no = types.InlineKeyboardButton(text='Узнать о наших салонах',callback_data='no')
keyboard.add(key_no)

keyboard1 = types.InlineKeyboardMarkup()
key_site = types.InlineKeyboardButton(text='Узнать подробнее на курсе', url='https://rufinakaramova.com')
keyboard1.add(key_site)

keyboard2=types.InlineKeyboardMarkup()
key223=types.InlineKeyboardButton(text='Avenue 223',callback_data='223')
keyboard2.add(key223)
key116=types.InlineKeyboardButton(text='Avenue 116',callback_data='116')
keyboard2.add(key116)
keyAmor=types.InlineKeyboardButton(text='Mon Amor',callback_data='amor')
keyboard2.add(keyAmor)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет, ты подписался на моего Бота👋🏻' + '\n' +
                 'Давай я буду тебе полезен🤗' + '\n' +
                 'Если хочешь узнать информацию о курсах или же о салонах' + '\n' +
                 'Жми кнопку ниже⤵',reply_markup=keyboard)







@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "yes":
        bot.send_message(call.message.chat.id, '🔷Обучение ведет мастер высочайшей категории' + '\n' +
                     '🔷Трудоустройство в лучших салонах Казахстана' + '\n' +
                     '🔷Полная отработка на моделях' + '\n' +
                     '🔷Обучение правильной фотосъемки' + '\n' +
                     '🔷Полная работа над ошибками под присмотром мастера',reply_markup=keyboard1)
    elif call.data == "no":
        bot.send_message(call.message.chat.id,'В городе Алматы открыты двери 3-х действующих '
                             'салонов красоты, которые предоставляют широкий спектр '
                             'услуг для любителей индустрии красоты и креатива.',reply_markup=keyboard2)
    elif call.data == "223":
        bot.send_message(call.message.chat.id, 'Виды услуг:'
                              ' Парикхмахеры, визажисты, мужские мастера, '
                              'косметологи, маникюр, педикюр, наращивание волос'+'\n'+' '+
                               'Телефон для связи:+7 702 101 1001'+'\n'+' '+
                            'Наш Instagram:https://instagram.com/rufinakaramova?igshid=tk54to4gttpd',reply_markup=keyboard2)
    elif call.data == "116":
        bot.send_message(call.message.chat.id, 'Виды услуг:'
                              ' Парикхмахеры, визажисты, мужские мастера, '
                              'косметологи, маникюр, педикюр, наращивание волос' + '\n' +' '+
                     'Телефон для связи: +7 702 101 1001' + '\n' +' '+
                     'Наш Instagram:https://instagram.com/rufinakaramova?igshid=tk54to4gttpd',reply_markup=keyboard2)

    elif call.data == "amor":
        bot.send_message(call.message.chat.id, 'Виды услуг:'
                              ' Маникюр, педикюр, подолог, наращивание ресниц, обучение'+'\n'+' '+
                               'Телефон для связи: +7 778 637 00 08'+'\n'+' '+
                              'Наш Instagram:https://instagram.com/rufinakaramova?igshid=tk54to4gttpd',reply_markup=keyboard2)

bot.polling(none_stop=True)
