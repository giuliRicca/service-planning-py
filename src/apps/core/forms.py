from multiprocessing import Event
from django import forms
from apps.core.models import OrderItem, ServiceType, ServiceTime, Team, Event

class DateInput(forms.DateInput):
    input_type = 'date'

class ServiceTypeForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    recur = forms.ChoiceField(required=True,choices=ServiceType.RECUR_OPTIONS, 
    widget=forms.Select(attrs={
        'class': 'form-control'
    }), label='Service Type Recur')
    times = forms.ModelMultipleChoiceField(required=True, queryset=ServiceTime.objects.all(),
    widget=forms.SelectMultiple(attrs={
        'class': 'form-control'
    }))
    teams = forms.ModelMultipleChoiceField(queryset=Team.objects.all(),
    widget=forms.SelectMultiple(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = ServiceType
        fields = ['name', 'recur','times', 'teams']

class EventForm(forms.ModelForm):
    service_type = forms.ModelChoiceField(required=True, queryset=ServiceType.objects.all(),
    widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    date = forms.DateField(required=True, 
    widget=DateInput(attrs={
        'class': 'form-control',
        'id': 'date',
    }))

    class Meta:
        model = Event
        fields = ['service_type', 'title','date']


class OrderItemForm(forms.ModelForm):
    minutes = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'min': 0,
            'max': 59,
            'placeholder': 0,
            "step": '1',
            }
    ), initial=0)
    seconds = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'min': 0,
            'max': 59,
            'placeholder': 0,
            'step': 1,
            }
    ), initial=0)
    item_type = forms.ChoiceField(choices=OrderItem.TYPE_OPTIONS, widget=forms.Select(
        attrs={'class': 'form-control'}
    ), required=True, initial='a')
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ), required=True)
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Optional', 'rows': "3"}
    ), required=False)
    person = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Optional'}
    ), required=False)


    class Meta:
        model = OrderItem
        fields = ['length', 'title','item_type', 'description', 'person']

