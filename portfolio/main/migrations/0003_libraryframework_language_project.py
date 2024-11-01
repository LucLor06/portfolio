# Generated by Django 5.1.2 on 2024-10-24 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_generalskill_language_libraryframework'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryframework',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='libraries_frameworks', to='main.language'),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url', models.URLField()),
                ('start_date', models.DateField()),
                ('stop_date', models.DateField(blank=True, null=True)),
                ('libraries_frameworks', models.ManyToManyField(related_name='projects', to='main.libraryframework')),
            ],
        ),
    ]
