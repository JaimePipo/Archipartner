# Generated by Django 4.1.6 on 2023-02-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_telefono_user_fono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fono',
            field=models.CharField(max_length=10),
        ),
    ]
