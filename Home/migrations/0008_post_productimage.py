# Generated by Django 3.0.3 on 2020-09-05 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_auto_20200903_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='productimage',
            field=models.ImageField(default='not', upload_to='post'),
        ),
    ]
