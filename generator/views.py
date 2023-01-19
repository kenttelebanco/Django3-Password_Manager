import random
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    letters = list('abcdefghijklmnopqrstuvwyxyz')

    if request.GET.get('uppercase'):
        letters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWYXZ'))

    if request.GET.get('special'):
        letters.extend(list('!?#@$%^&*|?><"~'))

    if request.GET.get('numbers'):
        letters.extend(list('0123456789'))

    length = int(request.GET.get('length'))
    generatedpassword = ""

    for i in range(length):
        generatedpassword += random.choice(letters)

    return render(request, 'generator/password.html', {'password': generatedpassword})