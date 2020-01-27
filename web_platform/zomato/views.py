from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .forms import loginform,orderform
from .models import User,Restaurants,Posts,Orders
from django.core.mail import send_mail

def redirect_signin(request):
    response = redirect('signin/')
    return response

def signin(request):
    if request.method == 'POST':
        id=request.POST.get('geoc3')
        # id = request.POST.get('od')
        print(id)
        if id !=None:
            request.session['res_id']=id
            r_info=Restaurants.objects.get(res_id=id)
            print(r_info)
            return render(request, "zomato/restaurant.html", {'r_info':r_info})
            # url = reverse('restaurant',kwargs={})
            # return HttpResponseRedirect(url)
        form = loginform(request.POST or None)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            password = form.cleaned_data['password']
            request.session['username'] = user
            request.session['password'] = password
            r=Restaurants.objects.filter(res_id=102)
            print('hello inside')
            print(r)
            return render(request, "zomato/home.html", {'res_info':r})
    # template = loader.get_template('zomato/login.html')
    # return HttpResponse(template.render())
    return render(request, "zomato/login.html", {})

def signup(request):
    # template = loader.get_template('zomato/signup.html')
    # return HttpResponse(template.render())
    return render(request, "zomato/signup.html", {})

def home(request):
    # if request.method == 'POST':
    #     form = loginform(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #         user = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         request.session['username'] = user
    #         request.session['password'] = password
    #         up=User.objects.get(user_name=user)
    #         print(up)
    #         return render(request, "zomato/home.html", {'user_info':up})
    return render(request, "zomato/home.html", {})

def restaurant(request):
    # print(request.session['res_id'])
    # r_id= request.session['res_id']
    # print(r_id)
    # r_info=Restaurants.objects.get(res_id=r_id)
    # print(r_info)
    return render(request, "zomato/restaurant.html", {})

def dashboard(request):
    r=Restaurants.objects.all()
    return render(request, "zomato/dashboard.html", {'restaurants':r})

def feed(request):
    u_id=request.session['username']
    print(u_id)
    posts=Posts.objects.filter(user_id=u_id)
    return render(request, "zomato/feeds.html", {'posts':posts})

def order(request):
    # u_id=request.session['username']
    # r_id=request.session['res_id']
    # if request.method == 'POST':
    #     # form = orderform(request.POST or None)
    #     #print(orderform.food_item)
    #     # if form.is_valid():
    #     ord=Orders()
    #     ord.food_item= request.POST.get('food_item')
    #     ord.price= request.POST.get('price')
    #     ord.user_id= u_id
    #     ord.res_id=r_id
    #     ord.order_id=10
    #     ord.save()
    #     return render(request, "zomato/orderplaced.html", {})
    if request.method == 'POST':
        return render(request, "zomato/order_place.html", {})
    return render(request, "zomato/order.html", {})

def orderplaced(request):
    if request.method == 'POST':
        form = orderform(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request, "zomato/orderplaced.html", {})

def c_post(request):
    if request.method == 'POST':
        return render(request, "zomato/post_create.html", {})
    return render(request, "zomato/posts.html", {})

def c_posted(request):
    if request.method == 'POST':
        form = loginform(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request, "c_posted.html", {})

def userprofile(request):
    # u_id=request.session['username']
    # up=User.objects.get(user_name=u_id)
    # print(up)
    return render(request, "zomato/profile.html", {})

def review(request):
    if request.method == 'POST':
        return render(request, "zomato/review_add.html", {})
    return render(request, "zomato/order.html", {})

def mail(request):
    send_mail('Django mail', 'Referal Link', 'siddesh.pn23@gmail.com', ['omkardhawal21@gmail.com'], fail_silently=False)
    return render(request, 'zomato/mail.html')
