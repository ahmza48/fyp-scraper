# from django.http import JsonResponse
# from django.views import View
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from scrapy import signals
# from twisted.internet import reactor
# import tempfile
# import json
# import os

# from games_scraper.games_scraper.spiders import playstation_spider
# from games_scraper.games_scraper.spiders import xbox_spider

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
#             return JsonResponse({'error': str(e)}, status=500)

#     def run_spider(self, spider_name, game_name):
#         settings = get_project_settings()
#         process = CrawlerProcess(settings)

#         if spider_name == 'playstation_spider':
#             spider_class = playstation_spider.PlaystationSpider
#         elif spider_name == 'xbox_spider':
#             spider_class = xbox_spider.XboxSpider
#         elif spider_name == 'pc_spider':
#             spider_class = pc_spider.PCSpider
#         else:
#             raise Exception(f"Spider '{spider_name}' not found.")



        
#         output_file = tempfile.mktemp()

#         def spider_closing(spider):
#             reactor.stop()

#         crawler = process.create_crawler(spider_class)
#         crawler.signals.connect(spider_closing, signal=signals.spider_closed)
#         process.crawl(crawler, search_query=game_name, output_file=output_file)
#         process.start()

#         with open(output_file, 'r') as f:
#             results = json.load(f)

#         os.remove(output_file)

#         return results

from django.http import JsonResponse
from django.views import View
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy import signals
from twisted.internet import reactor
import tempfile
import json
import os
from twisted.internet import reactor, defer  # Import defer explicitly

from games_scraper.games_scraper.spiders import playstation_spider
from games_scraper.games_scraper.spiders import xbox_spider

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
#             return JsonResponse({'error': str(e)}, status=500)

#     def run_spider(self, spider_name, game_name):
#         settings = get_project_settings()
#         process = CrawlerProcess(settings)

#         if spider_name == 'playstation_spider':
#             spider_class = playstation_spider.PlaystationSpider
#         elif spider_name == 'xbox_spider':
#             spider_class = xbox_spider.XboxSpider
#         elif spider_name == 'pc_spider':
#             spider_class = pc_spider.PCSpider
#         else:
#             raise Exception(f"Spider '{spider_name}' not found.")

#         output_file = tempfile.mktemp()

#         deferred = defer.Deferred()

#         def handle_results(results):
#             deferred.callback(results)
#             # Remove temporary file after scraping
#             os.remove(output_file)

#         crawler = process.create_crawler(spider_class)
#         crawler.signals.connect(handle_results, signal=signals.item_scraped)
#         print('BEFORE CRAWL')
#         process.crawl(crawler, search_query=game_name, output_file=output_file)
#         print('BEFORE Start')
#         deferred.addCallback(lambda results: reactor.stop())
#         process.start()  # Start the process even before waiting for completion
#         # Wait for results using callback (modified line)
#         def handle_deferred_result(result):
#             return result

#         deferred.addCallback(handle_deferred_result)
#         return deferred

#         results = self.run_spider(spider_name, game_name)
#         return JsonResponse(results, safe=False)
# ---------------------------------------------------------------------
# from django.http import JsonResponse
# from django.views import View
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from scrapy import signals
# from twisted.internet import reactor, defer  # Import defer explicitly
# import tempfile
# import json
# import os

# from games_scraper.games_scraper.spiders import playstation_spider
# from games_scraper.games_scraper.spiders import xbox_spider

# import warnings
# warnings.filterwarnings('ignore')
# from django.http import JsonResponse
# from django.views import View
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from scrapy import signals
# import tempfile
# import json
# import os
# import threading
# import logging
# from games_scraper.games_scraper.spiders import playstation_spider, xbox_spider
# from twisted.internet import reactor

# class ScrapeGameView(View):
#     def get(self, request, *args, **kwargs):
#         game_name = request.GET.get('game_name')
#         platform = request.GET.get('platform')

#         if not game_name or not platform:
#             return JsonResponse({'error': 'game_name and platform are required parameters.'}, status=400)

#         spider_name = f"{platform.lower()}_spider"
#         try:
#             # Run the spider and capture the output
#             output = self.run_spider(spider_name, game_name)
#             return JsonResponse(output, safe=False)
#         except Exception as e:
#             logging.error("An error occurred while running the spider: %s", str(e))
#             return JsonResponse({'error': str(e)}, status=500)

#     def run_spider(self, spider_name, game_name):
#         settings = get_project_settings()
#         process = CrawlerProcess(settings)

#         if spider_name == 'playstation_spider':
#             spider_class = playstation_spider.PlaystationSpider
#         elif spider_name == 'xbox_spider':
#             spider_class = xbox_spider.XboxSpider
#         else:
#             raise Exception(f"Spider '{spider_name}' not found.")

#         output_file = tempfile.mktemp()

#         def run_crawler():
#             deferred = process.crawl(spider_class, search_query=game_name, output_file=output_file)
#             deferred.addCallback(self.spider_closing, output_file)
#             deferred.addErrback(self.spider_error)
#             process.start()
#             reactor.stop()

#         thread = threading.Thread(target=run_crawler)
#         thread.start()
#         thread.join()

#         with open(output_file, 'r') as f:
#             results = json.load(f)

#         os.remove(output_file)
#         return results

#     def spider_closing(self, _):
#         # Function to handle the closing of the spider
#         pass

#     def spider_error(self, failure):
#         logging.error(failure)
#         raise Exception(f"Spider error: {failure}")

# here pyn yakki starts
# ----------------------------------------------------------------------------------
# import warnings
# warnings.filterwarnings('ignore')
# from django.http import JsonResponse
# from django.views import View
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from scrapy import signals
# import tempfile
# import json
# import os
# import threading
# import logging
# from games_scraper.games_scraper.spiders import playstation_spider, xbox_spider
# from twisted.internet import reactor
# import time

# class ScrapeGameView(View):
#     def get(self, request, *args, **kwargs):
#         game_name = request.GET.get('game_name')
#         platform = request.GET.get('platform')

#         if not game_name or not platform:
#             return JsonResponse({'error': 'game_name and platform are required parameters.'}, status=400)

#         spider_name = f"{platform.lower()}_spider"
#         try:
#             # Run the spider and capture the output
#             output = self.run_spider(spider_name, game_name)
#             return JsonResponse(output, safe=False)
#         except Exception as e:
#             logging.error("An error occurred while running the spider: %s", str(e))
#             return JsonResponse({'error': str(e)}, status=500)

#     def run_spider(self, spider_name, game_name):
#         settings = get_project_settings()
#         process = CrawlerProcess(settings)

#         if spider_name == 'playstation_spider':
#             spider_class = playstation_spider.PlaystationSpider
#         elif spider_name == 'xbox_spider':
#             spider_class = xbox_spider.XboxSpider
#         else:
#             raise Exception(f"Spider '{spider_name}' not found.")

#         output_file = tempfile.mktemp()

#         def run_crawler():
#             deferred = process.crawl(spider_class, search_query=game_name, output_file=output_file)
#             deferred.addCallback(self.spider_closing, output_file)
#             deferred.addErrback(self.spider_error)
#             process.start(stop_after_crawl=False)
#             reactor.stop()

#         thread = threading.Thread(target=run_crawler)
#         thread.start()
#         thread.join()

#         with open(output_file, 'r') as f:
#             results = json.load(f)

#         os.remove(output_file)
#         return results

#     def spider_closing(self, _):
#         # Function to handle the closing of the spider
#         pass

#     def spider_error(self, failure):
#         logging.error(failure)
#         raise Exception(f"Spider error: {failure}")

import warnings
warnings.filterwarnings('ignore')
from django.http import JsonResponse
from django.views import View
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy import signals
import tempfile
import json
import os
import threading
import logging
from games_scraper.games_scraper.spiders import playstation_spider, xbox_spider
from twisted.internet import reactor
from twisted.internet.task import react

class ScrapeGameView(View):
    process = None

    def get(self, request, *args, **kwargs):
        game_name = request.GET.get('game_name')
        platform = request.GET.get('platform')

        if not game_name or not platform:
            return JsonResponse({'error': 'game_name and platform are required parameters.'}, status=400)

        spider_name = f"{platform.lower()}_spider"
        try:
            # Run the spider and capture the output
            output = self.run_spider(spider_name, game_name)
            return JsonResponse(output, safe=False)
        except Exception as e:
            logging.error("An error occurred while running the spider: %s", str(e))
            return JsonResponse({'error': str(e)}, status=500)

    def run_spider(self, spider_name, game_name):
        settings = get_project_settings()
        if ScrapeGameView.process is None:
            ScrapeGameView.process = CrawlerProcess(settings)

        if spider_name == 'playstation_spider':
            spider_class = playstation_spider.PlaystationSpider
        elif spider_name == 'xbox_spider':
            spider_class = xbox_spider.XboxSpider
        else:
            raise Exception(f"Spider '{spider_name}' not found.")

        output_file = tempfile.mktemp()

        done_event = threading.Event()

        def run_crawler():
            deferred = ScrapeGameView.process.crawl(spider_class, search_query=game_name, output_file=output_file)
            deferred.addBoth(self.spider_closing, done_event)
            ScrapeGameView.process.start(stop_after_crawl=False)

        thread = threading.Thread(target=run_crawler)
        thread.start()

        # Wait until the spider is done
        done_event.wait()

        with open(output_file, 'r') as f:
            results = json.load(f)

        os.remove(output_file)
        return results

    def spider_closing(self, result, done_event):
        # Signal that the spider has finished
        done_event.set()
        return result

    def spider_error(self, failure):
        logging.error(failure)
        raise Exception(f"Spider error: {failure}")

# Initialize the reactor once if it's not already running
if not reactor.running:
    threading.Thread(target=reactor.run, kwargs={'installSignalHandlers': 0}).start()

# ----------------------------------------------------------------------------
# import warnings
# warnings.filterwarnings('ignore')
# from django.http import JsonResponse
# from django.views import View
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from scrapy import signals
# import tempfile
# import json
# import os
# import threading
# import logging
# from games_scraper.games_scraper.spiders import playstation_spider, xbox_spider
# from twisted.internet import reactor

#                                              WORKING
# import warnings
# warnings.filterwarnings('ignore')
# from django.http import JsonResponse
# from django.views import View
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from scrapy import signals
# import tempfile
# import json
# import os
# import logging
# from games_scraper.games_scraper.spiders import playstation_spider, xbox_spider
# from twisted.internet import reactor


# class ScrapeGameView(View):
#     def __init__(self):
#         # Initialize the reactor once in the constructor (assuming single-threaded approach)
#         if not reactor.running:
#             reactor.run(installSignalHandlers=0)

#     def get(self, request, *args, **kwargs):
#         game_name = request.GET.get('game_name')
#         platform = request.GET.get('platform')

#         if not game_name or not platform:
#             return JsonResponse({'error': 'game_name and platform are required parameters.'}, status=400)

#         spider_name = f"{platform.lower()}_spider"
#         try:
#             # Run the spider and capture the output
#             output = self.run_spider(spider_name, game_name)
#             return JsonResponse(output, safe=False)
#         except Exception as e:
#             logging.error("An error occurred while running the spider: %s", str(e))
#             return JsonResponse({'error': str(e)}, status=500)

#     def run_spider(self, spider_name, game_name):
#         settings = get_project_settings()
#         process = CrawlerProcess(settings)  # Create a new process for each request

#         if spider_name == 'playstation_spider':
#             spider_class = playstation_spider.PlaystationSpider
#         elif spider_name == 'xbox_spider':
#             spider_class = xbox_spider.XboxSpider
#         else:
#             raise Exception(f"Spider '{spider_name}' not found.")

#         with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
#             output_file = temp_file.name
#             logging.info(f"Temporary file created: {output_file}")

#             deferred = process.crawl(spider_class, search_query=game_name, output_file=output_file)
#             deferred.addBoth(self.handle_result, output_file)  # Handle both success and error
#             process.start(stop_after_crawl=False)  # Start the process

#         # Wait for results using deferred
#         results = deferred.result()
#         return results

#     def handle_result(self, results, output_file):
#         if isinstance(results, Exception):
#             # Handle spider errors
#             logging.error(f"Error running spider: {results}")
#             raise results
#         else:
#             try:
#                 with open(output_file, 'r') as f:
#                     return json.load(f)
#             except json.JSONDecodeError as e:
#                 logging.error(f"Error decoding JSON from file: {e}")
#                 raise Exception(f"Error decoding JSON from file: {e}")
#             finally:
#                 os.remove(output_file)
#                 logging.info(f"Temporary file deleted: {output_file}")


# -----------------------------------------------
# from django.http import JsonResponse
# from django.views import View
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from scrapy import signals
# from twisted.internet import reactor, defer
# import tempfile
# import json
# import os

# from games_scraper.games_scraper.spiders import playstation_spider
# from games_scraper.games_scraper.spiders import xbox_spider

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
#             return JsonResponse({'error': str(e)}, status=500)

#     def run_spider(self, spider_name, game_name):
#         settings = get_project_settings()
#         process = CrawlerProcess(settings)

#         if spider_name == 'playstation_spider':
#             spider_class = playstation_spider.PlaystationSpider
#         elif spider_name == 'xbox_spider':
#             spider_class = xbox_spider.XboxSpider
#         elif spider_name == 'pc_spider':
#             spider_class = pc_spider.PCSpider
#         else:
#             raise Exception(f"Spider '{spider_name}' not found.")

#         output_file = tempfile.mktemp()

#         @defer.inlineCallbacks
#         def crawl():
#             crawler = process.create_crawler(spider_class)
#             crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
#             yield process.crawl(crawler, search_query=game_name, output_file=output_file)
#             reactor.stop()

#         crawl()
        
#         if not reactor.running:
#             reactor.run(installSignalHandlers=0)

#         with open(output_file, 'r') as f:
#             results = json.load(f)
#         os.remove(output_file)

#         return results

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
