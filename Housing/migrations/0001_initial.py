# Generated by Django 4.1.7 on 2023-03-18 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HousingModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
                ('Amenities', models.TextField()),
                ('Rent', models.IntegerField()),
                ('Deposit', models.IntegerField()),
                ('AccomodationType', models.TextField(choices=[('Hostel', 'Hostel'), ('PayingGuest', 'Payingguest'), ('Flat', 'Flat')])),
                ('profile', models.ImageField(upload_to='%(app_label)s_%(class)s_%(pk)s/')),
            ],
        ),
    ]