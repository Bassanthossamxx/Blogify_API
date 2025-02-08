# Generated by Django 5.1.6 on 2025-02-08 13:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Phone number must be a valid Egyptian number (e.g., +201XXXXXXXX or 01XXXXXXXX).', regex='^(\\+20|0)?1[0125]\\d{8}$')]),
        ),
    ]
