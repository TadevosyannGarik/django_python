from django.shortcuts import HttpResponse
from datetime import datetime


# Create your views here.


def say_hello_views(request):

    return HttpResponse("Hello from another side. From more enter wlc ")


def info(request):

    return HttpResponse("""Welcome to my first project. So far this site is quite modest\n,
                            but still a couple of things it can, for example\n, 
                            tell you the time to wait up to a second or find the squares of numbers.
                            In order to find out the exact time, enter in the search bar "/time" \n
                            In order to see a dictionary of numbers and their squares, enter "sqrt" """)


def current_time(request):
    return HttpResponse(datetime.now())


def dict_(request):
    word = dict()
    for i in range(1, 16):
        word[i] = i ** 2
    return HttpResponse(word.items())
