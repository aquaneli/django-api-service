# Generated by Django 5.1.1 on 2025-02-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(max_length=500),
        ),
    ]
