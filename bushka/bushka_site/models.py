from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

# Create your models here.


class Categorie(models.Model):
    categorie = models.CharField(_('categorie'), max_length=100)
    description = models.CharField(_('description'), max_length=200)


class Weapon(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.CharField(_('description'), max_length=200)
    recoil_x = models.CharField(_('recoil_x'), max_length=100)
    recoil_y = models.CharField(_('recoil_y'), max_length=100)
    image = models.ImageField(_('image'), upload_to='bushka_site/img', null=True, blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, related_name='categories', verbose_name=_('autorius'))
