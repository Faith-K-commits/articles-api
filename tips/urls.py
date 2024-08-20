from django.urls import path
from . import views

app_name = 'tips'

urlpatterns = [
    path('api/articles/', views.add_article, name="add_article"),
]
