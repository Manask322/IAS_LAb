from django.urls import path

from . import views

urlpatterns = [
    path('cyclic_attack/', views.cyclic_attack, name='cyclic'),
    path('home', views.home, name='home'),
    # path('', views.home, name='home'),
    path('des/',views.ECB,name='des'),
    path('blind/',views.blind,name="blind"),
    path('cipher/',views.chosen_cipher,name="cipher"),
]