# Generated by Django 4.0.5 on 2022-06-21 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_due_date_task_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]
