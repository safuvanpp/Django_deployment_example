from django.shortcuts import render
from django.http import HttpResponse
from apptwo.models import User

# Create your views here.

def index(request):
    my_dict = {'temp_content': "go to user/ to see the user view"}
    return render(request,'apptwo/index.html',context = my_dict)

def help(request):
    my_dict = {'help_insert': "hello help"}
    return render(request,'apptwo/help.html',context = my_dict)

def db(request):
    namelist = User.objects.order_by('Firstname')
    name_dict = {'data':namelist}
    return render(request, 'apptwo/database.html',context=name_dict)
