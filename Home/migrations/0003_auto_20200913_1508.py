# Generated by Django 3.0.3 on 2020-09-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20200913_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='productimage',
            field=models.ImageField(blank=True, default='media/images/product.jpg', null=True, upload_to='media/images/'),
        ),
    ]