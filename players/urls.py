from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stats/', views.stats, name='stats'),
    path('add_stat/', views.add_stat, name='add_stat'),  # Nova rota
]