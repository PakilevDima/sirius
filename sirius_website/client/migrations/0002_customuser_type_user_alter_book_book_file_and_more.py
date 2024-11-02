# Generated by Django 5.1.1 on 2024-10-05 02:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='type_user',
            field=models.CharField(choices=[('читатель', 'ЧИТАТЕЛЬ'), ('автор', 'АВТОР')], default='читатель', max_length=10, verbose_name='Тип пользователя'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_file',
            field=models.FileField(upload_to='book/files/2468071003536', validators=[django.core.validators.FileExtensionValidator(['txt', 'docx'])], verbose_name='Файл книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image_book',
            field=models.ImageField(blank=True, upload_to='book/files/2468071003536', verbose_name='Обложка'),
        ),
    ]
