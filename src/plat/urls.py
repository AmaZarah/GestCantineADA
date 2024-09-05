from django.urls import path
from .views import add_plat, edit_plat, list_plat, delete_plat





app_name = "plats"

urlpatterns =[
    path('',add_plat, name='adplat'),
    path('listplat',list_plat, name='listplat' ),
    path('editsplat/<int:id>/',edit_plat, name='editplat'),
    path('delplat/<int:id>/', delete_plat, name='delplat')
   
]