import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.selector import Selector
import json

class XboxSpider(scrapy.Spider):
    name = "xbox-spider"
    allowed_domains = ["xbox.com", "amazon.com", "bestbuy.com"]

     
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,*",  # Consider broader language range
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    def __init__(self, search_query='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search_query = search_query
        self.game_name_xbox = search_query.replace(' ', '+')
        self.game_name_amazon = search_query.replace(' ', '+')
        self.game_name_bestbuy = search_query.replace(' ', '+')
        self.xbox_games_data = []
        self.amazon_games_data = []
        self.scraped_data = []

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920x1080')
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(options=options)

    def start_requests(self):
        xbox_url = f"https://www.xbox.com/en-us/Search/Results?q={self.game_name_xbox}"
        amazon_url = f"https://www.amazon.com/s?k={self.game_name_amazon}+xbox+game"
        # Add other URLs if needed

        yield scrapy.Request(xbox_url, callback=self.parse, headers=self.headers)
        yield scrapy.Request(amazon_url, callback=self.parse_amazon, headers=self.headers)

    def parse(self, response):
        self.driver.get(response.url)

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'ol.SearchProductGrid-module__container___jew-i'))
            )
        except Exception as e:
            self.logger.error(f"Timeout waiting for search results: {e}")
            return

        sel = Selector(text=self.driver.page_source)
        games = sel.css('ol.SearchProductGrid-module__container___jew-i li')

        for game in games:
            name = game.css('.ProductCard-module__title___nHGIp::text').get().strip()
            price_element = game.css('.Price-module__boldText___vmNHu::text').get()
            price = price_element.strip() if price_element else 'Price not available'
            
            if price == 'Price not available':
                view_game_element = game.css('.Price-module__viewLink___2Pbnf::text').get()
                if view_game_element and view_game_element.strip() == 'View Game':
                    price = 'View Game'
            link = game.css('a::attr(href)').get()
            image_url = game.css('img::attr(src)').get()

            game_data = {
                'name': name,
                'price': price,
                'link': link,
                'image_url': image_url,
            }
            self.scraped_data.append(game_data)
            self.xbox_games_data.append(game_data)
            yield game_data



    def parse_amazon(self, response):
        # Extracting game information
        games = response.css('div.s-main-slot div.s-result-item')
        if not games:
            self.logger.info("No games found on Amazon page.")
        else:
            self.logger.info(f"Found {len(games)} games on Amazon page.")

        for game in games:
            name = game.css('h2 span.a-text-normal::text').get()
            price_whole = game.css('span.a-price-whole::text').get()
            price_fraction = game.css('span.a-price-fraction::text').get()
            link = game.css('h2 a.a-link-normal::attr(href)').get()
            image_url = game.css('img.s-image::attr(src)').get()
            if price_whole:  # Ensure price_whole is not None
                price = price_whole + '.' +  (price_fraction if price_fraction else '')
                if name and link:
                    game_data = {
                        'name': name,
                        'price': price,
                        'link': response.urljoin(link),
                        'image_url': image_url,
                    }
                    self.scraped_data.append(game_data)

                    self.amazon_games_data.append(game_data)
                    yield game_data
    
    def closed(self, reason):
        with open(self.output_file, 'w') as f:
            json.dump(self.scraped_data, f)




# import scrapy
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from scrapy.selector import Selector


# class XboxSpider(scrapy.Spider):
#     name = "xbox-spider"
#     allowed_domains = ["xbox.com","amazon.com","bestbuy.com"]

#     start_urls = ['https://www.xbox.com/en-us/Search/Results?q=gta+v']
#     search_query='gta v'


#     def __init__(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument('--headless')
#         options.add_argument('--no-sandbox')
#         options.add_argument('--disable-dev-shm-usage')
#         options.add_argument('--disable-gpu')
#         options.add_argument('--window-size=1920x1080')
#         options.add_argument('--disable-blink-features=AutomationControlled')
#         self.driver = webdriver.Chrome(options=options)
#         self.xbox_games_data = []
#         self.amazon_games_data=[]


#     def parse(self, response):
#         self.driver.get(response.url)

#         try:
#             WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, 'ol.SearchProductGrid-module__container___jew-i'))
#             )
#         except Exception as e:
#             self.logger.error(f"Timeout waiting for search results: {e}")
#             return

#         sel = Selector(text=self.driver.page_source)
#         games = sel.css('ol.SearchProductGrid-module__container___jew-i li')

#         for game in games:
#             name = game.css('.ProductCard-module__title___nHGIp::text').get().strip()
#             price_element = game.css('.Price-module__boldText___vmNHu::text').get()
#             price = price_element.strip() if price_element else 'Price not available'
            
#             if price == 'Price not available':
#                 view_game_element = game.css('.Price-module__viewLink___2Pbnf::text').get()
#                 if view_game_element and view_game_element.strip() == 'View Game':
#                     price = 'View Game'
#             link = game.css('a::attr(href)').get()
#             image_url = game.css('img::attr(src)').get()

#             game_data = {
#                 'name': name,
#                 'price': price,
#                 'link': link,
#                 'image_url': image_url,
#             }
            
#             self.xbox_games_data.append(game_data)
#             yield game_data

#             # yield {
#             #     'name': name,
#             #     'price': price,
#             #     'link': link,
#             #     'image_url': image_url,
#             # }
#             game_search_query = 'gta v'  # Replace with dynamic query if needed
#             if 'amazon.com' in response.url:
#                 yield from self.parse_amazon(response)
#             else:
#                 # Build Amazon URL
#                 amazon_url = f"https://www.amazon.com/s?k={self.search_query.replace(' ', '+')}+xbox+game"
#                 # amazon_url = f"https://www.amazon.com/s?k={game_search_query}"
#                 yield scrapy.Request(amazon_url, callback=self.parse_amazon)


#     def parse_amazon(self, response):
#         # Extracting game information
#         games = response.css('div.s-main-slot div.s-result-item')
#         if not games:
#             self.logger.info("No games found on Amazon page.")
#         else:
#             self.logger.info(f"Found {len(games)} games on Amazon page.")

#         for game in games:
#             name = game.css('h2 span.a-text-normal::text').get()
#             price_whole = game.css('span.a-price-whole::text').get()
#             price_fraction = game.css('span.a-price-fraction::text').get()
#             link = game.css('h2 a.a-link-normal::attr(href)').get()
#             image_url = game.css('img.s-image::attr(src)').get()
#             if price_whole:  # Ensure price_whole is not None
#                 price = price_whole + '.' +  (price_fraction if price_fraction else '')
#                 if name and link:
#                     game_data = {
#                         'name': name,
#                         'price': price,
#                         'link': response.urljoin(link),
#                         'image_url': image_url,
#                     }
#                     self.amazon_games_data.append(game_data)
#                     yield game_data


#     def closed(self, reason):
#         self.driver.quit()
#         print('----------- Scraped Games ---------------')
#         print('X-BOX')
#         print(self.xbox_games_data)
#         print('Amazon')
#         print(self.amazon_games_data)
