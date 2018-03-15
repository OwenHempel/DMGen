from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:town_id>/shops/<int:shop_id>', views.shop, name='shopdetail'),
    path('<int:town_id>/NPCs/<int:NPC_id>', views.NPC, name='NPCdetail'),
    path('<int:town_id>/shops/', views.shop, name='shoplist'),
    path('<int:town_id>/NPCs/', views.NPC, name='NPClist'),
    path('', views.item, name='item'),
]