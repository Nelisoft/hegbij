from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('services/', views.Service, name='services'),
    path('contact/', views.Contact, name='contact'),
    path('cases/', views.Case_study, name='cases'),
    path('blog/', views.Blog, name='blog'),
]
