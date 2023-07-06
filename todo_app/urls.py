from django.contrib import admin
from django.urls import path,include
from todo_app.views import index_view,sign_up_view,sign_in_view,sign_out_view,create_todo_view,delete_todo_view

urlpatterns = [
    path('',index_view,name='index'),
    path('sign-up/',sign_up_view,name='sign_up'),
    path('sign-in/',sign_in_view,name='sign_in'),
    path('sign-out/',sign_out_view,name='sign_out'),
    path('create-todo/',create_todo_view,name='create_todo_view'),
    path('delete-todo/',delete_todo_view,name='delete_todo_view'),

]
