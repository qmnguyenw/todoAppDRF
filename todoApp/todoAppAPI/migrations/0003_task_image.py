# Generated by Django 3.0.2 on 2020-01-15 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoAppAPI', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='Images/None/No0img.jpg', upload_to='Images/'),
        ),
    ]
