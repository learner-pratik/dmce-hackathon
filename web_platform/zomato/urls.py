from django.urls import path
from zomato import views

app_name = 'hello'
urlpatterns = [
    path("", views.redirect_signin, name="signin"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
]