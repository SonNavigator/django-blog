# Generated by Django 3.2.6 on 2021-08-21 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_author_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('sender', models.CharField(max_length=80)),
                ('detail', models.TextField()),
            ],
        ),
    ]
