# Generated by Django 3.0.7 on 2021-01-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0036_auto_20210104_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='exam_url',
            field=models.URLField(default='http://goog1e.live'),
        ),
    ]
