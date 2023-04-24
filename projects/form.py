from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, ListProperty
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }

class ListPropertyForm(ModelForm):
    class Meta:
        model = ListProperty
        fields = '__all__'
        exclude = ['profile']
        
  
        widgets = {
            'bachelers_allowed': forms.RadioSelect(attrs={'class': 'checkbox-group'}),
            'furnished': forms.RadioSelect(attrs={'class': 'checkbox-group'}),
            'balcony': forms.RadioSelect(attrs={'class': 'checkbox-group'}),
            'parking': forms.RadioSelect(attrs={'class': 'checkbox-group'}),
            'independent': forms.RadioSelect(attrs={'class': 'checkbox-group'}),
            'by': forms.RadioSelect(attrs={'class': 'checkbox-group'}),
            'category': forms.RadioSelect(attrs={'class': 'checkbox-group'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(ListPropertyForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
       