# Generated by Django 4.1.2 on 2022-10-28 12:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Makalaye Foroğraf Ekleyin'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
