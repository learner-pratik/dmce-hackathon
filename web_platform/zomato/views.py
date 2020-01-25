from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import requests

def redirect_signin(request):
    response = redirect('signin/')
    return response

def signin(request):
    template = loader.get_template('zomato/login.html')
    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template('zomato/signup.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('zomato/home.html')
    return HttpResponse(template.render())

def profile(request):
    template = loader.get_template('zomato/profile.html')
    return HttpResponse(template.render())

def restaurant(request):
    template = loader.get_template('zomato/restaurant.html')
    return HttpResponse(template.render())

def order(request):
    template = loader.get_template('zomato/order.html')
    return HttpResponse(template.render())

def posts(request):
    template = loader.get_template('zomato/posts.html')
    return HttpResponse(template.render())

def feeds(request):
    template = loader.get_template('zomato/feeds.html')
    return HttpResponse(template.render())

# Create your views here.

