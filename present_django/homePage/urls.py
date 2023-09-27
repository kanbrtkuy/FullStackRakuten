# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('rakuten-api/', views.rakuten_api, name='rakuten_api'),
]