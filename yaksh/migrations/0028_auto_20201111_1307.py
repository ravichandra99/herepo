# Generated by Django 3.0.7 on 2020-11-11 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0027_release_0_28_0'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessonfile',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='learningunit',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='tableofcontents',
            name='lesson',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
        migrations.DeleteModel(
            name='LessonFile',
        ),
    ]