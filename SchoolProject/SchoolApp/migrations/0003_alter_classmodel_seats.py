# Generated by Django 5.0.4 on 2024-04-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("SchoolApp", "0002_rename_child_childmodel_rename_class_classmodel_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classmodel",
            name="seats",
            field=models.IntegerField(default=4),
        ),
    ]