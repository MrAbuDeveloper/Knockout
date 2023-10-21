from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def register_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("Ro'yhatdan o'tish ✍️")
    markup.add(btn)
    return markup


