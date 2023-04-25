from django import forms

from dapp.models import Ticket


class TicketCreateModelForm(forms.ModelForm):
    LEVEL_CHOICES = (
        (1, 'Level 1'),
        (2, 'Level 2'),
        (3, 'Level 3'),
    )
    level = forms.ChoiceField(choices=LEVEL_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Ticket
        fields = ['level','problem_message','status_message','user','customer_first_name','customer_last_name','customer_phone_number','customer_email']
        widgets = {
            'level': forms.Select(attrs={'class': 'form-select'}),
            'problem_message': forms.Textarea(attrs={'class': 'form-control'}),
            'status_message': forms.Textarea(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-select'}),
            'customer_first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'level': 'Ticket Level',
            'problem_message': 'Problem Specifikation',
            'status_message': 'Status på Udredning',
            'user': 'Ansvarlig Bruger',
            'customer_first_name': 'Kunde Fornavn',
            'customer_last_name': 'Kunde Efternavn',
            'customer_phone_number': 'Kunde Telefon',
            'customer_email': 'Kunde Email',
        }

class TicketUpdateModelForm(forms.ModelForm):
    LEVEL_CHOICES = (
        (1, 'Level 1'),
        (2, 'Level 2'),
        (3, 'Level 3'),
    )
    level = forms.ChoiceField(choices=LEVEL_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Ticket
        fields = ['level','status_message','solution_message']
        widgets = {
            'level': forms.Select(attrs={'class': 'form-select'}),
            'status_message': forms.Textarea(attrs={'class': 'form-control'}),
            'solution_message': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'level': 'Ticket Level',
            'status_message': 'Status på Udredning',
            'problem_message': 'Problem Specifikation',
        }

