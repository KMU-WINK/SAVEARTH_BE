# Generated by Django 4.1 on 2022-09-10 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0008_like_board_liked_users_delete_profile_like_board_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="like",
            old_name="Board",
            new_name="board",
        ),
    ]