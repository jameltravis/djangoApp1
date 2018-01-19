from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """Returns hello world"""
    my_dictionary = {"insert_me": "Hello I am from views.py"}
    return render(request, "index.html", context=my_dictionary)
