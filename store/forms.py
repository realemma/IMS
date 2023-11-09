from django.forms import ModelForm
from django import forms


from .models import Category,Location,Item,Allocation


class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title' , 'slug' )
        widgets = {
             'title':forms.TextInput(attrs={
                'class':'form-control'
            }),
             'slug':forms.TextInput(attrs={
                'class':'form-control'
            }),

        }

class LocForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('title' , 'slug' )
        widgets = {
             'title':forms.TextInput(attrs={
                'class':'form-control'
            }),
             'slug':forms.TextInput(attrs={
                'class':'form-control'
            }),
        }
class ItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        # Filter the queryset for the 'category' field to only include active categories
        self.fields['category'].queryset = Category.objects.filter(status='active')

    class Meta:
        model = Item
        fields = ('title' ,'category','quantity', )
        widgets = {
             'title':forms.TextInput(attrs={
                'class':'form-control'
            }),
             'category':forms.Select(attrs={
                'class':'form-control'
            }),
            'quantity':forms.NumberInput(attrs={
                'class':'form-control', 'min':'0'
            }),

        }

class AllocateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AllocateForm, self).__init__(*args, **kwargs)
        # Filter the queryset for the 'category' field to only include active categories
        self.fields['category'].queryset = Category.objects.filter(status='active')

        # Filter the queryset for the 'category' field to only include active categories
        self.fields['location'].queryset = Location.objects.filter(status='active')
    

    class Meta:
        model = Allocation
        fields = ('category','location','quantity', )
        widgets = {
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
