# Generated by Django 5.1.5 on 2025-02-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protfolio', '0005_alter_project_client_alter_project_project_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='procent',
            field=models.CharField(default=2, help_text='write % of skill', max_length=4),
            preserve_default=False,
        ),
    ]
