# Generated by Django 4.2.3 on 2023-09-04 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsdataform', '0012_alter_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='remarks',
            field=models.CharField(blank=True, help_text='Add remarks about the student', max_length=500, null=True),
        ),
    ]