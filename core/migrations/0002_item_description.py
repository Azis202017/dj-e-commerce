# Generated by Django 3.2.8 on 2022-01-19 16:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Product Description '),
        ),
    ]
