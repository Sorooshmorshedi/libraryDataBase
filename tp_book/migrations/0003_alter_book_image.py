# Generated by Django 3.2.9 on 2021-11-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp_book', '0002_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='store_image/'),
        ),
    ]