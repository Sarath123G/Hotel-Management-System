from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=100)),
                ('room_type', models.CharField(choices=[('Single', 'Single'), ('Double', 'Double'), ('Deluxe', 'Deluxe'), ('Suite', 'Suite')], max_length=20)),
                ('check_in_date', models.DateField()),
                ('no_of_days', models.PositiveIntegerField()),
            ],
        ),
    ]
