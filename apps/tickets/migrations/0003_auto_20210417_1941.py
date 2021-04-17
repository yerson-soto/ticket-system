# Generated by Django 3.1.7 on 2021-04-17 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20210417_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'default_related_name': 'employees'},
        ),
        migrations.CreateModel(
            name='TicketTimeEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('date_from', models.DateTimeField(auto_now_add=True)),
                ('date_to', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_entries', to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_entries', to='tickets.ticket')),
            ],
            options={
                'default_related_name': 'time_entries',
            },
        ),
    ]