from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title') 

class PostAdmin(admin.ModelAdmin):
    list_display =(
        'pk',
        'title',
    )
class CategoryPostAdmin(admin.ModelAdmin):
    list_display =(
        'pk',
        'title',
        'category',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(CategoryPost, CategoryPostAdmin)
