# Generated by Django 3.0.3 on 2020-09-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0020_auto_20200908_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='productimage',
            field=models.ImageField(blank=True, default='images/product.jpg', null=True, upload_to='images/'),
        ),
    ]
