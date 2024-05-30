

# # # PlayStation Store (https://store.playstation.com/)
# # # Amazon (https://www.amazon.com/) - Offers a wide range of PlayStation games
# # # Best Buy (https://www.bestbuy.com/) - Sells PlayStation games and consoles


# # # if user selects xbox as platform then xbox spider will scrape following sites:
# # # https://www.xbox.com/en-us/Search/Results?q=gta+5
# # # Microsoft Store (https://www.microsoft.com/en-us/store/games/windows)
# # # Amazon (https://www.amazon.com/) - Offers a variety of Xbox games
# # # GameStop (https://www.gamestop.com/) - Sells Xbox games and consoles


# # # and if user selects pc game as platform then pc games spider will scrape following sites:
# # # Steam (https://store.steampowered.com/) - One of the largest digital distribution platforms for PC games
# # # Epic Games Store (https://www.epicgames.com/store/en-US/) - Offers a range of PC games and exclusive titles
# # # GOG (https://www.gog.com/) - Focuses on DRM-free PC games


# # # import scrapy
# # # import json
# # # class PCSpider(scrapy.Spider):
# # #     name = "pc-spider"
# # #     allowed_domains = ["epicgames.com","humblebundle.com"]
# # #     # https://store.epicgames.com/en-US/browse?q=gta%20v&sortBy=relevancy&sortDir=DESC&count=40
# # #     headers = {
# # #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
# # #         "Accept-Language": "en-US,en;q=0.9,*",  # Consider broader language range
# # #         "Connection": "keep-alive",
# # #         "Upgrade-Insecure-Requests": "1",
# # #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
# # #     }

    
# # #     def __init__(self, search_query='', *args, **kwargs):
# # #         super().__init__(*args, **kwargs)
# # #         self.search_query = search_query
# # #         self.game_name_epicgames = search_query.replace(' ', '%20')
# # #         self.game_name_humblebundle = search_query.replace(' ', '%20')
        
# # #         # self.scraped_data={}
# # #         self.scraped_data = []

# # #         self.epicgames_scraped_list = []
# # #         self.humblebundle_scraped_list = []
# # #         # self.bestbuy_scraped_list = []
# # #     # def start_requests(self):
# # #     #     url = f'https://store.playstation.com/en-us/search/{self.search_query}'
# # #     #     yield scrapy.Request(url, self.parse)

# # #     def start_requests(self):
# # #             epicgames_url = f"https://store.epicgames.com/en-US/browse?q={self.game_name_epicgames}"
# # #             humblebundle_url = f"humblebundle.com/store/search?search={self.game_name_humblebundle}"

# # #             yield scrapy.Request(epicgames_url, callback=self.parse_epicgames, headers=self.headers)
# # #             # yield scrapy.Request(humblebundle_url, callback=self.parse_humblebundle, headers=self.headers)

# # #     # my working code
# # #     #      
# # #     # def start_requests(self):
# # #     #     play_station_url = f"https://store.playstation.com/en-us/search/{self.search_query.replace(' ', '%20')}"
# # #     #     # bestbuy_url = f"https://www.bestbuy.com/site/searchpage.jsp?st={self.search_query.replace(' ', '+')}"
# # #     #     amazon_url = f"https://www.amazon.com/s?k={self.search_query.replace(' ', '+')}+playstation+game"

# # #     #     yield scrapy.Request(play_station_url, callback=self.parse_playstation)
# # #     #     yield scrapy.Request(amazon_url, callback=self.parse_amazon, headers=self.headers)
# # #     #     # yield scrapy.Request(bestbuy_url, callback=self.parse_amazon, headers=headers)

# # #     def parse_epicgames(self, response):
# # #         section = response.xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/div/section/div/section/div/section/section')
# # #         for li in section.xpath('./ul/li'):
# # #             name = li.xpath('.//div[@data-component="DiscoverOfferCard"]/a/div[@class="css-1a6kj04"]/span[@class="css-1825rs2"]/span/text()').get()
# # #             price = li.xpath('.//div[@data-component="DiscoverOfferCard"]/a/div[@class="css-1a6kj04"]/div[@class="css-1q7njkh"]/div/div/div[@class="css-o1hbmr"]/div/span/text()').get()
# # #             image_url = li.xpath('.//div[@data-component="DiscoverOfferCard"]/a/div[@class="css-1a6kj04"]/div[@class="css-1lozana"]/div/div/div/div/div[@class="css-uwwqev"]/div/img/@src').get()
# # #             link = li.xpath('.//div[@data-component="DiscoverOfferCard"]/a/@href').get()
# # #             if name and price and image_url and link:
# # #                 game_data = {
# # #                     'name': name,
# # #                     'price': price,
# # #                     'link': link,
# # #                     'image_url': image_url,   
# # #                 }
# # #                 self.scraped_data.append(game_data)
# # #                 self.epicgames_scraped_list.append(game_data)
# # #                 yield game_data


# # #     def parse_amazon(self, response):
# # #         # Extracting game information
# # #         games = response.css('div.s-main-slot div.s-result-item')
# # #         if not games:
# # #             self.logger.info("No games found on Amazon page.")
# # #         else:
# # #             self.logger.info(f"Found {len(games)} games on Amazon page.")
# # #         game_number=0
# # #         while game_number < 10:
# # #             for game in games:
# # #                 name = game.css('h2 span.a-text-normal::text').get()
# # #                 price_whole = game.css('span.a-price-whole::text').get()
# # #                 price_fraction = game.css('span.a-price-fraction::text').get()
# # #                 link = game.css('h2 a.a-link-normal::attr(href)').get()
# # #                 image_url = game.css('img.s-image::attr(src)').get()
# # #                 game_number+=1
# # #                 if price_whole:  # Ensure price_whole is not None
# # #                     price = price_whole + '.' +  (price_fraction if price_fraction else '')
# # #                     price='$'+price
# # #                     if name and link:
# # #                         game_data = {
# # #                             'name': name,
# # #                             'price': price,
# # #                             'link': response.urljoin(link),
# # #                             'image_url': image_url,
# # #                         }
# # #                         self.scraped_data.append(game_data)
# # #                         self.amazon_scraped_list.append(game_data)
# # #                         yield game_data



# # #     def closed(self, reason):
# # #         with open(self.output_file, 'w') as f:
# # #             json.dump(self.scraped_data, f)

# # import scrapy
# # import json
# # import time
# # from scrapy.http import HtmlResponse
# # from selenium import webdriver

# # class PCSpider(scrapy.Spider):
# #     name = "pc-spider"
# #     allowed_domains = ["epicgames.com"]
# #     headers = {
# #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
# #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
# #         "Accept-Language": "en-US,en;q=0.9,*",
# #         "Connection": "keep-alive",
# #         "Upgrade-Insecure-Requests": "1"
# #     }
# #     def __init__(self, search_query='', *args, **kwargs):
# #         super().__init__(*args, **kwargs)
# #         self.search_query = search_query
# #         self.game_name_epicgames = search_query.replace(' ', '%20')
# #         self.scraped_data = []
# #         self.epicgames_scraped_list = []

# #         options = webdriver.ChromeOptions()
# #         options.add_argument('--headless')
# #         options.add_argument('--no-sandbox')
# #         options.add_argument('--disable-dev-shm-usage')
# #         options.add_argument('--disable-gpu')
# #         options.add_argument('--window-size=1920x1080')
# #         options.add_argument('--disable-blink-features=AutomationControlled')
# #         self.driver = webdriver.Chrome(options=options)

# #     def start_requests(self):
# #         epicgames_url = f"https://store.epicgames.com/en-US/browse?q={self.game_name_epicgames}"
# #         yield scrapy.Request(epicgames_url, callback=self.parse_epicgames, headers=self.headers)

# #     def parse_epicgames(self, response):
# #         # Wait for the page to load
# #         time.sleep(3)

# #         self.driver.get(response.url)
# #         html_content = self.driver.page_source
        
# #         # Create an HtmlResponse object to parse with Scrapy
# #         scrapy_response = HtmlResponse(url=response.url, body=html_content, encoding='utf-8')

# #         section = scrapy_response.xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/div/section/div/section/div/section/section')
# #         for li in section.xpath('./ul/li'):
# #             name = li.xpath('.//div[@data-component="DiscoverOfferCard"]/a/div[@class="css-1a6kj04"]/span[@class="css-1825rs2"]/span/text()').get()
# #             price = li.xpath('.//div[@data-component="DiscoverOfferCard"]/a/div[@class="css-1a6kj04"]/div[@class="css-1q7njkh"]/div/div/div[@class="css-o1hbmr"]/div/span/text()').get()
# #             image_url = li.xpath('.//div[@data-component="DiscoverOfferCard"]/a/div[@class="css-1a6kj04"]/div[@class="css-1lozana"]/div/div/div/div/div[@class="css-uwwqev"]/div/img/@src').get()
# #             link = li.xpath('.//div[@data-component="DiscoverOfferCard"]/a/@href').get()
# #             if name and price and image_url and link:
# #                 game_data = {
# #                     'name': name,
# #                     'price': price,
# #                     'link': link,
# #                     'image_url': image_url,
# #                 }
# #                 self.scraped_data.append(game_data)
# #                 self.epicgames_scraped_list.append(game_data)
# #                 yield game_data

# #     def closed(self, reason):
# #         self.driver.quit()
# #         with open(self.output_file, 'w') as f:
# #             json.dump(self.scraped_data, f)


# #     # def closed(self, reason):
     
# #     #     self.scraped_data = {
# #     #         'playstation': self.playstation_scraped_list,
# #     #         'amazon': self.amazon_scraped_list,
# #     #     }
# #     #     print()
# #     #     print('DATA: ',data)
# #     #     print()
# #     #     # scraped_data = {
# #     #     #     'playstation': self.playstation_scraped_list,
# #     #     #     'amazon': self.amazon_scraped_list,
# #     #     # }
# #     #     self.logger.info("Scraped data ready.")
# #     #     yield scraped_data  # Yield the scraped data

# #     #     # scraped_data = {
# #     #     #     'playstation': self.playstation_scraped_list,
# #     #     #     'amazon': self.amazon_scraped_list,
# #     #     # }
# #     #     # yield scraped_data
        
# #     #     # scraped_data = {
# #     #     #     'playstation': self.playstation_scraped_list,
# #     #     #     'amazon': self.amazon_scraped_list,
# #     #     # }
# #     #     # return json.dumps(scraped_data)
        
# #     # def closed(self, reason):
# #     #     # Print the lists after scraping is completed
# #     #     print("\nPlayStation Scraped Data:")
# #     #     print(self.playstation_scraped_list)
# #     #     print("\nAmazon Scraped Data:")
# #     #     print(self.amazon_scraped_list)
# #     #     # print("\nBestBuy Scraped Data:")
# #     #     # print(self.bestbuy_scraped_list)

# # # <section class="css-zjpm9r"><ul class="css-cnqlhg"><li class="css-lrwy1y"><div><div class="css-2mlzob" data-component="DiscoverOfferCard"><a class="css-g3jcms" aria-label="1 of 7, Base Game, Grand Theft Auto V: Premium Edition, -50%, $29.99, $14.99" href="/en-US/p/grand-theft-auto-v"><div class="css-914cl7"><div class="css-eix8c6"><div class="css-1lozana" data-testid="offer-card-image-portrait"><div class="css-767s3d"><div class="css-uwwqev"><div class="css-uwwqev" data-testid="picture"><img alt="Grand Theft Auto V: Premium Edition" src="https://cdn1.epicgames.com/0584d2013f0149a791e7b9bad0eec102/offer/GTAV_EGS_Artwork_1200x1600_Portrait Store Banner-1200x1600-382243057711adf80322ed2aeea42191.jpg?h=480&amp;quality=medium&amp;resize=1&amp;w=360" class="css-1ae5wog" data-image="https://cdn1.epicgames.com/0584d2013f0149a791e7b9bad0eec102/offer/GTAV_EGS_Artwork_1200x1600_Portrait Store Banner-1200x1600-382243057711adf80322ed2aeea42191.jpg?h=480&amp;quality=medium&amp;resize=1&amp;w=360" data-testid="picture-image"></div></div></div></div></div><div class="css-1a6kj04"><span class="css-1825rs2"><span>Base Game</span></span><div class="css-s98few"><span class="css-119zqif"><div class="css-lgj0h8"><div class="css-rgqwpc">Grand Theft Auto V: Premium Edition</div></div></span></div><div class="css-10kqwxf"></div><div class="css-1q7njkh"><div class="css-u4p24i"><div class="css-l24hbj"><span class="css-1kn2h2p"><div class="css-1q7f74q">-50%</div></span></div><div class="css-l24hbj"><div class="css-o1hbmr"><div class="css-l24hbj"><span class="css-d3i3lr"><div class="css-4jky3p">$29.99</div></span></div><div class="css-l24hbj"><span class="css-119zqif">$14.99</span></div></div></div></div></div></div></div></a><div class="css-b3olj2"><button class="css-138bf6p" aria-label="Add to Wishlist"><div class="css-hf2oq1" data-testid="wishbutton-circle"><div data-testid="spinner" class="css-t40d20"></div></div></button></div></div></div></li><li class="css-lrwy1y"><div><div class="css-2mlzob" data-component="DiscoverOfferCard"><a class="css-g3jcms" aria-label="2 of 7, Base Game, 3D City: Metaverse, Free" href="/en-US/p/3d-city-32fc13"><div class="css-914cl7"><div class="css-eix8c6"><div class="css-1lozana" data-testid="offer-card-image-portrait"><div class="css-767s3d"><div class="css-uwwqev"><div class="css-uwwqev" data-testid="picture"><img alt="3D City: Metaverse" src="https://cdn1.epicgames.com/spt-assets/ecc3d079fae84c089473da1960a1822f/3d-city-8a384.png?h=480&amp;quality=medium&amp;resize=1&amp;w=360" class="css-1ae5wog" data-image="https://cdn1.epicgames.com/spt-assets/ecc3d079fae84c089473da1960a1822f/3d-city-8a384.png?h=480&amp;quality=medium&amp;resize=1&amp;w=360" data-testid="picture-image"></div></div></div></div></div><div class="css-1a6kj04"><span class="css-1825rs2"><span>Base Game</span></span><div class="css-s98few"><span class="css-119zqif"><div class="css-lgj0h8"><div class="css-rgqwpc">3D City: Metaverse</div></div></span></div><div class="css-10kqwxf"></div><div class="css-1q7njkh"><div class="css-u4p24i"><div class="css-l24hbj"><div class="css-o1hbmr"><div class="css-l24hbj"><span class="css-119zqif"><span>Free</span></span></div></div></div></div></div></div></div></a><div class="css-b3olj2"><button class="css-138bf6p" aria-label="Add to Wishlist"><div class="css-hf2oq1" data-testid="wishbutton-circle"><div data-testid="spinner" class="css-t40d20"></div></div></button></div></div></div></li><li class="css-lrwy1y"><div><div class="css-2mlzob" data-component="DiscoverOfferCard"><a class="css-g3jcms" aria-label="3 of 7, Add-On, HOT WHEELS UNLEASHED™ 2 - Fast X Pack, -50%, $4.99, $2.49" href="/en-US/p/hot-wheels-unleashed-2--fast-x-pack"><div class="css-914cl7"><div class="css-eix8c6"><div class="css-1lozana" data-testid="offer-card-image-portrait"><div class="css-767s3d"><div class="css-uwwqev"><div class="css-uwwqev" data-testid="picture"><img alt="HOT WHEELS UNLEASHED™ 2 - Fast X Pack" src="https://cdn1.epicgames.com/offer/552a139c67e949ea8f8ea9a1d9d81cdb/EGS_HOTWHEELSUNLEASHED2FastXPack_MilestoneSrl_DLC_S2_1200x1600-29332b989562188ee2d12d6f9afb05e9?h=480&amp;quality=medium&amp;resize=1&amp;w=360" class="css-1ae5wog" data-image="https://cdn1.epicgames.com/offer/552a139c67e949ea8f8ea9a1d9d81cdb/EGS_HOTWHEELSUNLEASHED2FastXPack_MilestoneSrl_DLC_S2_1200x1600-29332b989562188ee2d12d6f9afb05e9?h=480&amp;quality=medium&amp;resize=1&amp;w=360" data-testid="picture-image"></div></div></div></div></div><div class="css-1a6kj04"><span class="css-1825rs2"><span>Add-On</span></span><div class="css-s98few"><span class="css-119zqif"><div class="css-lgj0h8"><div class="css-rgqwpc">HOT WHEELS UNLEASHED™ 2 - Fast X Pack</div></div></span></div><div class="css-10kqwxf"></div><div class="css-1q7njkh"><div class="css-u4p24i"><div class="css-l24hbj"><span class="css-1kn2h2p"><div class="css-1q7f74q">-50%</div></span></div><div class="css-l24hbj"><div class="css-o1hbmr"><div class="css-l24hbj"><span class="css-d3i3lr"><div class="css-4jky3p">$4.99</div></span></div><div class="css-l24hbj"><span class="css-119zqif">$2.49</span></div></div></div></div></div></div></div></a><div class="css-b3olj2"><button class="css-138bf6p" aria-label="Add to Wishlist"><div class="css-hf2oq1" data-testid="wishbutton-circle"><div data-testid="spinner" class="css-t40d20"></div></div></button></div></div></div></li><li class="css-lrwy1y"><div><div class="css-2mlzob" data-component="DiscoverOfferCard"><a class="css-g3jcms" aria-label="4 of 7, Base Game, Grand Theft Auto: Vice City – The Definitive Edition" href="/en-US/p/grand-theft-auto-vice-city-the-definitive-edition"><div class="css-914cl7"><div class="css-eix8c6"><div class="css-1lozana" data-testid="offer-card-image-portrait"><div class="css-767s3d"><div class="css-uwwqev"><div class="css-uwwqev" data-testid="picture"><img alt="Grand Theft Auto: Vice City – The Definitive Edition" src="https://cdn1.epicgames.com/offer/fd6a13a256014a22a83ff2aaacc30e00/EGS_GrandTheftAutoViceCityTheDefinitiveEdition_RockstarGames_S2_1200x1600-18ac3dd32143492b2650144da0cf0ca9?h=480&amp;quality=medium&amp;resize=1&amp;w=360" class="css-1ae5wog" data-image="https://cdn1.epicgames.com/offer/fd6a13a256014a22a83ff2aaacc30e00/EGS_GrandTheftAutoViceCityTheDefinitiveEdition_RockstarGames_S2_1200x1600-18ac3dd32143492b2650144da0cf0ca9?h=480&amp;quality=medium&amp;resize=1&amp;w=360" data-testid="picture-image"></div></div></div></div></div><div class="css-1a6kj04"><span class="css-1825rs2"><span>Base Game</span></span><div class="css-s98few"><span class="css-119zqif"><div class="css-lgj0h8"><div class="css-rgqwpc">Grand Theft Auto: Vice City – The Definitive Edition</div></div></span></div><div class="css-10kqwxf"></div></div></div></a><div class="css-b3olj2"><button class="css-138bf6p" aria-label="Add to Wishlist"><div class="css-hf2oq1" data-testid="wishbutton-circle"><div data-testid="spinner" class="css-t40d20"></div></div></button></div></div></div></li><li class="css-lrwy1y"><div><div class="css-2mlzob" data-component="DiscoverOfferCard"><a class="css-g3jcms" aria-label="5 of 7, Base Game, Grand Theft Auto: San Andreas – The Definitive Edition" href="/en-US/p/grand-theft-auto-san-andreas-the-definitive-edition"><div class="css-914cl7"><div class="css-eix8c6"><div class="css-1lozana" data-testid="offer-card-image-portrait"><div class="css-767s3d"><div class="css-uwwqev"><div class="css-uwwqev" data-testid="picture"><img alt="Grand Theft Auto: San Andreas – The Definitive Edition" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" class="css-b664ty" data-image="https://cdn1.epicgames.com/offer/3262906d93334603b399e106492b1217/EGS_GrandTheftAutoSanAndreasTheDefinitiveEdition_RockstarGames_S2_1200x1600-31b942afca6472306be8ae9dfa73290e?h=480&amp;quality=medium&amp;resize=1&amp;w=360" data-testid="picture-image"></div></div></div></div></div><div class="css-1a6kj04"><span class="css-1825rs2"><span>Base Game</span></span><div class="css-s98few"><span class="css-119zqif"><div class="css-lgj0h8"><div class="css-rgqwpc">Grand Theft Auto: San Andreas – The Definitive Edition</div></div></span></div><div class="css-10kqwxf"></div></div></div></a><div class="css-b3olj2"><button class="css-138bf6p" aria-label="Add to Wishlist"><div class="css-hf2oq1" data-testid="wishbutton-circle"><div data-testid="spinner" class="css-t40d20"></div></div></button></div></div></div></li><li class="css-lrwy1y"><div><div class="css-2mlzob" data-component="DiscoverOfferCard"><a class="css-g3jcms" aria-label="6 of 7, Base Game, Grand Theft Auto III – The Definitive Edition" href="/en-US/p/grand-theft-auto-iii-the-definitive-edition"><div class="css-914cl7"><div class="css-eix8c6"><div class="css-1lozana" data-testid="offer-card-image-portrait"><div class="css-767s3d"><div class="css-uwwqev"><div class="css-uwwqev" data-testid="picture"><img alt="Grand Theft Auto III – The Definitive Edition" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" class="css-b664ty" data-image="https://cdn1.epicgames.com/offer/ec64a50e79884e28be9ac3d3cd4f5c12/EGS_GrandTheftAutoIIITheDefinitiveEdition_RockstarGames_S2_1200x1600-951dfab28dd4c6d61bfe7bb360a349fc?h=480&amp;quality=medium&amp;resize=1&amp;w=360" data-testid="picture-image"></div></div></div></div></div><div class="css-1a6kj04"><span class="css-1825rs2"><span>Base Game</span></span><div class="css-s98few"><span class="css-119zqif"><div class="css-lgj0h8"><div class="css-rgqwpc">Grand Theft Auto III – The Definitive Edition</div></div></span></div><div class="css-10kqwxf"></div></div></div></a><div class="css-b3olj2"><button class="css-138bf6p" aria-label="Add to Wishlist"><div class="css-hf2oq1" data-testid="wishbutton-circle"><div data-testid="spinner" class="css-t40d20"></div></div></button></div></div></div></li><li class="css-lrwy1y"><div><div class="css-2mlzob" data-component="DiscoverOfferCard"><a class="css-g3jcms" aria-label="7 of 7, Bundle, Grand Theft Auto: The Trilogy – The Definitive Edition, -50%, $59.99, $29.99" href="/en-US/bundles/grand-theft-auto-the-trilogy-the-definitive-edition"><div class="css-914cl7"><div class="css-eix8c6"><div class="css-1lozana" data-testid="offer-card-image-portrait"><div class="css-767s3d"><div class="css-uwwqev"><div class="css-uwwqev" data-testid="picture"><img alt="Grand Theft Auto: The Trilogy – The Definitive Edition" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" class="css-b664ty" data-image="https://cdn1.epicgames.com/offer/fe752703dd2042008ff874fc8642fba3/EGS_GrandTheftAutoTheTrilogyTheDefinitiveEdition_RockstarGames_S2_1200x1600-7a39d7c91aed7cf7c5fafdca4dbb9d1c?h=480&amp;quality=medium&amp;resize=1&amp;w=360" data-testid="picture-image"></div></div></div></div></div><div class="css-1a6kj04"><span class="css-1825rs2"><span>Bundle</span></span><div class="css-s98few"><span class="css-119zqif"><div class="css-lgj0h8"><div class="css-rgqwpc">Grand Theft Auto: The Trilogy – The Definitive Edition</div></div></span></div><div class="css-10kqwxf"></div><div class="css-1q7njkh"><div class="css-u4p24i"><div class="css-l24hbj"><span class="css-1kn2h2p"><div class="css-1q7f74q">-50%</div></span></div><div class="css-l24hbj"><div class="css-o1hbmr"><div class="css-l24hbj"><span class="css-d3i3lr"><div class="css-4jky3p">$59.99</div></span></div><div class="css-l24hbj"><span class="css-119zqif">$29.99</span></div></div></div></div></div></div></div></a><div class="css-b3olj2"><button class="css-138bf6p" aria-label="Add to Wishlist"><div class="css-hf2oq1" data-testid="wishbutton-circle"><div data-testid="spinner" class="css-t40d20"></div></div></button></div></div></div></li></ul></section>
# import requests
# from bs4 import BeautifulSoup
# import json
# import sys

# def scrape_epic_games(search_query):
#     url = f"https://store.epicgames.com/en-US/browse?q={search_query}"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }

#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.content, "html.parser")

#     games = []
#     for li in soup.select('div[data-component="DiscoverOfferCard"]'):
#         name = li.select_one('.css-rgqwpc').text.strip()
#         price = li.select_one('.css-d3i3lr').text.strip()
#         image_url = li.select_one('img')['src']
#         link = li.select_one('a')['href']

#         game_data = {
#             'name': name,
#             'price': price,
#             'image_url': image_url,
#             'link': link
#         }
#         games.append(game_data)

#     return games

# if __name__ == "__main__":
#     search_query = sys.argv[1] if len(sys.argv) > 1 else ""
#     scraped_data = scrape_epic_games(search_query)
#     print(json.dumps(scraped_data, indent=4))
