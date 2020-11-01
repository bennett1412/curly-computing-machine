from django import forms  
from .models import STGUserProfile
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm



class STGUserRegister(UserCreationForm):

    email = forms.EmailField(required = False, widget= forms.EmailInput(attrs={'placeholder':'(Not Required)'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'password1': _('nothing'),
        }

class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = STGUserProfile
        fields = ['user_type','Location','Pincode']        