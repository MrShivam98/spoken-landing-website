# Generated by Django 3.0.3 on 2022-07-20 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csc', '0016_auto_20220720_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvigilationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('invigilator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csc.Invigilator')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csc.Test')),
            ],
        ),
    ]
