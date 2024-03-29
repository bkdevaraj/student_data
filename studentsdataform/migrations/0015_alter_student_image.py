# Generated by Django 4.2.3 on 2023-09-04 11:47

from django.db import migrations, models
import studentsdataform.models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsdataform', '0014_alter_student_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, default='no_image.jpg', null=True, upload_to=studentsdataform.models.student_image_path, validators=[studentsdataform.models.validate_image_extension, studentsdataform.models.validate_image_size]),
        ),
    ]
