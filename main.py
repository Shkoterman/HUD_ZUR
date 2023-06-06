import telebot

import btns
import get_airtable
import strings




bot = telebot.TeleBot('5885884113:AAE_TcJavu1iWb1NTF3EZ7g-2iuMEWBm6gY')  # this is test
#bot = telebot.TeleBot('6148758021:AAGl4BGfSnTuwyKoDUKRP3UJlPIy3Pv2OqM') # this is prod
@bot.message_handler(commands=["start"])
def Start(message):
    main_menu(message, True)
@bot.message_handler(content_types=["text"])
def handle_text(message):

    # user's func
    if message.text==btns.take_place.text:
        pass
    if message.text==btns.my_reg.text:
        pass


    # my func
    if message.text==btns.test.text and message.chat.id==214130351:
        print(get_airtable.get_open_for_reg_event_dickt())
    if message.text==btns.ping.text and message.chat.id==214130351:
        bot.send_message(message.chat.id, text=btns.ping.text)


def main_menu(message, reason):
    if message.chat.id==214130351:
        markup=btns.my_main_menu_markup
    else:
        markup=btns.user_main_menu_markup
    if reason==1:
        text=strings.hello_text
    else:
        text=strings.main_menu_text
    bot.send_message(message.chat.id, text=text, reply_markup=markup)

bot.infinity_polling(timeout=30, long_polling_timeout=15)