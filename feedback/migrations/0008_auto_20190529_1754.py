# Generated by Django 2.0.4 on 2019-05-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0007_feedback_is_urgent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='status',
            field=models.CharField(choices=[('already_exists', 'Issue Already Exists'), ('considering_ntf', 'Considering No Time Frame'), ('considering_tf', 'Considering With Time Frame'), ('working', 'Working'), ('complete', 'Complete'), ('not_valid', 'Not a Valid Issue'), ('submitted', 'Submitted')], default='submitted', max_length=60),
        ),
    ]