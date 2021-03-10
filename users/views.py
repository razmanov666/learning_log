from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def register(request):
    # import pdb; pdb.set_trace()
    if request.method != "POST":
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form':form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, 
                                              password=request.POST['password1'],
                                              confirm_password=request.POST['password2'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
            context = {'form': form}
            return render(request, 'users/register.html', context)