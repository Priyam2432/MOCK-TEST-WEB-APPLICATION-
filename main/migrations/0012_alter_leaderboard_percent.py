# Generated by Django 3.2.17 on 2023-04-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20230418_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboard',
            name='percent',
            field=models.FloatField(max_length=100),
        ),
    ]
