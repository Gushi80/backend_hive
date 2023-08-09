# Generated by Django 4.2.1 on 2023-08-08 02:59

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=250, null=True, verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Price')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Product image')),
                ('type', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=160, null=True, verbose_name='Type')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_category', to='categories.categories')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]