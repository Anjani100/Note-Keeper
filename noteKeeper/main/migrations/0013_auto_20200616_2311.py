# Generated by Django 3.0.7 on 2020-06-16 17:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200616_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='college_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.College', verbose_name='College'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='file_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 16, 23, 11, 18, 821669), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='sub_slug',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='semester',
            name='department_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='department_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Department', verbose_name='Department'),
        ),
    ]
