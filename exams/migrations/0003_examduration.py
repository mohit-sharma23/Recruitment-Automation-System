# Generated by Django 4.1.2 on 2022-11-05 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exams", "0002_remove_questions_companyid_alter_options_questionid"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExamDuration",
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
                ("time", models.TimeField()),
            ],
        ),
    ]
