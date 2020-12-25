from django.shortcuts import render, get_object_or_404
from .models import Blogs

# Create your views here.
def all_blogs(request):
    articles = Blogs.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'articles':articles})

def detail(request, blog_id):
    article = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/detail.html', {'article':article})
