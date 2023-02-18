import telebot
from telebot import types

TOKEN = '5554445689:AAEcSZr4BCBMcEVGGaGXaaKs62NRZWTtNhI'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn_types_alcohol = types.InlineKeyboardButton(text='ПРОИЗВОДСТВО АЛКОГОЛЯ', callback_data='btn_types_alcohol')
    kb.add(btn_types_alcohol)
    bot.send_message(message.chat.id, "Приветствую вас на обучающем курсе по барному ассортименту ресторана Телеграф",
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn_types_alcohol':
        file = open('alcohol_types.jpg', 'rb')
        kb = types.InlineKeyboardMarkup(row_width=1)
        botany = types.InlineKeyboardButton(text='БОТАНИКАЛЫ', callback_data='botany')
        kb.add(botany)
        bot.send_photo(callback.message.chat.id, file,
                       'Выделяют 4 группы сырья для производства алкоголя. Разберем каждую отдельно.', reply_markup=kb)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback1_data(callback):
    if callback.data == 'botany':
        file = open('fermentation.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file,
                       'Большое количество алкогольных напитков получают на основе растений. Например: текила, ром, мескаль. '
                       'Как правило, из растений добывают сладкий сок, который сбраживают, а затем перегоняют.')

#         # file = open('excerpt.jpg', 'rb')
        # bot.send_photo(callback.message.chat.id, file,



        # @bot.message_handler(content_types=['text'])
        # def bot_message(message):
        #     if message.text == 'ПРОИЗВОДСТВО АЛКОГОЛЯ':

        # @bot.callback_query_handler(func=lambda callback: callback.data)
        # def check_callback_data(callback):
        #     if callback.data == 'botany':

bot.infinity_polling()
