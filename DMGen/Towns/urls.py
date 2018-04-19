from django.urls import path

from . import views

app_name = 'Towns'
urlpatterns = [
    path('', views.TownList, name='index'),
    path('<int:town_id>/', views.Towndetail, name='Towndetail'),
    path('Generate/', views.Generate, name='Generate'),
    path('Modify/NPC/<int:npcid>', views.modifyNPC, name = 'ModifyNPC'),
    path('Modify/Shop/<int:sid>', views.modifyShop, name = 'ModifyShop'),
    path('Randomize/', views.randomizeTown, name = 'Randomize')
]