# Generated by Django 3.0.5 on 2020-04-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0002_auto_20200426_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_number',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
