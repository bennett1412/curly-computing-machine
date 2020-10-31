from django import forms  
from .models import PostAd, DooSomething
from django.contrib.auth.forms import UserCreationForm



class STGUserCreationForm(UserCreationForm):

    email = forms.EmailField(required = False, widget= forms.EmailInput(attrs={'placeholder':'(Not Required)'}))
    Location = forms.TextInput(widget= forms.TextInput(attrs={'placeholder':'Enter your Location'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'password1': _('nothing'),
        }