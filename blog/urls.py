from django.urls import path
from . import views

urlpatterns = [
    path("", views.log_in, name="blog-log_in"),
    path('signup/', views.sign_up, name='blog-sign_up'),
    path('login/', views.log_in, name='blog-log_in'),
    path("Home/", views.Home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
]