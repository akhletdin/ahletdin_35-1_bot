# from parsel import Selector
# import requests
#
#
# class NewsScraper:
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#         'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#         'Accept-Encoding': 'gzip, deflate, br',
#         # 'Referer': 'https://www.prnewswire.com/news-releases/',
#         'Connection': 'keep-alive',
#     }
#     MAIN_URL = "https://24.kg/"
#     LINK_XPATH = '//div[@class="title"]/a/@href'
#     IMG_XPATH = '//div[@class="Dashboard-Content-Card--image"]/img/@src'
#
#     def parse_data(self):
#         html = requests.get(url=self.MAIN_URL, headers=self.headers).text
#         # print(html)
#         tree = Selector(text=html)
#         links = tree.xpath(self.LINK_XPATH).extract()
#         # images = tree.xpath(self.IMG_XPATH).extract()
#         for link in links:
#             print(link)
#         return links
#         # for img in images:
#         #     print(img)
#
#
# if __name__ == "__main__":
#     scraper = NewsScraper()
#     scraper.parse_data()
