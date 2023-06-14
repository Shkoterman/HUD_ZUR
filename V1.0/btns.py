from telebot import types
# main menu btns
ping=types.KeyboardButton('ping')
take_place=types.KeyboardButton('Займи место')
my_reg=types.KeyboardButton('Мои регистрации')
test=types.KeyboardButton('Test')

# btnc keets
user_main_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
admin_main_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
my_main_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
user_main_menu_markup.add(my_reg, take_place)
admin_main_menu_markup=user_main_menu_markup.add()
my_main_menu_markup=admin_main_menu_markup.add(ping, test)

# other
back=types.KeyboardButton('Отмена')
skip=types.KeyboardButton('Пропустить')
