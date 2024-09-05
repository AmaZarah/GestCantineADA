from django.urls import path
from .views import add_menu, edit_menu, list_menu, delete_menu





app_name = "menus"

urlpatterns =[
    path('',add_menu, name='admenu'),
    path('listmenu',list_menu, name='listmenu' ),
    path('editmenu/<int:id>/',edit_menu, name='edimenu'),
    path('delmenu/<int:id>/', delete_menu, name='delmenu')
   
]