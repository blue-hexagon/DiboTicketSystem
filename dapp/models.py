from django.db import models

from dauth.models import AuthUser


class Ticket(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    level = models.IntegerField()
    problem_message = models.TextField()
    status_message = models.TextField(blank=True, null=True)
    solution_message = models.TextField(blank=True, null=True)
    is_open = models.BooleanField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    customer_first_name = models.CharField(max_length=40)
    customer_last_name = models.CharField(max_length=40)
    customer_phone_number = models.TextField()
    customer_email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ticket'


class TicketLog(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    action = models.TextField()
    table_name = models.TextField()
    user_id = models.IntegerField()
    old_data = models.JSONField(blank=True, null=True)
    new_data = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_log'
