from django.shortcuts import render, redirect
from .models import PlatModel
from .form import PlatForm

# Create your views here.


def add_plat(request):
    if request.method == "POST":
        form_plat = PlatForm(request.POST)

        if  form_plat.is_valid():
             form_plat.save()
             return redirect('plats:listplat')
        
    else:
       form_plat = PlatForm()
    
    return render(request, 'add_menu.html', {'form_plat': form_plat})


def edit_plat(request, id):
    plat = PlatModel.objects.get(id = id)
    form_plat = PlatForm(request.POST, instance=plat)
    if form_plat.is_valid():
       form_plat.save()
       return redirect('plats:listplat')
    
    form_plat = PlatForm(instance= plat )
    return render(request, 'edit_menu.html', {'form_plat': form_plat} )

  
def list_plat(request):
    plat = PlatModel.objects.all()
    return render(request, 'plats.html', {'plat': plat})


def delete_plat(request, id):
    plat = PlatModel.objects.get(id = id)
    plat.delete()
    return redirect('plats:listplat')
