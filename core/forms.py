from django.forms import ModelForm
from django import forms


from .models import Request
from store.models import Category,Location


class RequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        # Filter the queryset for the 'category' field to only include active categories
        self.fields['category'].queryset = Category.objects.filter(status='active')

        # Filter the queryset for the 'category' field to only include active categories
        self.fields['location'].queryset = Location.objects.filter(status='active')
    

    class Meta:
        model = Request
        fields = ('item','category','location','quantity', )
        widgets = {
            'item':forms.Select(attrs={
                'class':'form-control'
            }),
            'category':forms.Select(attrs={
                'class':'form-control'
            }),
             'location':forms.Select(attrs={
                'class':'form-control'
            }),
            'quantity':forms.NumberInput(attrs={
                'class':'form-control', 'min':'0'
            }),

        }


class ApproveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ApproveForm, self).__init__(*args, **kwargs)
        # Filter the queryset for the 'category' field to only include active categories
        self.fields['category'].queryset = Category.objects.filter(status='active')

        # Filter the queryset for the 'category' field to only include active categories
        self.fields['location'].queryset = Location.objects.filter(status='active')
    class Meta:
        model = Request
        fields = ('item','category','location','quantity','comments' )
        widgets = {
            'item':forms.Select(attrs={
                'class':'form-control'
            }),
            'category':forms.Select(attrs={
                'class':'form-control'
            }),
             'location':forms.Select(attrs={
                'class':'form-control'
            }),
            'quantity':forms.NumberInput(attrs={
                'class':'form-control', 'min':'0'
            }),
            'comments':forms.Textarea(attrs={
                'class':'form-control',
            }),

        }

