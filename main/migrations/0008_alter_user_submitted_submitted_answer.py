# Generated by Django 3.2.17 on 2023-02-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_user_submitted_submitted_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_submitted',
            name='Submitted_Answer',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
