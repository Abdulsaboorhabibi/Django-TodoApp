# Generated by Django 5.0.4 on 2024-04-08 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TodoApp", "0002_todomodel_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todomodel",
            name="slug",
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
