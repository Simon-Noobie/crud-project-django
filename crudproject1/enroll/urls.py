from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('add_and_show', views.add_show, name="addNshow"),
    path('delete/<int:id>/', views.delete_data, name="deleteData"),
    path('update/<int:id>/', views.update_data, name="updateData"),
]