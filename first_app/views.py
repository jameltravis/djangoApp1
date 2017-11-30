from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(requests):
    """Returns hello world""" 
    return HttpResponse("Hello World...again")

