# Generated by Django 3.0.3 on 2022-09-27 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csc', '0012_auto_20220920_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='vle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_date', to='csc.VLE'),
        ),
    ]
