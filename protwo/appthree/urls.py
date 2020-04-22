from django.urls import path
from appthree import views

urlpatterns = [path('',views.signup, name = 'formmodel'),]
