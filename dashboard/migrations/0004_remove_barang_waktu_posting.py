# Generated by Django 5.0.7 on 2024-07-18 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_jenisuser_user_jenisid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barang',
            name='waktu_posting',
        ),
    ]