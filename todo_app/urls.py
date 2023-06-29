from django.contrib import admin
from django.urls import path,include
from todo_app.views import index_view

urlpatterns = [
    path('',index_view,name='index'),
]
