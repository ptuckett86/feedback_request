# Generated by Django 2.0.4 on 2019-06-18 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0008_auto_20190529_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='is_urgent',
            field=models.BooleanField(default=False),
        ),
    ]
