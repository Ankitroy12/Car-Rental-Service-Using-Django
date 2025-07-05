from django.urls import path
from Rent import views

urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path('about',views.about),
    path('luxurious',views.luxurious),
    path('premium',views.premium),
    path('budget',views.budget),
    path('contact',views.contact,name='contact'),
    path('bike',views.bike),
]
