# Generated by Django 4.2.9 on 2024-02-04 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebenezamanagement', '0010_delete_perforance_alter_teacher_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(choices=[('Kiswahili', 'Kiswahili'), ('Science', 'Science'), ('Maths', 'Maths'), ('English', 'English'), ('History', 'History')], max_length=150),
        ),
    ]
