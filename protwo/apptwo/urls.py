from django.urls import path
from apptwo import views

urlpatterns = [path('',views.db, name = 'data'),]
