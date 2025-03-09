
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/', include('AdminPanel.urls')),
    path('users/', include('UserInterface.urls')),
    path('', lambda request: redirect('users/')),
    path('spiriter/', include('Spiriter.urls')),
]
