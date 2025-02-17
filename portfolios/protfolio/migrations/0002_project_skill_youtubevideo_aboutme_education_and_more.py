# Generated by Django 5.1.5 on 2025-01-28 08:26

import django.db.models.deletion
import tinymce.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter your project title', max_length=100)),
                ('year', models.CharField(help_text='Year, e.g. , 2018', max_length=4)),
                ('client', models.CharField(help_text='Client e.g. , Monday Labs', max_length=100)),
                ('service', models.CharField(help_text='Service, e.g. , Web Development', max_length=100)),
                ('project_type', models.CharField(help_text='Project type  e.g. , Back end ', max_length=100)),
                ('description', tinymce.models.HTMLField(blank=True, help_text='Details about the project', null=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your skill name', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter your video title', max_length=100)),
                ('link', models.URLField(help_text='Enter your video link')),
                ('thumnail', models.ImageField(help_text='Youtube video thumbnail', upload_to='image/youtube_thumbnail')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', tinymce.models.HTMLField(help_text='Write someting about yourself', null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='about_me/image')),
                ('my_name', models.CharField(help_text='Enter your name', max_length=100)),
                ('social_media', models.JSONField(blank=True, help_text='Add your social media links', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(blank=True, help_text='Add your skills', to='protfolio.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.CharField(help_text='Start year, e.g, 2022', max_length=4)),
                ('end_year', models.CharField(help_text='End year, e.g, 2024', max_length=4)),
                ('degree', models.CharField(help_text='Degree, e.g. , Bachelor of Science ', max_length=100)),
                ('university', models.CharField(help_text='University, e.g. , University of Bukhara', max_length=100)),
                ('description', tinymce.models.HTMLField(help_text='Description, e.g, Bachelor of Science in Computer Science')),
                ('about_me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protfolio.aboutme')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.CharField(help_text='Start year, e.g, 2022', max_length=4)),
                ('end_year', models.CharField(help_text='End year, e.g, 2024', max_length=4)),
                ('position', models.CharField(help_text='Postionion, e.g. , Software engineer', max_length=100)),
                ('company', models.CharField(help_text='Company, e.g. , Monday labs', max_length=100)),
                ('description', tinymce.models.HTMLField(help_text='Description, e.g, Software Engineer at Monday labs')),
                ('about_me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protfolio.aboutme')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Upload your project image', upload_to='project/image')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protfolio.project')),
            ],
        ),
    ]
