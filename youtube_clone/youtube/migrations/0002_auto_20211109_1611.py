# Generated by Django 3.2.9 on 2021-11-09 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='dislikes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='comments',
            name='likes',
            field=models.IntegerField(),
        ),
    ]