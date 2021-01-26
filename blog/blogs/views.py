from django.shortcuts import render

from .models import BlogPost

def blogposts(request):
    """Возвращает пост из блога."""
    blogposts = BlogPost.objects.order_by("date_added")
    context = {'blogposts': blogposts}
    return render(request, 'blogs/blogposts.html', context)