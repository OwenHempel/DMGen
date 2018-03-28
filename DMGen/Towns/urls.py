from django.urls import path

from . import views

app_name = 'Towns'
urlpatterns = [
    path('', views.TownList, name='index'),
    path('<int:town_id>/', views.Towndetail, name='Towndetail'),
    path('Generate/', views.Generate, name='Generate'),
    path('Modify/', views.modify, name = 'Modify')
]