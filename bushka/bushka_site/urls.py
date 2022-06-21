from django.urls import path
from . import views


app_name = 'bushka_site'
urlpatterns = [
    path('', views.index, name='index')
]
