# Generated by Django 3.0.3 on 2020-09-02 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_extrainfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrainfo',
            name='Nationality',
            field=models.IntegerField(choices=[(1, 'Afghanistan'), (2, 'Albania')], default=1),
        ),
    ]
