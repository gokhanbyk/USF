from django.shortcuts import render
from information.models import *
# Create your views here.
def index(request):

  posts = Post.objects.all()
  categories = Category.objects.all()


  return render(request, 'index.html', {
    'posts':posts,
    'categories': categories
  })

def category(request, category_slug):

  categories = Category.objects.all()

  posts = CategoryPost.objects.filter(category__slug = category_slug)
  
  return render(request, 'category.html', {
    'posts': posts,
    'categories': categories
  })

