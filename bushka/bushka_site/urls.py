from django.urls import path
from . import views


app_name = 'bushka_site'
urlpatterns = [
    path('show_recoil/', views.show_recoil, name='show_recoil'),
    path('', views.WeaponListView.as_view(), name='weapons'),
]
