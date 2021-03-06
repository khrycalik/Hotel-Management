# Generated by Django 4.0 on 2022-01-06 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_alter_object_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='object',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.object'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.client'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='payment_status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Paid', max_length=10),
        ),
    ]
