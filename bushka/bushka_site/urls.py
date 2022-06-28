from django.urls import path
from . import views


app_name = 'bushka_site'
urlpatterns = [
    path('', views.WeaponListView.as_view(), name='index'),
    path('weapon_detail/<int:pk>/', views.WeaponDetailView.as_view(), name = 'weapon_detail'),
    path('weapons_compare/', views.weapons_compare, name='weapons_compare'),
]
