# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('rakuten-api/', views.rakuten_api, name='rakuten_api'),
    # path('search-result/', views.searchResult.as_view(), name='search_result'),
    path('index', views.IndexView.as_view(), name='index'),
]