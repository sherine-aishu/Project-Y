from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('offerings/', views.offerings, name='offerings'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
