# Generated by Django 3.0.3 on 2020-09-07 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrainfo',
            name='profilepicture',
            field=models.ImageField(blank=True, default='maleprofile.jpg', null=True, upload_to='images/'),
        ),
    ]
