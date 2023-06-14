import telebot
from telebot import types
import time
import btns
import get_airtable
import strings




time_out={}
bot = telebot.TeleBot('5885884113:AAE_TcJavu1iWb1NTF3EZ7g-2iuMEWBm6gY')  # this is test
#bot = telebot.TeleBot('6148758021:AAGl4BGfSnTuwyKoDUKRP3UJlPIy3Pv2OqM') # this is prod
@bot.message_handler(commands=["start"])
def Start(message):
    main_menu(message, True)
    get_airtable.add_user_id(message.chat.id, message.from_user.username)
@bot.message_handler(content_types=["text"])
def handle_text(message):

    # user's func
    if message.text== btns.take_place.text:
        take_place_st_1(message)
        menu_time_out(message)
    if message.text== btns.my_reg.text:
        pass


    # my func
    if message.text== btns.test.text and message.chat.id==214130351:
        pass
    if message.text== btns.ping.text and message.chat.id==214130351:
        bot.send_message(message.chat.id, text=btns.ping.text)

def menu_time_out(message):
    time_out[message.chat.id]=1
    time.sleep(600)
    if time_out[message.chat.id]==1:
        main_menu(message, 2)
        time_out[message.chat.id]=0
def main_menu(message, reason): # 0-ending process, 1-first time, 2-timeout
    bot.clear_step_handler_by_chat_id(message.chat.id)
    time_out[message.chat.id] = 0
    if message.chat.id==214130351:
        markup= btns.my_main_menu_markup
    else:
        markup= btns.user_main_menu_markup
    if reason==1:
        text= strings.hello_text
    elif reason==2:
        text=strings.time_out
    else:
        text= strings.main_menu_text
    bot.send_message(message.chat.id, text=text, reply_markup=markup)




def take_place_st_1(message):
    if message.from_user.username==None:
        bot.send_message(message.chat.id, text=strings.need_dog)
    else:
        ev_dickt= get_airtable.get_open_for_reg_event_dickt()
        if ev_dickt=={}:
            bot.send_message(message.chat.id, text=strings.there_is_no_reg_events)
            main_menu(message, 0)
        else:
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in range(len(ev_dickt)):
                markup.add(types.KeyboardButton(list(ev_dickt.keys())[i]))
            markup.add(btns.back)
            send=bot.send_message(message.chat.id, text=strings.what_ev_for_take_place, reply_markup=markup)
            bot.register_next_step_handler(send, take_place_st_2, ev_dickt)

def take_place_st_2(message, ev_dickt):
    if message.text== btns.back.text:
        main_menu(message, 0)
    elif message.text in list(ev_dickt.keys()):
        ev_id=ev_dickt[message.text]
        ev_name=message.text
        user_name= get_airtable.get_username(message.from_user.username)
        if user_name==None:
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btns.back, btns.skip)
            send=bot.send_message(message.chat.id, text=strings.whats_ur_name, reply_markup=markup)
            bot.register_next_step_handler(send, take_place_st_3, ev_id, ev_name)
        else:
            bot.send_message(message.chat.id, text=strings.wait)
            take_place_st_4(message, ev_id, ev_name, user_name, first_time=0)
    else:
        send=bot.send_message(message.chat.id, text=strings.didnt_get_it)
        bot.register_next_step_handler(message, take_place_st_2, ev_dickt)

def take_place_st_3(message, ev_id, ev_name):
    if message.text== btns.back.text:
        main_menu(message, 0)
    elif message.text== btns.skip.text or message.text==None:
        user_name= strings.didnt_whant_show_name
    elif message.text!=None:
        user_name=message.text

    bot.send_message(message.chat.id, text=strings.wait)
    take_place_st_4(message, ev_id, ev_name, user_name, first_time=1)

def take_place_st_4(message, ev_id, ev_name, user_name, first_time):
    user_nick=message.from_user.username
    get_airtable.write_in_reg(user_nick, user_name, ev_id)
    if user_name!= strings.didnt_whant_show_name and first_time==1:
        get_airtable.write_in_members(user_nick, user_name)
    bot.send_message(message.chat.id, text=strings.registration_done + ev_name)
    main_menu(message, 0)
    time_out[message.chat.id]=0



bot.infinity_polling(timeout=30, long_polling_timeout=15)