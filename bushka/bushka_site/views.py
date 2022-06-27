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


# Create your views here.


class WeaponListView(generic.ListView):
    model = Weapon
    # context_object_name = 'weapon_list'
    # paginate_by = 2
    template_name = 'bushka_site/index.html'


class WeaponDetailView(generic.DetailView):
    model = Weapon
    template_name = 'bushka_site/weapon_detail.html'

    def show_recoil():
        df = pd.read_excel(settings.BASE_DIR.joinpath('bushka_site/static/bushka_site/recoil_multi.xlsx'), index_col=0)
        recoil = sns.scatterplot(data = df, x = 'recoil_X', y = 'recoil_Y')
        fig = recoil.figure
        recoil_file = BytesIO() 
        fig.savefig(recoil_file, format='png')
        encoded_file = base64.b64encode(recoil_file.getvalue())
        return encoded_file


class WeaponCompareView(generic.DetailView):
    model = Weapon
    template_name = 'weapon_compare'

    def get_weapons(request):
        checked = request.POST.getlist('weapon_checkbox[]')
        return render(request, 'weapon_compare.html')
    

    






def index(request):
    return render(request, 'bushka_site/index.html')