# Generated by Django 2.2 on 2021-03-10 20:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210310_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 20, 55, 54, 188925, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='like',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 20, 55, 54, 188925, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]