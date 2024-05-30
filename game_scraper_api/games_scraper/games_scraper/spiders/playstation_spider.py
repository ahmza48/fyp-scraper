

# PlayStation Store (https://store.playstation.com/)
# Amazon (https://www.amazon.com/) - Offers a wide range of PlayStation games
# Best Buy (https://www.bestbuy.com/) - Sells PlayStation games and consoles


# if user selects xbox as platform then xbox spider will scrape following sites:
# https://www.xbox.com/en-us/Search/Results?q=gta+5
# Microsoft Store (https://www.microsoft.com/en-us/store/games/windows)
# Amazon (https://www.amazon.com/) - Offers a variety of Xbox games
# GameStop (https://www.gamestop.com/) - Sells Xbox games and consoles


# and if user selects pc game as platform then pc games spider will scrape following sites:
# Steam (https://store.steampowered.com/) - One of the largest digital distribution platforms for PC games
# Epic Games Store (https://www.epicgames.com/store/en-US/) - Offers a range of PC games and exclusive titles
# GOG (https://www.gog.com/) - Focuses on DRM-free PC games



# import scrapy

# class PlaystationSpider(scrapy.Spider):
#     name = "playstation-spider"
#     allowed_domains = ["store.playstation.com","amazon.com","bestbuy.com"]
#     search_query='dragon ball z'
#     # if ' ' in search_query:
#     #     game_name=search_query.replace(' ', '%20')
#     # else:
#     #     game_name=search_query
#     game_name_playstation=search_query.replace(' ','%20')
#     game_name_amazon = search_query.replace(' ', '+')
#     game_name_bestbuy=search_query.replace(' ','+')

       
#     headers = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         "Accept-Language": "en-US,en;q=0.9,*",  # Consider broader language range
#         "Connection": "keep-alive",
#         "Upgrade-Insecure-Requests": "1",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
#     }

#     playstation_scraped_list = []
#     amazon_scraped_list = []
#     # bestbuy_scraped_list = []
    
#     def start_requests(self):
#         play_station_url = f"https://store.playstation.com/en-us/search/{self.search_query.replace(' ', '%20')}"
#         # bestbuy_url = f"https://www.bestbuy.com/site/searchpage.jsp?st={self.search_query.replace(' ', '+')}"
#         amazon_url = f"https://www.amazon.com/s?k={self.search_query.replace(' ', '+')}+playstation+game"

#         yield scrapy.Request(play_station_url, callback=self.parse_playstation)
#         yield scrapy.Request(amazon_url, callback=self.parse_amazon, headers=self.headers)
#         # yield scrapy.Request(bestbuy_url, callback=self.parse_amazon, headers=headers)

#     def parse_playstation(self, response):
#         print("Scraping PlayStation Store...")
#         games=response.css('.search-results div ul li')
#         game_number=0
#         if games is not None:
#             for game in games:
#                 name = game.xpath(f'.//span[@data-qa="search#productTile{game_number}#product-name"]/text()').get()               
#                 price = game.xpath(f'.//div[@data-qa="search#productTile{game_number}#price"]//span[@data-qa="search#productTile{game_number}#price#display-price"]/text()').get()

#                 image_url = game.xpath(f'.//span[@data-qa="search#productTile{game_number}#game-art#image"]//noscript/img/@src').get()

#                 game_number+=1
#                 link = f"https://store.playstation.com{game.css('div a').attrib['href']}"
#                 game_data = {
#                     'name': name,
#                     'price': price,
#                     'link': link,
#                     'image_url': image_url,
#                 }

#                 self.playstation_scraped_list.append(game_data)
#                 yield game_data

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
#                     self.amazon_scraped_list.append(game_data)
#                     yield game_data


#     def closed(self, reason):
#         # Print the lists after scraping is completed
#         print("\nPlayStation Scraped Data:")
#         print(self.playstation_scraped_list)
#         print("\nAmazon Scraped Data:")
#         print(self.amazon_scraped_list)
#         # print("\nBestBuy Scraped Data:")
#         # print(self.bestbuy_scraped_list)

# ------------------------------------------------------------------------------------

import scrapy
import json
class PlaystationSpider(scrapy.Spider):
    name = "playstation-spider"
    allowed_domains = ["store.playstation.com","amazon.com","bestbuy.com"]
    
    # search_query='dragon ball z'
    # game_name_playstation=search_query.replace(' ','%20')
    # game_name_amazon = search_query.replace(' ', '+')
    # game_name_bestbuy=search_query.replace(' ','+')

    
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
        self.game_name_playstation = search_query.replace(' ', '%20')
        self.game_name_amazon = search_query.replace(' ', '+')
        self.game_name_bestbuy = search_query.replace(' ', '+')
        
        # self.scraped_data={}
        self.scraped_data = []

        self.playstation_scraped_list = []
        self.amazon_scraped_list = []
        self.bestbuy_scraped_list = []

    # def start_requests(self):
    #     url = f'https://store.playstation.com/en-us/search/{self.search_query}'
    #     yield scrapy.Request(url, self.parse)

    def start_requests(self):
            play_station_url = f"https://store.playstation.com/en-us/search/{self.game_name_playstation}"
            amazon_url = f"https://www.amazon.com/s?k={self.game_name_amazon}+playstation+game"
            bestbuy_url = f"https://www.bestbuy.com/site/searchpage.jsp?st={self.search_query.replace(' ', '+')}+playstation&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys&intl=nosplash"
            yield scrapy.Request(play_station_url, callback=self.parse_playstation)
            yield scrapy.Request(amazon_url, callback=self.parse_amazon, headers=self.headers)
            yield scrapy.Request(bestbuy_url, callback=self.parse_bestbuy, headers=self.headers)
            

    # playstation_scraped_list = []
    # amazon_scraped_list = []
    # bestbuy_scraped_list = []
   
    # my working code
    #      
    # def start_requests(self):
    #     play_station_url = f"https://store.playstation.com/en-us/search/{self.search_query.replace(' ', '%20')}"
    #     # bestbuy_url = f"https://www.bestbuy.com/site/searchpage.jsp?st={self.search_query.replace(' ', '+')}"
    #     amazon_url = f"https://www.amazon.com/s?k={self.search_query.replace(' ', '+')}+playstation+game"

    #     yield scrapy.Request(play_station_url, callback=self.parse_playstation)
    #     yield scrapy.Request(amazon_url, callback=self.parse_amazon, headers=self.headers)
    #     # yield scrapy.Request(bestbuy_url, callback=self.parse_amazon, headers=headers)

    def parse_playstation(self, response):
        print("Scraping PlayStation Store...")
        games=response.css('.search-results div ul li')
        game_number=0
        if games is not None:
            while game_number<10:
                for game in games:
                    name = game.xpath(f'.//span[@data-qa="search#productTile{game_number}#product-name"]/text()').get()               
                    price = game.xpath(f'.//div[@data-qa="search#productTile{game_number}#price"]//span[@data-qa="search#productTile{game_number}#price#display-price"]/text()').get()

                    image_url = game.xpath(f'.//span[@data-qa="search#productTile{game_number}#game-art#image"]//noscript/img/@src').get()

                    game_number+=1
                    link = f"https://store.playstation.com{game.css('div a').attrib['href']}"
                    if name and image_url and link and '$' in price:
                        game_data = {
                            'name': name,
                            'price': price,
                            'link': link,
                            'image_url': image_url,
                        }
                        self.scraped_data.append(game_data)

                        self.playstation_scraped_list.append(game_data)
                        yield game_data

    def parse_amazon(self, response):
        # Extracting game information
        games = response.css('div.s-main-slot div.s-result-item')
        if not games:
            self.logger.info("No games found on Amazon page.")
        else:
            self.logger.info(f"Found {len(games)} games on Amazon page.")
        game_number=0
        while game_number < 10:
            for game in games:
                name = game.css('h2 span.a-text-normal::text').get()
                price_whole = game.css('span.a-price-whole::text').get()
                price_fraction = game.css('span.a-price-fraction::text').get()
                link = game.css('h2 a.a-link-normal::attr(href)').get()
                image_url = game.css('img.s-image::attr(src)').get()
                game_number+=1
                if price_whole:  # Ensure price_whole is not None
                    price = price_whole + '.' +  (price_fraction if price_fraction else '')
                    price='$'+price
                    if name and link:
                        game_data = {
                            'name': name,
                            'price': price,
                            'link': response.urljoin(link),
                            'image_url': image_url,
                        }
                        self.scraped_data.append(game_data)
                        self.amazon_scraped_list.append(game_data)
                        yield game_data

    def parse_bestbuy(self, response):
        # Parse product information from Best Buy using CSS selectors
        products = response.css('li.sku-item')
        for product in products:
            name = product.css('h4.sku-title a::text').get()
            price = product.css('div.priceView-hero-price span::text').get()
            image_url = product.css('img.product-image::attr(src)').get()  # Assuming an `img.product-image` element exists
            link = product.css('h4.sku-title a::attr(href)').get()
            if name and price and image_url and link:  # Check for all necessary data
                game_data = {
                    'name': name,
                    'price': price,
                    'link': response.urljoin(link),  # Construct absolute URL from relative link
                    'image_url': image_url
                }
                self.scraped_data.append(game_data)
                self.bestbuy_scraped_list.append(game_data)
                yield game_data


    def closed(self, reason):
        with open(self.output_file, 'w') as f:
            json.dump(self.scraped_data, f)
            
    # def closed(self, reason):
     
    #     self.scraped_data = {
    #         'playstation': self.playstation_scraped_list,
    #         'amazon': self.amazon_scraped_list,
    #     }
    #     print()
    #     print('DATA: ',data)
    #     print()
    #     # scraped_data = {
    #     #     'playstation': self.playstation_scraped_list,
    #     #     'amazon': self.amazon_scraped_list,
    #     # }
    #     self.logger.info("Scraped data ready.")
    #     yield scraped_data  # Yield the scraped data

    #     # scraped_data = {
    #     #     'playstation': self.playstation_scraped_list,
    #     #     'amazon': self.amazon_scraped_list,
    #     # }
    #     # yield scraped_data
        
    #     # scraped_data = {
    #     #     'playstation': self.playstation_scraped_list,
    #     #     'amazon': self.amazon_scraped_list,
    #     # }
    #     # return json.dumps(scraped_data)
        
    # def closed(self, reason):
    #     # Print the lists after scraping is completed
    #     print("\nPlayStation Scraped Data:")
    #     print(self.playstation_scraped_list)
    #     print("\nAmazon Scraped Data:")
    #     print(self.amazon_scraped_list)
    #     # print("\nBestBuy Scraped Data:")
    #     # print(self.bestbuy_scraped_list)
