# Generated by Django 4.0.1 on 2022-03-07 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentoring', '0008_remove_businessareachangerequest_request_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessareachangerequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='mentoring.profile'),
        ),
    ]