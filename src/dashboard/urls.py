from django. urls import path
from .views import index


app_name = "dash"

urlpatterns =[
    path('',index, name='dash'),
   
   
]