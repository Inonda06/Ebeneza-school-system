# Generated by Django 4.2.9 on 2024-02-04 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebenezamanagement', '0003_remove_student_schoolpic_alter_subjects_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='name',
            field=models.CharField(choices=[('Kiswahili', 'Kiswahili'), ('Maths', 'Maths'), ('History', 'History'), ('English', 'English'), ('Science', 'Science')], max_length=150),
        ),
    ]
