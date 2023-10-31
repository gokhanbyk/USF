from django.shortcuts import render
from information.models import *
# Create your views here.
def index(request):

  post = Post.objects.all()

  return render(request, 'index.html', {
    'posts':post
  })