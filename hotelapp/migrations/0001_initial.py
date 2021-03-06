# Generated by Django 3.2.7 on 2021-12-10 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addHotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelimage', models.ImageField(upload_to='')),
                ('hotelname', models.CharField(max_length=50)),
                ('hoteldescription', models.CharField(max_length=100)),
                ('hotellocation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='bookRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=40)),
                ('Mobile', models.CharField(max_length=12)),
                ('Address', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=30)),
                ('State', models.CharField(max_length=30)),
                ('CheckInDate', models.DateField()),
                ('CheckInTime', models.TimeField()),
                ('CheckOutDate', models.DateField()),
                ('CheckOutTime', models.TimeField()),
                ('RoomType', models.CharField(max_length=50)),
                ('Adults', models.IntegerField()),
                ('Childrens', models.IntegerField()),
                ('IdType', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='hotelappAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('address', models.CharField(max_length=50)),
                ('profile', models.ImageField(upload_to='')),
                ('dob', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='hoteldetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelimage', models.ImageField(upload_to='')),
                ('hotelname', models.CharField(max_length=200)),
                ('hoteldescription', models.CharField(max_length=300)),
                ('hotellocation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='roomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomType', models.CharField(max_length=150)),
                ('roomPrice', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('hotelId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.addhotels')),
            ],
        ),
    ]
