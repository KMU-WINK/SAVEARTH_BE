# Generated by Django 4.1 on 2022-09-10 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0016_remove_profile_like_posts_profile_like_posts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="like_posts",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="community.board",
            ),
        ),
    ]
