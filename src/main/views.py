from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse('<h1>hello world</h1>')


def index2(response):
    return HttpResponse('<h1>hello world2</h1>')
