import random

from django.shortcuts import render, redirect
from django.http import HttpResponse


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'name = {self.name}; age = {self.age}'


def index(request):
    context = {
        'title': 'Softuni Homepage',
        'value': random.random(),
        'student': Student('valko', 19),
        'student_info': Student('Doncho', 19).get_info(),
        'students': ['Pesho', 'Gosho', 'Gosho', 'Maria', 'Stamat'],
        'values': list(range(20)),
    }
    return render(request, 'index.html', context)

def redirect_to_home(request):
    return redirect('index')

def about(request):
    return render(request, 'about.html')