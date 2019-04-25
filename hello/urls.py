from django.urls import path
from hello import views

urlpatterns = [        
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("hello/about/", views.about, name="about"),
    path("hello/contact/", views.contact, name="contact"),
    path("hello/home/", views.home, name="home"),
]