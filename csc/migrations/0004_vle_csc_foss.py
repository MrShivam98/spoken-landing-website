# Generated by Django 3.0.3 on 2022-07-07 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spokenlogin', '0002_spfosssupercategory_spokenfoss'),
        ('csc', '0003_auto_20220601_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vle_csc_foss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programme_type', models.CharField(choices=[('dca', 'DCA Programme'), ('individual', 'Individual Course')], default='dca', max_length=100)),
                ('created', models.DateField(blank=True, null=True)),
                ('updated', models.DateField(auto_now=True, null=True)),
                ('spoken_foss', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='spokenlogin.SpokenFoss')),
            ],
        ),
    ]
