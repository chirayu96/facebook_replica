# Generated by Django 3.1.1 on 2020-10-30 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_app', '0007_auto_20201030_0706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='friend_post',
        ),
    ]
