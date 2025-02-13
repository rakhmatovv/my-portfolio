# Generated by Django 5.1.5 on 2025-02-05 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protfolio', '0004_alter_project_client_alter_project_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.CharField(help_text='Enter the client name, e.g., Google', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(help_text='Enter the project type, e.g., Mobile App', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='service',
            field=models.CharField(help_text='Enter the service type, e.g., Web Design', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='year',
            field=models.CharField(help_text='Enter the project year, e.g., 2024', max_length=4),
        ),
    ]
