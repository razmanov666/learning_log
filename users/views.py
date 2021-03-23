# from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm


# def register(request):
#     # import pdb; pdb.set_trace()
#     if request.method != "POST":
#         form = UserCreationForm()
#         return render(request, 'users/register.html', {'form':form})
#     else:
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             authenticated_user = authenticate(username=new_user.username, 
#                                               password=request.POST['password1'],
#                                               confirm_password=request.POST['password2'])
#             login(request, authenticated_user)
#             return redirect(reverse('index'))
#             context = {'form': form}
#             return render(request, 'users/register.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Регистрирует нового пользователя."""
    if request.method != 'POST':
        # Выводит пустую форму регистрации.
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form':form})
    else:
        # Обработка заполненной формы.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу.
            login(request, new_user)
            return redirect('learning_logs:index')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'users/register.html', context)