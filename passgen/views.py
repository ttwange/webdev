from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hellos there its me!!</h1> <br> <h2>Thone</h2>')

def passgen(request):
    char = list('abcdefghijklmnopqrstuvwyz')
    password = ""
    for x in range(15):
        password += random.choice(char)
    pas = {'password':password}
    return JsonResponse(pas)