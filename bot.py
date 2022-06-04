import telebot
from news_parser import Parser

bot = telebot.TeleBot('5527984135:AAHdNR45WKfP5R4zLE7rtNYDNXeabq6S8ck')

CHANNEL_NAME = '@slayer_parser_bot'

news_list = Parser('кошелек')
print(news_list.get_news())
# @bot.message_handler(content_types=['text'])
# def get_message():
#     pass

