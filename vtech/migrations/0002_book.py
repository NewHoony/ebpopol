# Generated by Django 4.0 on 2023-02-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(blank=True, max_length=100, null=True)),
                ('site_url', models.TextField()),
                ('site_con', models.TextField(max_length=200)),
                ('site_cover', models.ImageField(blank=True, null=True, upload_to='vtech/bookcovers/')),
            ],
        ),
    ]