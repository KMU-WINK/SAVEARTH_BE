# Generated by Django 4.1 on 2022-09-10 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0012_alter_profile_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="nickname",
        ),
    ]
