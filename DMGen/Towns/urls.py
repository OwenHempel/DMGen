from django.urls import path

from . import views

app_name = 'Towns'
urlpatterns = [
    path('', views.TownList, name='index'),
    path('<int:town_id>/', views.Towndetail, name='Towndetail'),
    path('Generate/', views.Generate, name='Generate'),
    #path('<int:town_id>/shops/', views.ShopList.as_view(), name='shoplist'),
    #path('<int:town_id>/NPCs/', views.NPCList.as_view(), name='NPClist'),
    #path('<int:town_id>/shops/<int:pk>', views.Shop, name='shopdetail'),
    #path('<int:town_id>/NPCs/<int:pk>', views.NPC, name='NPCdetail'),
    #path('/Item/<int:Item_id>', views.item, name='item'),
]