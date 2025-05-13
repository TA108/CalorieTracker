from django.contrib import admin
from django.urls import path, include
from tracker import views


urlpatterns = [
    
    path('', views.home, name='home'),  
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_food_item/', views.add_food_item, name='add_food_item'),
    path('add_food_log/', views.add_food_log, name='add_food_log'),
    path('foods_logged/', views.foods_logged, name='foods_logged'),
    path('progress_chart/', views.progress_chart, name='progress_chart'),
    
]
