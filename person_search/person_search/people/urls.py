from django.urls import path
from . import views

urlpatterns = [
    path('', views.find_person, name='find_person'),
    path('create_person/', views.create_person, name='create_person'),
]
