# Generated by Django 3.0.5 on 2020-04-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0004_case_verdict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='verdict',
            field=models.TextField(blank=True, null=True),
        ),
    ]
