# Generated by Django 4.2.2 on 2023-07-27 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'student', 'verbose_name_plural': 'students'},
        ),
    ]
