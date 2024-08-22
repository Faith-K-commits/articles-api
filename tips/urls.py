from django.urls import path
from . import views

app_name = 'tips'

urlpatterns = [
    path('api/articles/', views.articles, name="articles"),
    path('api/articles/language/<str:language>/', views.get_articles_by_language, name="get_articles_by_language"),
    path('api/articles/search/', views.search_articles, name="search_articles"),
    path('api/articles/<int:pk>/update/', views.update_article, name="update_articles"),
    path('api/articles/<int:pk>/delete/', views.delete_article, name="delete_article"),
]
