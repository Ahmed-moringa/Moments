from django.urls import path
from . import views
from .views import (
    index,
    homepage
    )

urlpatterns=[
    path('', index, name = "index"),
    path('home/', homepage, name = 'homepage')
]