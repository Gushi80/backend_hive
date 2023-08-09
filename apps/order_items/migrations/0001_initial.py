# Generated by Django 4.2.1 on 2023-08-09 14:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(verbose_name='Quantity')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Creation Date')),
            ],
            options={
                'db_table': 'order_item',
            },
        ),
    ]