# Generated by Django 4.2.9 on 2024-01-30 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classteacher', models.BooleanField()),
                ('NationalID', models.IntegerField()),
            ],
        ),
    ]
