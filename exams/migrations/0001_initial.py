# Generated by Django 4.1.2 on 2022-10-09 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Questions",
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
                ("question", models.TextField()),
                ("score", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Options",
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
                ("option", models.TextField()),
                (
                    "questionId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exams.questions",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Answers",
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
                    "optionId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exams.options"
                    ),
                ),
                (
                    "questionId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exams.questions",
                    ),
                ),
            ],
        ),
    ]
