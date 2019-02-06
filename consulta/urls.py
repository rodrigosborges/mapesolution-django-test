from django.urls import path
from .views import home, lists

urlpatterns = [
    path('', home, name="home"),
    path('list/', lists, name="lists"),
]
