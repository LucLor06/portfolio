# Generated by Django 5.1.2 on 2024-11-04 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_generalskill_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalskill',
            name='began_learning',
            field=models.DateField(default=datetime.date(2024, 11, 4)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='language',
            name='began_learning',
            field=models.DateField(default=datetime.date(2024, 11, 4)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='libraryframework',
            name='began_learning',
            field=models.DateField(default=datetime.date(2024, 11, 4)),
            preserve_default=False,
        ),
    ]