from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

def redirect_signin(request):
    response = redirect('signin/')
    return response

def signin(request):
    template = loader.get_template('zomato/login.html')
    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template('zomato/signup.html')
    return HttpResponse(template.render())
# Create your views here.

