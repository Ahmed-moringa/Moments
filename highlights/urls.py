from django.urls import path, re_path
from . import views
from .views import (
    index,
    search_results
    )

urlpatterns=[
    path('', index, name = "index"),
    path('search/', search_results, name = 'search'),
    re_path(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
]