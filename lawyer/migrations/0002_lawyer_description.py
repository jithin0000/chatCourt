# Generated by Django 3.0.5 on 2020-04-27 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]