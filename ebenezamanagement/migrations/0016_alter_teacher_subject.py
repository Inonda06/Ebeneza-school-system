# Generated by Django 4.2.9 on 2024-02-07 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebenezamanagement', '0015_student_performance_alter_teacher_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(choices=[('Science', 'Science'), ('English', 'English'), ('Kiswahili', 'Kiswahili'), ('Maths', 'Maths'), ('History', 'History')], max_length=150),
        ),
    ]
