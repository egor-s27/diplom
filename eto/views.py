from django.shortcuts import render, redirect
from .models import Dvigateli
from .forms import DvigateliForm
from django.views.generic import DetailView, UpdateView, DeleteView

def eto_home(request):
    eto = Dvigateli.objects.all() #Получаем все объекты из БД
    return render(request, 'eto/eto_home.html', {'eto': eto})

class EtoDetailView(DetailView):
    model = Dvigateli
    template_name = 'eto/details_eto.html' #шаблон который будет запускаться
    context_object_name = 'eto' #ключ по которому мы передаём объект в нутрь шаблона

class EtoUpdateView(UpdateView):
    model = Dvigateli
    template_name = 'eto/add.html'

    form_class = DvigateliForm
    # fields = ['model', 'vid_eto', 'tip_1', 'tip_2', 'tip_3']

class EtoDeleteView(DeleteView):
    model = Dvigateli
    success_url = '/eto' #адрес по которому перенаправят пользователя после удаления записи
    template_name = 'eto/eto_delete.html'

def add(request):
    error = ''
    if request.method == 'POST':
        form = DvigateliForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/eto')
        else:
            error = 'Форма введена не верно'

    form = DvigateliForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'eto/add.html', data)
# Create your views here.
