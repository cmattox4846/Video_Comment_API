# Generated by Django 3.2.9 on 2021-11-09 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_auto_20211109_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_reply',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='dislikes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]