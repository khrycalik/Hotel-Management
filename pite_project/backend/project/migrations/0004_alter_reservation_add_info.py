# Generated by Django 4.0 on 2021-12-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_reservation_add_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='add_info',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
