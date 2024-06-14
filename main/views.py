from django.shortcuts import render, redirect
from .forms import ZnaniyaForm
from django.db.models import Avg
from .models import Znaniya

def index(request):
    return render(request, 'main/index.html')

def baza(request):
    error = ''
    sa = None
    nes_value = None
    sin_value = None
    otl_chast_value = None
    pomehi_value = None
    vid_eto_value = None
    form = ZnaniyaForm()

    if request.method == "POST":
        form = ZnaniyaForm(request.POST)
        if form.is_valid(): #Проверка на корректность введеннх данных
            form.save()
            vid_eto_value = form.cleaned_data['vid_eto']

            sa = Znaniya.objects.filter(vid_eto=vid_eto_value).aggregate(Avg('otl_koleb'))['otl_koleb__avg']
            nes_value = Znaniya.objects.filter(vid_eto=vid_eto_value).aggregate(Avg('nes'))['nes__avg']
            sin_value = Znaniya.objects.filter(vid_eto=vid_eto_value).aggregate(Avg('sin'))['sin__avg']
            otl_chast_value = Znaniya.objects.filter(vid_eto=vid_eto_value).aggregate(Avg('otl_chast'))['otl_chast__avg']
            pomehi_value = Znaniya.objects.filter(vid_eto=vid_eto_value).aggregate(Avg('pomehi'))['pomehi__avg']
        else:
            error = 'Форма введена неверно!'


    data = {
        'form': form,
        'error': error,
        'sa': sa,
        'nes_value': nes_value,
        'sin_value': sin_value,
        'otl_chast_value': otl_chast_value,
        'pomehi_value': pomehi_value,
        'vid_eto_value': vid_eto_value
    }
    return render(request, 'main/baza.html', data)
# Create your views here.

