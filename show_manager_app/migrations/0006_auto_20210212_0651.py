# Generated by Django 2.2 on 2021-02-12 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_manager_app', '0005_auto_20210212_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(verbose_name='%B %d, %Y'),
        ),
    ]