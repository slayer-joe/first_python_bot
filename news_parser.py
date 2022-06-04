from bs4 import BeautifulSoup as bs
import requests


categories = {
    'кошелек': 'https://money.onliner.by/',
    'лайфстайл': 'https://people.onliner.by/',
    'авто': 'https://auto.onliner.by/',
    'технологии': 'https://tech.onliner.by/',
    'недвижимость': 'https://realt.onliner.by/'
}

class Parser:
    def __init__(self, category):
        self.category_url = categories[category]
        self.news_list = []

    def get_news(self):
        news = requests.get(self.category_url)
        html = bs(news.content, 'html.parser')
        for el in html.select('.aubli_data > a'):
            self.news_list.append(el.text)
        print(self.news_list)
        return self.news_list

parser = Parser('кошелек')
parser.get_news()