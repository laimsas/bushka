from django.urls import path
from . import views


app_name = 'bushka_site'
urlpatterns = [
    path('', views.index, name='index'),
    path('WeaponListView/', views.WeaponListView.as_view(), name='weapons'),
    path('<pk>/', views.WeaponDetailView.as_view()),
    path('show_recoil/', views.show_recoil, name='show_recoil'),
]
