# Generated by Django 5.2.2 on 2025-07-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tools", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tool",
            name="average_rating",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="tool",
            name="review_count",
            field=models.IntegerField(default=0),
        ),
    ]
