from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = RichTextField(null=True)

    def __str__(self):
        return self.title


class CategoryPost(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = RichTextField(null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



