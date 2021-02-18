from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/getQuery', views.getQuery, name="getQuery"),
    path('sortdata', views.sortdata, name='sortdata')
]
