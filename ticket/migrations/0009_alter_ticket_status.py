# Generated by Django 4.0.6 on 2023-02-17 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0008_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('N', 'Ny'), ('O', 'Oppet'), ('J', 'Jobbar'), ('S', 'Stangd')], default='N', max_length=1),
        ),
    ]