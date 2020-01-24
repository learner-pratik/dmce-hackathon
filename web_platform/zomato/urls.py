from django.urls import path
from zomato import views

app_name = 'hello'
urlpatterns = [
    path("", views.redirect_signin, name="signin"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('userprofile/', views.userprofile, name="userprofile"),
    path('restaurant/', views.restaurant, name="restaurant"),
    path('dashboard/', views.dashboard, name="dashboard"),
]