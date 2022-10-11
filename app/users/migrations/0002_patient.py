# Generated by Django 4.1.1 on 2022-09-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pname', models.CharField(max_length=255)),
                ('PNational_ID', models.CharField(max_length=255, unique=True)),
                ('Mobile_Number', models.CharField(max_length=20)),
            ],
        ),
    ]
