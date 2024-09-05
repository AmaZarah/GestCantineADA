from django.shortcuts import render, redirect
from .models import MenuMolel
from .forms import MenuForm

# Create your views here.





def add_menu(request):
    if request.method == "POST":
        form_menu = MenuForm(request.POST)

        if form_menu.is_valid():
            form_menu.save()
            return redirect('menus:liststudent')
        
    else:
      form_menu = MenuForm()
    
    return render(request, 'add_menus.html', {'form_menu': form_menu})


def edit_menu(request, id):
    menu = MenuMolel.objects.get(id = id)
    form_menu = MenuForm(request.POST, instance=menu)
    if form_menu.is_valid():
       form_menu.save()
       return redirect('menus:listmenu')
    
    form_student = MenuForm(instance= menu )
    return render(request, 'edit_menu.html', {'form_menu': form_menu} )

   
def list_menu(request):
    menu = MenuMolel.objects.all()
    return render(request, 'menus.html', {'student': menu})


def delete_menu(request, id):
    menu = MenuMolel.objects.get(id = id)
    menu.delete()
    return redirect('menus:listmenu')
