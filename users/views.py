from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserForm
from .models import User
from django.views.generic import DetailView

def login_view(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['pas']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # Переадресация на главную страницу или другую страницу после входа
            else:
                error = 'Неверный логин или пароль!'
    else:
        form = UserForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'users/vhod.html', context)

def login(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            error = 'Форма сохранена'
            return redirect('vhod', error) #переадрессация на другую страницу
        else:
            error = 'Форма введена неверно!'

    form = UserForm()
    date = {
        'form': form,
        'error': error
    }
    return render(request, 'users/login.html', {'date': date})

def user_home(request):
    user = User.objects.order_by('surname') #сортировка по фамилии
    return render(request, 'users/user_home.html', {'user': user})

class UserDetailView(DetailView):
    model = User
    template_name = 'users/details_view.html'
    context_object_name = 'user'



# Create your views here.
