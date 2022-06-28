from django.shortcuts import render
import pandas as pd
import matplotlib as plt
import seaborn as sns
import openpyxl
from io import BytesIO
import base64
from django.conf import settings
from .models import Weapon, Categorie
from django.views import generic
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormMixin
from django.http import HttpResponse


class WeaponListView(generic.ListView):
    model = Weapon
    # context_object_name = 'weapon_list'
    # paginate_by = 2
    template_name = 'bushka_site/index.html'


def show_recoil(weapon):
    df = pd.read_excel(settings.BASE_DIR.joinpath('bushka_site/static/bushka_site/recoil_multi.xlsx'), index_col=0)
    recoil = sns.scatterplot(data = df, x = weapon.recoil_x, y = weapon.recoil_y, legend='full')
    fig = recoil.figure
    recoil_file = BytesIO() 
    fig.savefig(recoil_file, format='png')
    encoded_file = base64.b64encode(recoil_file.getvalue())
    print(df)
    return encoded_file


class WeaponDetailView(generic.DetailView):
    model = Weapon
    template_name = 'bushka_site/weapon_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_recoil'] = show_recoil(self.get_object()).decode('utf-8')
        return context


def weapons_compare(request):
    if request.method == 'POST':
        checked = request.POST.getlist('weapon_checkbox')
        weapons = Weapon.objects.filter(id__in = checked)        
    else:
        checked = None
        weapons = None
    return render(request, 'bushka_site/weapons_compare.html', {'weapons':weapons, 'checked' : checked})


def index(request):
    return render(request, 'bushka_site/index.html')
    