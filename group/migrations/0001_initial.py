# Generated by Django 5.0.6 on 2024-08-29 23:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now=True, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('bio', models.TextField(blank=True, max_length=50, null=True)),
                ('leader', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Leader', to=settings.AUTH_USER_MODEL)),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Members', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'created_at',
            },
        ),
    ]
