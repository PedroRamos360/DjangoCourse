from django.urls import path

from .views import *

urlpatterns = [
    path('<int:id>', index, name='index'),
    path('', home, name='home'),
    path('home', home, name='home'),
    path('create', create, name='create'),
    path('view', view, name='view'),
]