# Generated by Django 3.0.3 on 2020-09-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='productimage',
            field=models.ImageField(blank=True, default='images/product.jpg', null=True, upload_to='images/'),
        ),
    ]
