from data.loader import bot, db
from telebot.types import Message
from keyboards.default import register_button


@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    db.insert_user_id_to_users(user_id)
    check = db.check_user_info(user_id)
    if None in check:
        markup = register_button()
        text = '''Siz ro'yhatdan o'tmagansiz, iltimos biz bilan ishlash uchun ro'yhatdan o'ting.'''
    else:
        text = 'Xush kelibsiz!'
        markup = None
    bot.send_message(chat_id, text, reply_markup=markup)

