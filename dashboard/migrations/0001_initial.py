# Generated by Django 5.0.7 on 2024-07-14 02:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jenis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('ket', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodebrg', models.CharField(max_length=8)),
                ('imagebrg', models.ImageField(upload_to='')),
                ('namabrg', models.CharField(max_length=50)),
                ('stokbrg', models.IntegerField()),
                ('hargabrg', models.BigIntegerField()),
                ('waktu_posting', models.DateTimeField(auto_now_add=True)),
                ('jenis_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.jenis')),
            ],
        ),
    ]