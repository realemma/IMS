from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm



from .models import note,Users,Userprofile

class UpdateForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['first_name','username', 'email','password1', 'password2']


class UpdStatus(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['user','is_admin']
        widgets = {
             'user':forms.Select(attrs={
                'class':'form-control', 
            }),
           
          
        }





class NoteForm(forms.ModelForm):
    class Meta:
        model = note
        fields = ('title' , 'email', 'username', 'password' )
        widgets = {
             'title':forms.TextInput(attrs={
                'class':'form-control'
            }),
             'email':forms.EmailInput(attrs={
                'class':'form-control'
            }),

             'username':forms.TextInput(attrs={
                'class':'form-control'
            }),

             'password':forms.TextInput(attrs={
                'class':'form-control'
            }),

        }

