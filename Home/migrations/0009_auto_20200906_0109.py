# Generated by Django 3.0.3 on 2020-09-05 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_post_productimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='productimage',
            new_name='image',
        ),
    ]
