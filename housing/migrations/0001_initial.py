# Generated by Django 4.1.7 on 2023-03-04 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='housing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_image', models.ImageField(upload_to=None)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('rent', models.IntegerField()),
            ],
        ),
    ]
