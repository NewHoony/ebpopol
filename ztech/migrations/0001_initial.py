# Generated by Django 4.0 on 2023-02-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(blank=True, max_length=100, null=True)),
                ('site_url', models.TextField()),
                ('site_con', models.TextField(max_length=200)),
                ('site_cover', models.ImageField(blank=True, null=True, upload_to='wtech/bookcovers/')),
            ],
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='wtech/pdfs/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='wtech/covers/')),
            ],
        ),
    ]
