# Generated by Django 4.1.6 on 2023-02-18 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_board', '0015_delete_subtask_remove_task_newcol_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='No Title', max_length=50)),
                ('status_subtask', models.BooleanField(default=False, verbose_name='Status')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanban_board.task')),
            ],
        ),
    ]
