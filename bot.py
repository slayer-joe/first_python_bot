import telebot
from news_parser import Parser
import utils

bot = telebot.TeleBot('5527984135:AAHdNR45WKfP5R4zLE7rtNYDNXeabq6S8ck')

CHANNEL_NAME = '@slayer_parser_bot'

options_array = ['кошелек', 'лайфстайл', 'авто', 'технологии', 'недвижимость']

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет, выбери категорию новостей')
    keyboard = utils.generate_keyboard('кошелек', 'лайфстайл', 'авто', 'технологии', 'недвижимость')
    bot.send_message(m.chat.id, m, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_message(msg):
    try:
        news_parse = Parser(msg.text)
        news_list = news_parse.get_news()
        for news in news_list:
            message = f"{news['title']}\n {news['image_src']}\n {news['short_text']}\n {news['pub_date']}"
            bot.send_message(msg.chat.id, message)
    except:
        if msg.text not in options_array:
            bot.reply_to(msg, "а вот йух тебе")

bot.polling(none_stop=True, interval=0)

