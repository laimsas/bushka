from django.shortcuts import render
import pandas as pd
import matplotlib as plt
import seaborn as sns
import openpyxl
from io import BytesIO
import base64
from django.conf import settings

# Create your views here.




def show_recoil():
    df = pd.read_excel(settings.BASE_DIR.joinpath('bushka_site/static/bushka_site/recoil_multi.xlsx'), index_col=0)    recoil = sns.scatterplot(data = df, x = 'groza_X', y = 'groza_Y')
    fig = recoil.figure
    recoil_file = BytesIO() 
    fig.savefig(recoil_file, format='png')
    encoded_file = base64.b64encode(recoil_file.getvalue())
    return encoded_file

def index(request):
    return render(request, 'bushka_site/show_recoil.html',{'show_recoil':show_recoil().decode('utf-8')})