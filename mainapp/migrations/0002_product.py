# Generated by Django 3.1.3 on 2020-11-27 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='products_images', verbose_name='Изображение')),
                ('short_desc', models.CharField(max_length=120, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество на складе')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productcategory', verbose_name='Категория')),
            ],
        ),
    ]
