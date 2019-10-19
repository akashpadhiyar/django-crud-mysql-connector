
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    
    path('category/', views.categorylisting, name="categorylisting"),
    path('category/create/', views.categorycreate, name="categorycreate"),
    path('category/inserted/', views.categoryaddprocess, name="categoryaddprocess"),
    path('category/delete/<int:id>', views.categorydelete, name="categorydelete"),
    path('category/edit/<int:id>', views.categoryedit, name="categoryedit"),
    path('category/update/', views.categoryupdate, name="categoryupdate"),
]