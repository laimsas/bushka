from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField
import pandas as pd
import matplotlib as plt
import seaborn as sns
import openpyxl
from io import BytesIO
import base64
from django.conf import settings

# Create your models here.


class Categorie(models.Model):
    categorie = models.CharField(_('categorie'), max_length=100)
    description = models.CharField(_('description'), max_length=200)

    def __str__(self):
        return f'{str(self.categorie)} - {self.description}'

    def get_weapons(self):
        return ', '.join(Weapon.name for weapon in self.weapons.all())


class Weapon(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.CharField(_('description'), max_length=200)
    recoil_x = models.CharField(_('recoil_x'), max_length=100)
    recoil_y = models.CharField(_('recoil_y'), max_length=100)
    image = models.ImageField(_('image'), upload_to='bushka_site/img', null=True, blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, related_name='weapons', verbose_name=_('weapon'))


    def __str__(self):
        return f'{str(self.name)} - {self.description} - {self.categorie}'

    def get_seaborn(self):
        df = pd.read_excel(settings.BASE_DIR.joinpath('bushka_site/static/bushka_site/recoil_multi.xlsx'), index_col=0)
        recoil = sns.scatterplot(data = df, x = self.recoil_x, y = self.recoil_y, legend='full')
        fig = recoil.figure
        recoil_file = BytesIO() 
        fig.savefig(recoil_file, format='png')
        encoded_file = base64.b64encode(recoil_file.getvalue())
        recoil.figure.clf()
        return encoded_file.decode('utf-8')