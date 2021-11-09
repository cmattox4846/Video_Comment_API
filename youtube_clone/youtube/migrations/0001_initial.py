# Generated by Django 3.2.9 on 2021-11-09 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_ID', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=200)),
                ('comment_reply', models.CharField(max_length=200)),
                ('likes', models.IntegerField(max_length=10)),
                ('dislikes', models.IntegerField(max_length=10)),
            ],
        ),
    ]
