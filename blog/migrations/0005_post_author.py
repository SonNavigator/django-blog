# Generated by Django 3.2.6 on 2021-08-21 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.author'),
        ),
    ]
