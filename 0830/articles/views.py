from multiprocessing import context
import random
from django.shortcuts import render

# Create your views here.
def index(request):
    nums = [1, 2, 3]
    context = {
        'name': 'lee sumin',
        'nums': nums,
    }
    return render(request, 'index.html', context)

def greeting(request):
    foods = ['apple', 'banana', 'coconut']
    info = {
        'name': 'Alice'
    }
    context = {
        'foods': foods,
        'info': info,
    }
    return render(request, 'greeting.html', context)

def dinner(request):
    foods = ['족발', '햄버거', '치킨', '초밥',]
    pick = random.choice(foods)
    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'dinner.html', context)

def base(request):
    return render(request, 'base.html')
    pass

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message
    }
    return render(request, 'catch.html', context)

def hello(request, name, age):
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'hello.html', context)
    