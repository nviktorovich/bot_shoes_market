import telebot
from sub.constant import BotToken as BT
from sub.constant import Messages as MSG
from sub.constant import Files as FL
from sub.choise import Choice
import sub.algo as ALGO

bot = telebot.TeleBot(BT.API_TOKEN)


@bot.message_handler(func=lambda message: message.text == '/start' or message.text == MSG.BACK_TO_START_BUTTON)
def start_message_with_brands(message):
    print(f'start_message_with_brands: brand is {Choice.brand}, model is {Choice.model}, color is {Choice.color}')
    Choice.set_model('')
    Choice.set_brand('')
    Choice.set_color('')
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    Brands = ALGO.generate_brands_dictionary(FL.BASE_FILE)
    for row in ALGO.get_parts_of_list(*Brands.keys()):
        keyboard.row(*row)
    bot.send_message(message.chat.id, text=MSG.START_MESSAGE, reply_markup=keyboard, disable_web_page_preview=True)


@bot.message_handler(func=lambda message: message.text in ALGO.generate_brands_dictionary(FL.BASE_FILE).keys()
                                          or message.text == MSG.BACK_TO_MODEL_CHOICE_BUTTON)
def message_with_models_of_selected_brand(message):

    print(f'message_with_models_of_selected_brand: brand is {Choice.brand}, model is {Choice.model}, color is {Choice.color}')
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    Brands = ALGO.generate_brands_dictionary(FL.BASE_FILE)
    try:
        if message.text in Brands.keys():
            Choice.set_brand(message.text)
            for row in ALGO.get_parts_of_list(*Brands[message.text]):
                keyboard.row(*row)
        elif message.text == MSG.BACK_TO_MODEL_CHOICE_BUTTON:
            for row in ALGO.get_parts_of_list(*Brands[Choice.brand]):
                keyboard.row(*row)
        keyboard.row(MSG.BACK_TO_START_BUTTON)
        bot.send_message(message.chat.id, text=MSG.BRAND_MESSAGE, reply_markup=keyboard)
    except KeyError:
        keyboard.row(MSG.BACK_TO_START_BUTTON)
        bot.send_message(message.chat.id, text=MSG.ALARM_MESSAGE, reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text in ALGO.generate_model_list(
    ALGO.generate_brands_dictionary(FL.BASE_FILE)))
def message_with_colors_of_selected_model(message):
    print(ALGO.generate_model_list(ALGO.generate_brands_dictionary(FL.BASE_FILE)))
    Choice.set_model(message.text)
    print(f'message_with_colors_of_selected_model: brand is {Choice.brand}, '
          f'model is {Choice.model}, color is {Choice.color}')
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    if Choice.brand != '':
        colors = ALGO.get_list_of_colors(ALGO.generate_brands_dictionary(
            FL.BASE_FILE, 'Colors'), message.text)
        for row in ALGO.get_parts_of_list(*colors):
            keyboard.row(*row)
        keyboard.row(MSG.BACK_TO_MODEL_CHOICE_BUTTON, MSG.BACK_TO_START_BUTTON)
        bot.send_message(message.chat.id, text=ALGO.get_color_select_message(
            Choice.brand, Choice.model), reply_markup=keyboard)
    else:
        keyboard.row(MSG.BACK_TO_START_BUTTON)
        bot.send_message(message.chat.id, text=MSG.ALARM_MESSAGE, reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text in ALGO.get_list_of_colors(
    ALGO.generate_brands_dictionary(FL.BASE_FILE, 'Colors'), Choice.model))
def message_with_picture_of_selected_model_and_color(message):
    Choice.set_color(message.text)
    print(f'message_with_picture_of_selected_model_and_color: '
          f'brand is {Choice.brand}, model is {Choice.model}, color is {Choice.color}')
    link = ALGO.get_photo_link(ALGO.generate_brands_dictionary(
        FL.BASE_FILE, 'Colors'), Choice.model, message.text)[0]
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(text=MSG.VIEW_PRICE_BUTTON[0], callback_data=MSG.VIEW_PRICE_BUTTON[1]),
        telebot.types.InlineKeyboardButton(text=MSG.GET_BUY_BUTTON[0], callback_data=MSG.GET_BUY_BUTTON[1]))
    bot.send_photo(message.chat.id, link, caption=f'<b>{Choice.brand}</b>\n<b>{Choice.model}</b>\n{Choice.color}',
                   parse_mode='HTML', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda message: message.data == MSG.VIEW_PRICE_BUTTON[1])
def message_with_selected_picture_with_price(message):
    try:
        price = ALGO.get_photo_link(ALGO.generate_brands_dictionary(
            FL.BASE_FILE, 'Colors'), Choice.model, Choice.color)[1]
        print(price)
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(text=price, callback_data='**********'),
            telebot.types.InlineKeyboardButton(text=MSG.GET_BUY_BUTTON[0], callback_data=MSG.GET_BUY_BUTTON[1]))
        bot.edit_message_reply_markup(chat_id=message.message.chat.id, message_id=message.message.message_id,
                                      reply_markup=keyboard)
    except KeyError:
        print("KeyError")


@bot.callback_query_handler(func=lambda message: message.data == MSG.GET_BUY_BUTTON[1])
def message_with_selected_model_with_price(message):
    try:
        product = f'{Choice.brand}, {Choice.model}, {Choice.color}'
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        send_contact_button = telebot.types.KeyboardButton(MSG.SHOW_PHONE_BUTTON, request_contact=True)
        keyboard.add(MSG.BACK_TO_START_BUTTON, send_contact_button)
        bot.edit_message_caption(caption=ALGO.get_buy_message(product), chat_id=message.message.chat.id,
                                 message_id=message.message.message_id, parse_mode='HTML')
        bot.send_message(message.message.chat.id, 'Продолжить?', reply_markup=keyboard)

    except KeyError:
        print('KeyError')


@bot.message_handler(content_types=['contact'])
def message_with_good_bay_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row(MSG.BACK_TO_START_BUTTON)
    bot.send_message(message.chat.id, MSG.GOOD_BAY_MESSAGE, reply_markup=keyboard)
    bot.send_message(chat_id=BT.HOST_ID, text=ALGO.send_message_to_host(message.contact.phone_number,
                                                                        Choice.brand, Choice.model, Choice.color))


while True:
    bot.polling(none_stop=True, interval=0, timeout=0)
