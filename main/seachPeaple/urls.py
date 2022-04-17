from django.urls import path 
from . import views


urlpatterns = [
    path('', views.source),
    path('next/', views.person, name = 'resoults'),
]
