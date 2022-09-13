# Generated by Django 4.1 on 2022-09-13 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('steps', models.IntegerField()),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
                ('distance', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
