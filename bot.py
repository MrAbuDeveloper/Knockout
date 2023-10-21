from data.loader import bot, db

import handlers

db.create_users_table()

if __name__ == '__main__':
    bot.infinity_polling()

