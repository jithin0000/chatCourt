# Generated by Django 3.0.5 on 2020-04-26 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('case', '0005_auto_20200426_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.FileField(upload_to='evidence/%Y/%m/%d/')),
                ('crated', models.DateTimeField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evidence_case', to='case.Case')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evidence_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
