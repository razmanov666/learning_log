from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Регистрирует нового пользователя."""
    # print('\nls\n')
    print('\n'+str(request.method))
    print(str(request.method) != "POST")
    print('\n')
    if str(request.method) != "POST":
        # Display blank registration form.
        form = UserCreationForm()
        print('\n'+str(form.is_valid())+'\n')
    else:
        # Обработка заполненной формы.
        print('\nelse\n')
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страничку.
            authenticated_user = authenticate(username=new_user.username, 
                                              password=request.POST['password1'],
                                              confirm_password=request.POST['password2'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
            context = {'form': form}
            return render(request, 'users/register.html', context)
        else:
            pass 
