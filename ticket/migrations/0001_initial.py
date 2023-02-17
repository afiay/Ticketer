# Generated by Django 4.0.6 on 2023-02-17 20:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Ar Nummer / Plockplats')),
                ('ticket_location', models.CharField(choices=[('ALL', 'ALL'), ('Logistics_1', 'Logistics_2'), ('Logistics_2', 'Logistics_3'), ('Logistics_3', 'Logistics_4'), ('Logistics_4', 'Logistics_5'), ('AHL_station_2', 'Ahl_station_3'), ('Ahl_station_3', 'Ahl_station_4'), ('Ahl_station_4', 'Ahl_station_5'), ('Stative_station_0', 'Stative_station_0'), ('Stative_station_1', 'Stative_station_1'), ('Stative_station_2', 'Stative_station_2'), ('Stative_station_3', 'Stative_station_3'), ('Stative_station_4', 'Stative_station_4'), ('1000_station_0', '1000_station_0'), ('1000_station_1', '1000_station_1'), ('1000_station_2', '1000_station_2'), ('1000_station_3', '1000_station_3'), ('1000_station_4', '1000_station_4'), ('Compact_station_0', 'Compact_station_0'), ('Compact_station_1', 'Compact_station_1'), ('Compact_station_2', 'Compact_station_2'), ('Compact_station_3', 'Compact_station_3'), ('Compact_station_4', 'Compact_station_4'), ('Pack&plock_0', 'Pack&plock_0'), ('Pack&plock_1', 'Pack&plock_1'), ('Pack&plock_2', 'Pack&plock_2'), ('Pack&plock_3', 'Pack&plock_3'), ('Pack&plock_4', 'Pack&plock_4'), ('Del_Montage_0', 'Del_Montage_0'), ('Del_Montage_1', 'Del_Montage_1'), ('Del_Montage_2', 'Del_Montage_2'), ('Del_Montage_3', 'Del_Montage_3'), ('Del_Montage_4', 'Del_Montage_4')], default='0', max_length=36)),
                ('image', models.ImageField(blank=True, upload_to='media/images')),
                ('content', models.TextField()),
                ('date_ticketed', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('N', 'Ny'), ('O', 'Oppet'), ('J', 'Jobbar'), ('S', 'Stängd')], default='N', max_length=1)),
                ('ticket_type', models.CharField(choices=[('Tracksys', 'Tracksys'), ('AHL', 'AHL'), ('Stative', 'Stative'), ('Compact', 'Compact'), ('Pack & Plock', 'Pack & Plock'), ('DelMontage', 'DelMontage')], default='Tracksys', max_length=50)),
                ('urgency', models.IntegerField(default=1, error_messages={'max_value': 'Välj ett brådskande mellanrum 1 och 10', 'min_value': 'Välj ett brådskande mellanrum 1 och 10'}, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Brotskande (1-10)')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Replie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date_replied', models.DateTimeField(default=django.utils.timezone.now)),
                ('replier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='ticket.ticket')),
            ],
        ),
    ]
