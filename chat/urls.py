from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test_room, name='test_room'),
    path('<str:room_name>/', views.room, name='room'),

]