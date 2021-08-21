# Generated by Django 3.2.6 on 2021-08-21 04:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default=datetime.datetime(2021, 8, 21, 4, 16, 43, 599159, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
