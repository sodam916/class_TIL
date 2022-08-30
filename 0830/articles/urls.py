
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name= 'dinner'),
    path('base/', views.base, name= 'base'),
    path('throw/', views.throw, name= 'throw'),
    path('catch/', views.catch, name= 'catch'),
    path('hello/<str:name>/<int:age>/', views.hello, name= 'hello'),
]