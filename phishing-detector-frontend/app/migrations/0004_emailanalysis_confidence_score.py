# Generated by Django 5.1.2 on 2024-11-02 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_emailanalysis_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailanalysis',
            name='confidence_score',
            field=models.FloatField(default=0.0),
        ),
    ]
