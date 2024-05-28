from django.urls import path
from .views import ScrapeGameView

urlpatterns = [
    path('scrape-game/', ScrapeGameView.as_view(), name='scrape-game'),
]
