# Generated by Django 2.1.11 on 2021-09-17 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Dashboard', '0003_alter_country_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='phone',
            new_name='phone_digit',
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]