# Generated by Django 4.0.5 on 2022-06-24 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]
