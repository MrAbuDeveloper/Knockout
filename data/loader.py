from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from data.config import TOKEN
from telebot import custom_filters
from database.database import DataBase

bot = TeleBot(TOKEN, state_storage=StateMemoryStorage())

bot.add_custom_filter(custom_filters.StateFilter(bot))

db = DataBase()
