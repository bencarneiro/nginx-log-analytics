# Generated by Django 4.1.5 on 2024-08-02 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Request",
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
                ("ip_address", models.CharField(max_length=64)),
                ("dt", models.DateTimeField()),
                ("request_type", models.CharField(max_length=16)),
                ("url", models.CharField(max_length=512)),
                ("protocol", models.CharField(max_length=64)),
                ("status_code", models.PositiveSmallIntegerField()),
                (
                    "bytes_transferred",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                (
                    "referrer_url",
                    models.CharField(blank=True, max_length=512, null=True),
                ),
                ("user_agent", models.CharField(blank=True, max_length=512, null=True)),
            ],
            options={
                "db_table": "request",
                "managed": True,
            },
        ),
    ]
