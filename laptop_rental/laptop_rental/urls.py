from django.contrib import admin
from django.urls import path, include
from rental.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', include('rental.urls')),
]
