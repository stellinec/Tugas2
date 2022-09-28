
from django.shortcuts import render
from todolist.models import Task
from todolist.forms import Form
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user)
    context = {
        
    'list_data': data_task,
    'nama' : 'Stelline Claudia',
    'id' : '2106700933',
    'user' : request.user,
    'last_login': request.COOKIES['last_login'],
}
    return render(request, "todolist.html", context)
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
def create_task(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            form2 = Task(title = title, description = description,user = request.user,date =datetime.datetime.now())
            form2.save()
            return HttpResponseRedirect(reverse("todolist:show_todolist"))

    else:
        form = Form() 

    return render(request, 'create-task.html', {'form': form})