# Generated by Django 4.0.1 on 2022-02-22 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laborganizer', '0004_remove_lab_time_lab_end_time_lab_start_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='day',
        ),
        migrations.AddField(
            model_name='lab',
            name='days',
            field=models.CharField(default='nothing', max_length=10, verbose_name='Days'),
            preserve_default=False,
        ),
    ]
