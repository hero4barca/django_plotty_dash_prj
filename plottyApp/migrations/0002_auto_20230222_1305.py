# Generated by Django 3.2.18 on 2023-02-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plottyApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='availability',
        ),
        migrations.AddField(
            model_name='product',
            name='stock_qty',
            field=models.IntegerField(default=1),
        ),
    ]
