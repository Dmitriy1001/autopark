# Generated by Django 3.2 on 2021-12-13 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0005_auto_20211213_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='driver_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog_app.driver'),
        ),
    ]
