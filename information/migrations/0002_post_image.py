# Generated by Django 4.2.6 on 2023-11-01 14:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
