from django.urls import path
from . import views

urlpatterns =[
    path('', views.roomsView, name='rooms'),
    path('<slug:slug>/', views.roomDetailView, name='room'),
]