"""Menu views"""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Local
from nora_menu.menu.forms import MenuForm


@login_required
def admin_view(request):

    if request.method == 'POST':
        menu_form = MenuForm(request.POST)
        if menu_form.is_valid():
            print('se armo. :)')

    return render(request=request, template_name='menu/main.html')
