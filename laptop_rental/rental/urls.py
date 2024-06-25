from django.urls import path
from .views import index, laptops, accessories, insurance, rental

urlpatterns = [
    path('', index, name='index'),
    path('laptops/', laptops, name='laptops'),
    path('accessories/', accessories, name='accessories'),
    path('insurance/', insurance, name='insurance'),
    path('rental/', rental, name='rental'),
]
