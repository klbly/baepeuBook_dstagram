#from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegistraterForm

# Create your views here.
#def logout(request):
#    return HttpResponse("logout view")

def register(request):
    if request.method == 'POST':
        user_form = RegistraterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else:
        user_form = RegistraterForm()
    
    return render(request, 'registration/register.html', {'form':user_form})