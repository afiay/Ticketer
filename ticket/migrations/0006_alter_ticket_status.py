# Generated by Django 4.0.6 on 2023-02-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_remove_ticket_privacy_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('N', 'New'), ('O', 'Open'), ('J', 'jobbar'), ('S', 'stängd')], default='N', max_length=1),
        ),
    ]
