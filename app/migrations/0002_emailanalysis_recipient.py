# Generated by Django 5.1.2 on 2024-11-01 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailanalysis',
            name='recipient',
            field=models.CharField(default='unknown@example.com', max_length=255),
        ),
    ]
