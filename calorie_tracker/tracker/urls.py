from django.contrib import admin
from django.urls import path, include
from tracker import views


urlpatterns = [
    path('', views.home, name='home'),  
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('add_food_item/', views.add_food_item, name='add_food_item'),
    path('add_food_log/', views.add_food_log, name='add_food_log'),
    path('progress_chart/', views.progress_chart, name='progress_chart'),
    
    # path('accounts/login/', views.user_login, name='default_login_redirect')
]
