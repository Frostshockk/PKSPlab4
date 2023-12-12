from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('article/<int:article_id>', views.get_article, name = 'get_article'),
    path('', views.archive)
    
]