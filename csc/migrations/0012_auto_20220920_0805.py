# Generated by Django 3.0.3 on 2022-09-20 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csc', '0011_auto_20220915_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='occupation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
