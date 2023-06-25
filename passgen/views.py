from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hellos there its me!!</h1> <br> <h2>Thone</h2>')

def passgen(request):
    char = list('abcdefghijklmnopqrstuvwyz')