# Generated by Django 3.2.9 on 2021-11-25 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp_book', '0004_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=150),
        ),
    ]
