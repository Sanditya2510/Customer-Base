# Generated by Django 2.1.3 on 2018-12-19 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp1', '0004_auto_20181219_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='data_sheet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp1.DataSheet'),
        ),
    ]