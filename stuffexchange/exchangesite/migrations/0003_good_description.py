# Generated by Django 3.2.7 on 2021-09-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangesite', '0002_alter_gallery_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='description',
            field=models.TextField(blank=True, max_length=500, verbose_name='описание товара'),
        ),
    ]
