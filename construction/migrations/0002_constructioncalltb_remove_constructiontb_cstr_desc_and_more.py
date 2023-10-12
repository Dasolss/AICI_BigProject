# Generated by Django 4.2.2 on 2023-06-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("construction", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConstructionCallTB",
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
                (
                    "cstr_desc",
                    models.CharField(max_length=20, verbose_name="file name"),
                ),
                (
                    "cstr_file",
                    models.FileField(
                        upload_to="construction/%Y/%m/%d", verbose_name="uploaded file"
                    ),
                ),
                (
                    "started_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="construction date"
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="constructiontb",
            name="cstr_desc",
        ),
        migrations.RemoveField(
            model_name="constructiontb",
            name="cstr_file",
        ),
        migrations.RemoveField(
            model_name="constructiontb",
            name="started_at",
        ),
    ]
