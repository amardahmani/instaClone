# Generated by Django 2.2 on 2021-03-10 14:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='data_created',
        ),
        migrations.AddField(
            model_name='comments',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 14, 1, 2, 678195, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='like',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 14, 1, 2, 678697, tzinfo=utc)),
        ),
    ]