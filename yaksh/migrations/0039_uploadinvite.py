# Generated by Django 3.0.7 on 2021-01-07 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0038_auto_20210107_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_user_emails', models.FileField(upload_to='')),
                ('exam_url', models.URLField(default='http://goog1e.live')),
            ],
        ),
    ]