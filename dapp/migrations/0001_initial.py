# Generated by Django 4.2 on 2023-04-25 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('level', models.IntegerField()),
                ('message', models.TextField()),
                ('customer_first_name', models.CharField(max_length=40)),
                ('customer_last_name', models.CharField(max_length=40)),
                ('customer_phone_number', models.TextField()),
                ('customer_email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TicketLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('action', models.TextField()),
                ('table_name', models.TextField()),
                ('user_id', models.IntegerField()),
                ('old_data', models.JSONField(blank=True, null=True)),
                ('new_data', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ticket_log',
                'managed': False,
            },
        ),
    ]
