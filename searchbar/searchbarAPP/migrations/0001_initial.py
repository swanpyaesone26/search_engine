# Generated by Django 5.1.3 on 2025-01-09 05:03

import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Movie',
            },
        ),
    ]
