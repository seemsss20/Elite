from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('Book/', views.Book, name="Book"),
    path('bookflight/', views.allCity, name="bookflight"),
    path('destination/', views.destination, name="destination"),
    path('FAQs/', views.FAQs, name="FAQs"),
    path('group/', views.group, name="group"),
    path('hotel/', views.hotel, name="hotel"),
    path('login/', views.login, name="login"),
    path('quick/', views.quick, name="quick"),
    path('details/<int:id>', views.details, name="details"),
    path('services/', views.services, name="services"),
    path('view/', views.view, name="view"),
    path('contact/', views.contact, name="contact"),
    path('checkout/', views.checkout, name="checkout"),

]
