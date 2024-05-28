from django.http import JsonResponse
from django.views import View
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy import signals
from twisted.internet import reactor
import tempfile
import json
import os

from games_scraper.games_scraper.spiders import playstation_spider
from games_scraper.games_scraper.spiders import xbox_spider

class ScrapeGameView(View):
    def get(self, request, *args, **kwargs):
        game_name = request.GET.get('game_name')
        platform = request.GET.get('platform')

        if not game_name or not platform:
            return JsonResponse({'error': 'game_name and platform are required parameters.'}, status=400)

        spider_name = f"{platform.lower()}_spider"
        try:
            # Run the spider and capture the output
            results = self.run_spider(spider_name, game_name)
            return JsonResponse(results, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def run_spider(self, spider_name, game_name):
        settings = get_project_settings()
        process = CrawlerProcess(settings)

        if spider_name == 'playstation_spider':
            spider_class = playstation_spider.PlaystationSpider
        elif spider_name == 'xbox_spider':
            spider_class = xbox_spider.XboxSpider
        elif spider_name == 'pc_spider':
            spider_class = pc_spider.PCSpider
        else:
            raise Exception(f"Spider '{spider_name}' not found.")



        
        output_file = tempfile.mktemp()

        def spider_closing(spider):
            reactor.stop()

        crawler = process.create_crawler(spider_class)
        crawler.signals.connect(spider_closing, signal=signals.spider_closed)
        process.crawl(crawler, search_query=game_name, output_file=output_file)
        process.start()

        with open(output_file, 'r') as f:
            results = json.load(f)

        os.remove(output_file)

        return results

# from django.shortcuts import render

# from django.http import JsonResponse
# from django.views import View
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# import tempfile
# import os
# import sys
# import json
# import importlib
# from scrapy.spiders import Spider

# from games_scraper.games_scraper.spiders import playstation_spider

# class ScrapeGameView(View):
#     def get(self, request, *args, **kwargs):
#         game_name = request.GET.get('game_name')
#         platform = request.GET.get('platform')

#         if not game_name or not platform:
#             return JsonResponse({'error': 'game_name and platform are required parameters.'}, status=400)

#         spider_name = f"{platform.lower()}_spider"
#         try:
#             # Run the spider and capture the output
#             results = self.run_spider(spider_name, game_name)
#             return JsonResponse(results, safe=False)
#         except Exception as e:
#             print('YAKKIIII')
#             return JsonResponse({'error': str(e)}, status=500)

#         # try:
#         #     # Dynamically import the spider class with full path
#         #     spider_module_path = f"games_scraper.spiders.{spider_name}"
#         #     spider_module = importlib.import_module(spider_module_path)
#         #     spider_class = getattr(spider_module, spider_name)
#         #     if not issubclass(spider_class, Spider):
#         #         raise Exception(f"Class '{spider_name}' is not a Scrapy spider.")

#         #     # Run the spider with the game name
#         #     results = self.run_spider(spider_class, game_name)
#         #     return JsonResponse(results, safe=False)
#         # except Exception as e:
#         #     return JsonResponse({'error': str(e)}, status=500)
#         # try:
#         #     # Run the spider and capture the output
#         #     results = self.run_spider(spider_name, game_name)
#         #     return JsonResponse(results, safe=False)
#         # except Exception as e:
#         #     return JsonResponse({'error': str(e)}, status=500)

#     def run_spider(self, spider_name, game_name):
#         # Setup Scrapy settings
#         try:
#             settings = get_project_settings()
#             process = CrawlerProcess(settings)

#             # Temporary file to store the results
#             output_file = tempfile.mktemp()

#             # Define the custom settings for the spider
#             custom_settings = {
#                 'FEED_FORMAT': 'json',
#                 'FEED_URI': output_file
#             }

#             # print('spider name: ', spider_name)

#             if spider_name == 'playstation_spider':
#                 spider_class = playstation_spider.PlaystationSpider
#                 # print('spider CLASS: ', spider_class)
#             elif spider_name == 'xbox_spider':
#                 spider_class = XboxSpider
#             elif spider_name == 'pc_spider':
#                 spider_class = pcSpider
#             else:
#                 raise Exception(f"Spider '{spider_name}' not found.")



#             process.crawl(spider_class, search_query=game_name, custom_settings=custom_settings)
#             process.start()
#             # List to hold the scraped data
#             scraped_data = []

#             def spider_closing(spider):
#                 # Collect the data from the spider instance
#                 scraped_data.extend(spider.data)
#                 reactor.stop()

#             crawler = process.create_crawler(spider_class)
#             crawler.signals.connect(spider_closing, signal=signals.spider_closed)
#             process.crawl(crawler, search_query=game_name)
#             process.start()  # Blocking call, will stop once the reactor is stopped

#             return scraped_data

            
#             # return results
#         except Exception as e:
#             print(str(e))
#             return str(e)

# -----------------------------------------------------------------------------------------------------

# def run_spider(self, spider_name, game_name):
#     settings = get_project_settings()
#     process = CrawlerProcess(settings)

#     if spider_name == 'playstation_spider':
#         spider_class = playstation_spider.PlaystationSpider
#     else:
#         raise Exception(f"Spider '{spider_name}' not found.")

#     scraped_data = []

#     def spider_closing(spider):
#         scraped_data.extend(spider.data['playstation'])
#         scraped_data.extend(spider.data['amazon'])
#         reactor.stop()

#     crawler = process.create_crawler(spider_class)
#     crawler.signals.connect(spider_closing, signal=signals.spider_closed)
#     process.crawl(crawler, search_query=game_name)
#     process.start()

#     print(f"Scraped data: {scraped_data}")  # Log the scraped data
#     return scraped_data
