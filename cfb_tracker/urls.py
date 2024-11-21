from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/', include('players.urls')),  # Incluindo as URLs do app players
]
