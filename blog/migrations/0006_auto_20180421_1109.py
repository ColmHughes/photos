# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-21 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_likes'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='likepost',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='likepost',
            name='author',
        ),
        migrations.RemoveField(
            model_name='likepost',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='LikePost',
        ),
    ]
