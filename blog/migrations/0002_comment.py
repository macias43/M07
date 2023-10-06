# Generated by Django 4.2.6 on 2023-10-06 00:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(max_length=200)),
                ("text", models.TextField()),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("approved_comment", models.BooleanField(default=False)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blog.post",
                    ),
                ),
            ],
        ),
    ]
