# Generated by Django 4.0 on 2021-12-12 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20210310_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrydata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
