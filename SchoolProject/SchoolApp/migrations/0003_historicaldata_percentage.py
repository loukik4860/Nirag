# Generated by Django 5.0.4 on 2024-05-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("SchoolApp", "0002_alter_classmodel_seats_historicaldata_subjectmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicaldata",
            name="percentage",
            field=models.FloatField(blank=True, null=True),
        ),
    ]