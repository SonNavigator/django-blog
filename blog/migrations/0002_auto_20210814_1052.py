# Generated by Django 3.2.6 on 2021-08-14 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_updatd',
        ),
        migrations.AddField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]