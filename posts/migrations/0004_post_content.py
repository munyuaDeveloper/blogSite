# Generated by Django 3.0.4 on 2020-03-20 04:09

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='test'),
            preserve_default=False,
        ),
    ]
