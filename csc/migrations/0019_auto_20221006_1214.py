# Generated by Django 3.0.3 on 2022-10-06 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csc', '0018_test_invigilator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='participant_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
