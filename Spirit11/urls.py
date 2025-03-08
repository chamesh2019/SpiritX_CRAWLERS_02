
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/', include('AdminPanel.urls')),
    path('users/', include('UserInterface.urls')),
]
