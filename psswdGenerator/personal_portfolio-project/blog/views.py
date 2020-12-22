from django.shortcuts import render
from .models import Blogs

# Create your views here.
def all_blogs(request):
    articles = Blogs.objects.all()
    return render(request, 'blog/all_blogs.html', {'articles':articles})
