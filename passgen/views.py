from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random


# Create your views here.
def home(request):
    return render(request, 'home.html')

def passgen(request):
    char = list('abcdefghijklmnopqrstuvwyz!@#$%^&*()+')
    nums = list('123456789')
    password = ""
    for x in range(15):
        password += random.choice(char)
        password += random.choice(nums)
    return render(request, 'password.html', {'password': password})