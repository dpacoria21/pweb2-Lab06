# Generated by Django 4.0.5 on 2022-06-25 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_alter_destination_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
