from django.urls import path 
from . import views

app_name= 'close'

urlpatterns = [
    path('home/', views.test_home , name='home' ),

]
