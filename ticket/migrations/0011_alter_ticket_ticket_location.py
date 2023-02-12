# Generated by Django 4.0.6 on 2023-02-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0010_alter_ticket_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_location',
            field=models.CharField(choices=[('ALL', 'ALL'), ('Logistics_1', 'Logistics_2'), ('Logistics_2', 'Logistics_3'), ('Logistics_3', 'Logistics_4'), ('Logistics_4', 'Logistics_5'), ('AHL_station_2', 'Ahl_station_3'), ('Ahl_station_3', 'Ahl_station_4'), ('Ahl_station_4', 'Ahl_station_5'), ('Stative_station_0', 'Stative_station_0'), ('Stative_station_1', 'Stative_station_1'), ('Stative_station_2', 'Stative_station_2'), ('Stative_station_3', 'Stative_station_3'), ('Stative_station_4', 'Stative_station_4'), ('1000_station_0', '1000_station_0'), ('1000_station_1', '1000_station_1'), ('1000_station_2', '1000_station_2'), ('1000_station_3', '1000_station_3'), ('1000_station_4', '1000_station_4'), ('Compact_station_0', 'Compact_station_0'), ('Compact_station_1', 'Compact_station_1'), ('Compact_station_2', 'Compact_station_2'), ('Compact_station_3', 'Compact_station_3'), ('Compact_station_4', 'Compact_station_4'), ('Pack&plock_0', 'Pack&plock_0'), ('Pack&plock_1', 'Pack&plock_1'), ('Pack&plock_2', 'Pack&plock_2'), ('Pack&plock_3', 'Pack&plock_3'), ('Pack&plock_4', 'Pack&plock_4'), ('Del_Montage_0', 'Del_Montage_0'), ('Del_Montage_1', 'Del_Montage_1'), ('Del_Montage_2', 'Del_Montage_2'), ('Del_Montage_3', 'Del_Montage_3'), ('Del_Montage_4', 'Del_Montage_4')], default='0', max_length=36),
        ),
    ]
