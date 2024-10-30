# Generated by Django 5.1.2 on 2024-10-28 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_project_description_project_github_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libraryframework',
            name='language',
        ),
        migrations.AddField(
            model_name='libraryframework',
            name='languages',
            field=models.ManyToManyField(blank=True, related_name='libraries_frameworks', to='main.language'),
        ),
    ]