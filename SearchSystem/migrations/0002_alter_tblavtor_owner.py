# Generated by Django 4.0.5 on 2022-06-28 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblavtor',
            name='owner',
            field=models.CharField(max_length=256),
        ),
    ]
