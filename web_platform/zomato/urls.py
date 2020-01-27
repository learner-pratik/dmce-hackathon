from django.urls import path
from zomato import views

app_name = 'zomato'
urlpatterns = [
    path("", views.signin, name="signin"),
    path('signin/', views.signin, name="login"),
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('userprofile/', views.userprofile, name="profile"),
    path('restaurant/', views.restaurant, name="restaurant"),
    path('feeds/', views.feed, name="feeds"),
    path('createpost/', views.c_post, name="posts"),
    path('order/', views.order, name="order"),
    path('review/', views.review, name="review"),
    path('mail/', views.mail, name="mail")
    # path('c_post/', views.c_post, name="c_post"),
]