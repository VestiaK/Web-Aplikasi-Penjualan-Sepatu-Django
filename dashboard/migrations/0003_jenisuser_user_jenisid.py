# Generated by Django 4.1.2 on 2024-07-18 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_barang_imagebrg'),
    ]

    operations = [
        migrations.CreateModel(
            name='JenisUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='jenisid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.jenisuser'),
        ),
    ]
