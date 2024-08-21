from django.urls import path
from . import views

app_name = 'tips'

urlpatterns = [
    path('api/articles/', views.articles, name="articles"),
    path('api/articles/language/<str:language>/', views.get_articles_by_language, name="get_articles_by_language"),
]
