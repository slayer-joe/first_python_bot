from bs4 import BeautifulSoup as bs
import requests
import re





class Parser:
    def __init__(self, category):
        self.categories = {
            'кошелек': 'https://money.onliner.by/',
            'лайфстайл': 'https://people.onliner.by/',
            'авто': 'https://auto.onliner.by/',
            'технологии': 'https://tech.onliner.by/',
            'недвижимость': 'https://realt.onliner.by/'
        }
        self.category_url = self.categories[category]
        self.news_list = []

    def get_news(self):
        news = requests.get(self.category_url)
        html = bs(news.content, 'html.parser')
        # print(html.select(".news-tidings__item"))
        for el in html.select(".news-tidings__list >.news-tidings__item_condensed"):
            title = el.select_one(".news-tidings__clamping > .news-tidings__subtitle span").text
            image = el.select_one(".news-tidings__image > picture > img").get('src')
            text = re.sub(r'\s+', ' ', el.select_one(".news-tidings__speech").text)
            pub_date = re.sub(r'\s+', ' ', el.select_one(".news-tidings__detail .news-tidings__time").text)
            self.news_object_creator(title, image, text, pub_date)
        return self.news_list
    
    def news_object_creator(self, title, image_src, short_text, pub_date):
        news_object = {
            'title': title,
            'image_src': image_src,
            'short_text': short_text,
            'pub_date': pub_date
        }
        self.news_list.append(news_object)


# parser = Parser('кошелек')
# parser.get_news_html()

