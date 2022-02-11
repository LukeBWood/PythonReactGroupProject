# Generated by Django 4.0.2 on 2022-02-11 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentoring', '0005_remove_relationship_mentor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.BooleanField()),
                ('active_status', models.CharField(choices=[('A', 'active'), ('I', 'inactive')], max_length=10)),
                ('advertising_for_group', models.BooleanField()),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentoring.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('attendance_status', models.CharField(choices=[('GA', 'going_ahead'), ('C', 'cancelled')], max_length=10)),
                ('title', models.CharField(max_length=20)),
                ('notes', models.TextField()),
                ('relationship', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mentoring.relationship')),
            ],
        ),
        migrations.AddField(
            model_name='meetingfeedback',
            name='meeting',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mentoring.meeting'),
        ),
        migrations.AddField(
            model_name='menteeattending',
            name='relationship',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mentoring.relationship'),
        ),
        migrations.AddField(
            model_name='planofaction',
            name='relationship',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mentoring.relationship'),
        ),
    ]
