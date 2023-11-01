from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="indexPage"),
    path('sertifika/<slug:category_slug>/', category, name='categoryPage'),
]
