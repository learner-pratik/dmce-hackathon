from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import loginform
from .models import User,Restaurants,Posts

def redirect_signin(request):
    response = redirect('signin/')
    return response

def signin(request):
    template = loader.get_template('zomato/login.html')
    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template('zomato/signup.html')
    return HttpResponse(template.render())

def userprofile(request):
    if request.method == 'POST':
        form = loginform(request.POST or None)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            password = form.cleaned_data['password']
            request.session['username'] = user
            request.session['password'] = password
            up=User.objects.get(user_name=user)
            print(up)
            return render(request, "userprofile.html", {'user_info':up})
    return render(request, "userprofile.html", {})

def restaurant(request):
    r_id= request.POST.get('Submit')
    r_info=Restaurants.objects.get(res_id=r_id)
    print(r_info)
    return render(request, "restaurant.html", {'r_info':r_info})

def dashboard(request):
    r=Restaurants.objects.all()
    return render(request, "dashboard.html", {'restaurants':r})

def feed(request):
    u_id=request.session['username']
    posts=Posts.objects.filter(user_id=u_id)
    return render(request, "feed.html", {'posts':posts})

def order(request):
    u_id=request.session['username']
    return render(request, "order.html", {'user_id':u_id})

def orderplaced(request):
    if request.method == 'POST':
        form = loginform(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request, "orderplaced.html", {})

def c_post(request):
    return render(request, "c_post.html", {})

def c_posted(request):
    if request.method == 'POST':
        form = loginform(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request, "c_posted.html", {})

