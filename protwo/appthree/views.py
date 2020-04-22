from django.shortcuts import render
from appthree.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request, 'appthree/index.html')


def signup(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)


        if form.is_valid():
            form.save(commit = True)
            return index(request)

        else:
            print('Invalid form')
    return render(request, 'appthree/users.html',{'form':form})
