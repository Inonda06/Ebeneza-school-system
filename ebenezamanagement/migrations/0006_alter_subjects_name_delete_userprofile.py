# Generated by Django 4.2.9 on 2024-02-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebenezamanagement', '0005_remove_parent_parentprofile_alter_subjects_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='name',
            field=models.CharField(choices=[('Science', 'Science'), ('Kiswahili', 'Kiswahili'), ('English', 'English'), ('Maths', 'Maths'), ('History', 'History')], max_length=150),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
