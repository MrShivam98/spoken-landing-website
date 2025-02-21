# Generated by Django 3.0.3 on 2022-11-03 04:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('csc', '0020_auto_20221006_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='invigilator',
            name='password_mail_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='mdl_mail_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='invigilator',
            name='phone',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='invigilator',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invi', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invigilator',
            name='vle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='invig', to='csc.VLE'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_registration',
            field=models.DateField(default=datetime.date(2022, 11, 3)),
        ),
        migrations.AlterField(
            model_name='test',
            name='status',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='invigilator',
            unique_together={('user', 'vle')},
        ),
        migrations.CreateModel(
            name='CSCFossMdlCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mdlcourse_id', models.PositiveIntegerField()),
                ('mdlquiz_id', models.PositiveIntegerField()),
                ('foss', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cscfoss', to='csc.FossCategory')),
                ('testfoss', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='testfoss', to='csc.FossCategory')),
            ],
        ),
        migrations.RemoveField(
            model_name='invigilator',
            name='added_by',
        ),
        migrations.RemoveField(
            model_name='invigilator',
            name='vle',
        ),
        migrations.CreateModel(
            name='CSCTestAtttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mdluser_id', models.PositiveIntegerField()),
                ('mdlcourse_id', models.PositiveIntegerField(default=0)),
                ('mdlquiz_id', models.PositiveIntegerField(default=0)),
                ('mdlattempt_id', models.PositiveIntegerField(default=0)),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('mdlgrade', models.DecimalField(decimal_places=5, default=0.0, max_digits=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='csc.Student')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='csc.Test')),
            ],
            options={
                'verbose_name': 'Test Attendance',
                'unique_together': {('test', 'mdluser_id')},
            },
        ),
    ]
