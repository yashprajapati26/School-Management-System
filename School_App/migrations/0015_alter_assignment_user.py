# Generated by Django 4.1.5 on 2023-01-22 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('School_App', '0014_result_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_App.user'),
        ),
    ]