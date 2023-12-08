# import httpx
# from parsel import Selector
# import asyncio
#
#
# class AsyncScraper:
#     HEADERS = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#         'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#         'Accept-Encoding': 'gzip, deflate, br',
#         # 'Referer': 'https://www.prnewswire.com/news-releases/',
#         'Connection': 'keep-alive',
#     }
#     URL = "https://24.kg/"
#     LINK_XPATH = '//div[@class="title"]/a/@href'
#     IMG_XPATH = '//div[@class="Dashboard-Content-Card--image"]/img/@src'
#
#     async def async_gererator(self, limit):
#         for page in range(1, limit + 1):
#             yield page
#
#     async def async_scrapers(self):
#         urls = []
#         async with httpx.AsyncClient(headers=self.HEADERS) as client:
#             async for page in self.async_gererator(limit=5):
#                 url = await self.get_url(client=client, url=self.URL)
#                 urls.append(url)
#         return urls
#
#     async def get_url(self, client, url):
#         response = await client.get(url)
#         print(response.url)
#         await self.scrap_link(html=response.text, client=client)
#         return response.url
#
#     async def scrap_link(self, html, client):
#         tree = Selector(text=html)
#         links = tree.xpath(self.LINK_XPATH).extract()
#         return links
#
#
# if __name__ == '__main__':
#     scraper = AsyncScraper()
#     asyncio.run(scraper.async_scrapers())
