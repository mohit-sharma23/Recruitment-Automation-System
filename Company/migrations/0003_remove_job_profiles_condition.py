# Generated by Django 4.1.2 on 2023-04-27 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Company", "0002_rename_condi_tion_job_profiles_condition"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job_profiles",
            name="condition",
        ),
    ]