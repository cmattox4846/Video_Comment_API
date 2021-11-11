# Generated by Django 3.2.9 on 2021-11-10 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0004_auto_20211109_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment_reply',
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_reply', models.CharField(max_length=200)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube.comments')),
            ],
        ),
    ]