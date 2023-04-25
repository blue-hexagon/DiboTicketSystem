from django.views.generic import ListView

from dapp.models import TicketLog


class TicketLogListView(ListView):
    model = TicketLog
    context_object_name = 'ticketlogs'
    ordering = '-id'
    # ordering = ['-published_date']
    template_name = 'ticket-log/list-view.html'
