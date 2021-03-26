from django.shortcuts import render, redirect, reverse

from .models import BlogPost
from .forms import BlogPostForm

def blogposts(request):
    """Возвращает пост из блога."""
    blogposts = BlogPost.objects.order_by("date_added")
    context = {'blogposts': blogposts}
    return render(request, 'blogs/blogposts.html', context)

def new_post(request):
    """Создает новый пост."""
    if request.method != "POST":
        # Данные не отправлялись создается пустая форма.
        form = BlogPostForm()
    else:
        # Отправленные данные POST; Обработать данные.
        form = BlogPostForm(data=request.POST)
        print(15)
        if form.is_valid():
            print(10)
            new_post = form.save(commit=False)
            new_post.save()
            return redirect(reverse("blogs:blogposts"))
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)    

def edit_post(request, blogposts_id):
    """Изменяет пост."""
    blogpost = BlogPost.objects.get(id=blogposts_id)
    if request.method != 'POST':
        form = BlogPostForm(instance=blogpost)
    else:
        # отправка данных пост.
        form = BlogPostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('blogs:blogposts'), blogposts_id=blogpost.id)
    context = {'blogpost':blogpost,'form':form}
    return render(request, 'blogs/edit_post.html', context)