import telebot
from news_parser import Parser
import utils

bot = telebot.TeleBot('5527984135:AAHdNR45WKfP5R4zLE7rtNYDNXeabq6S8ck')

CHANNEL_NAME = '@slayer_parser_bot'

options_array = ['кошелек', 'лайфстайл', 'авто', 'технологии', 'недвижимость']

@bot.message_handler(commands=["start"])
def start(m, res=False):
    keyboard = utils.generate_keyboard('кошелек', 'лайфстайл', 'авто', 'технологии', 'недвижимость')
    bot.send_message(m.chat.id, 'Привет, выбери категорию новостей', reply_markup=keyboard)
    print(m)


@bot.message_handler(content_types=['text'])
def get_message(msg):
    try:
        keyboard = utils.generate_keyboard('кошелек', 'лайфстайл', 'авто', 'технологии', 'недвижимость')
        news_parse = Parser(msg.text)
        news_list = news_parse.get_news()
        for news in news_list:
            message = f"*{news['title']}*\n\n {news['short_text']}\n\n {news['link']}\n\n {news['pub_date']}"
            bot.send_photo(msg.chat.id, news['image_src'], caption=message, parse_mode="Markdown")
        bot.send_message(msg.chat.id, 'Выбери категорию новостей, открой иконку списка, возле иконки смайлов', reply_markup=keyboard)
    except:
        if msg.text not in options_array:
            bot.reply_to(msg, "Выбери из предложенных опций, открой иконку опций возле иконки смайлов, пес!!!")

bot.polling(none_stop=True, interval=0)

