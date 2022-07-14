from django.shortcuts import render
from django.http import HttpResponse

# Define the home view


def home(request):
    return HttpResponse('<h1>Chat App</h1>')


def about(request):
    return HttpResponse('<h1>About the User</h1>')
