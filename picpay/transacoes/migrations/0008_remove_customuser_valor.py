# Generated by Django 3.2.19 on 2024-05-20 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transacoes', '0007_auto_20240520_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='valor',
        ),
    ]
