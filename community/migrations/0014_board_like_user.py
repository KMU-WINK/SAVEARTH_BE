# Generated by Django 4.1 on 2022-09-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0013_remove_profile_nickname"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="like_user",
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
