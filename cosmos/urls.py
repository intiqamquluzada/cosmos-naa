from django.urls import path
from cosmos.views import *


urlpatterns = [
    path('', index_view, name='index'),
    path('detail/<int:id>/', detail_view, name='detail'),
]