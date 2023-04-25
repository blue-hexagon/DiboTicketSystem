from django.db import connection
from django.urls import reverse_lazy
from psycopg2 import sql

from django.views.generic import ListView, CreateView, DetailView, UpdateView

from dapp.forms.ticket import TicketCreateModelForm, TicketUpdateModelForm
from dapp.models import Ticket


class TicketListView(ListView):
    model = Ticket
    context_object_name = 'tickets'
    ordering = ['-id']
    template_name = 'ticket/list-view.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_open=True)
        return queryset

class TicketListClosedView(ListView):
    model = Ticket
    context_object_name = 'tickets'
    ordering = ['-id']
    template_name = 'ticket/list-closed.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_open=False)
        return queryset


class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketCreateModelForm
    success_url = reverse_lazy('ticket-list')
    template_name = 'ticket/create-view.html'



class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'ticket/ticket-detail.html'
    context_object_name = 'ticket'


class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketUpdateModelForm
    success_url = reverse_lazy('ticket-list')
    template_name = 'ticket/ticket-update.html'


class TicketCloseView(UpdateView):
    model = Ticket
    fields = ['is_open']
    success_url = reverse_lazy('ticket-list')
    template_name = 'ticket/ticket-update.html'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
