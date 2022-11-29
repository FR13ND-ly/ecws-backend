# Generated by Django 4.0.1 on 2022-01-23 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
