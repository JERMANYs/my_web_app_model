# Generated by Django 4.2.2 on 2023-08-03 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0004_alter_student_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'major',
                'verbose_name_plural': 'majors',
            },
        ),
    ]
