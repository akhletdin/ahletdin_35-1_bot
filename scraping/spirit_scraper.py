from parsel import Selector
import requests


class SpiritScraper:
    headers = {
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Accept': 'application/x-clarity-gzip',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    MAIN_URL = "https://animespirit.tv/xfsearch/%D0%B0%D0%BD%D0%B8%D0%BC%D0%B5%20%D0%BF%D1%80%D0%BE%20%D0%B4%D0%B5%D0%BC%D0%BE%D0%BD%D0%BE%D0%B2/"
    LINK_XPATH = '//div[@class="custom-poster"]/a/@href'
    IMG_XPATH = '//div[@class="custom-poster"]/a/img/@src'
    SERIES_XPATH = '//div[@class="custom-label1"]/text()'
    NEW_XPATH = '//div[@class="row newsCards"]/div/a/@href'
    PAGE_XPATH = '//div[@class="card col-viev"]/a/@href'

    def parse_data(self):
        html = requests.get(url=self.MAIN_URL, headers=self.headers,
                            proxies="http://username:password@123.43.677.89:6789").text
        # print(html)
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_XPATH).extract()
        images = tree.xpath(self.IMG_XPATH).extract()
        series = tree.xpath(self.SERIES_XPATH).extract()
        news = tree.xpath(self.NEW_XPATH).extract()
        pages = tree.xpath(self.NEW_XPATH).extract()
        for link in links:
            print(link)
        for image in images:
            print(image)
        for serie in series:
            print(serie)
        for new in series:
            print(new)
        for page in series:
            print(page)


if __name__ == "__main__":
    scraper = SpiritScraper()
    scraper.parse_data()
