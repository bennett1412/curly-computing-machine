from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import ProfileCreationForm, STGUserRegister
def signup(request):
    if request.method == 'POST':
        u_form = STGUserRegister(request.POST)
        p_form = ProfileCreationForm(request.POST)
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            username = u_form.cleaned_data.get('username')
            raw_password = u_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            p_form.user = user
            #Profile.objects.create(user=instance)
            p_form.save()
            login(request, user)
            return redirect('donations/')
    else:
        u_form = STGUserRegister()
        p_form = ProfileCreationForm()
    return render(request, 'useraccounts/signup.html', {'u_form': u_form,'p_form':p_form})
