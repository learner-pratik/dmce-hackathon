from django.urls import path, include
from zomato import views
from django.contrib.auth import views as auth_views

app_name = 'zomato'
urlpatterns = [
    path("", views.redirect_signin, name="signin"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('restaurant/', views.restaurant, name="restaurant"),
    path('profile/', views.profile, name="profile"),
    path('order/', views.order, name="order"),
    path('posts/', views.posts, name="posts"),
    path('feeds/', views.feeds, name="feeds"),
]