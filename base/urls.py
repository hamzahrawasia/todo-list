from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('list/<str:id>/', views.list, name="list"),
    path('create-list/', views.createList, name="create-list"),
    path('update-list/<str:id>/', views.updateList, name="update-list"),
    path('delete-list/<str:id>/', views.deleteList, name="delete-list"),
    path('delete-task/<str:id>/', views.deleteTask, name="delete-task"),
#     path('update-task/<str:id>/', views.updateTask, name="update-task"),
 ]