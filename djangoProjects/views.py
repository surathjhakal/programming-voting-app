from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(req):
    return HttpResponse("The Server has Started")
