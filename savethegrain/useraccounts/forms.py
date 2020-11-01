from django import forms  
from .models import STGUserProfile
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

USER_TYPE_CHOICES = (
        ('DNR','Donor'),
        ('NGO', 'NGO'),
    )


class STGUserRegister(UserCreationForm):

    email = forms.EmailField(required = False, widget= forms.EmailInput(attrs={'placeholder':'(Not Required)'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'password1': _('nothing'),
        }

class ProfileCreationForm(forms.ModelForm):
    user_type = forms.CharField(widget=forms.Select(choices=USER_TYPE_CHOICES) )
    Location = forms.Textarea(attrs={'rows':4, 'cols':1})
    class Meta:
        model = STGUserProfile
        fields = ['user_type','Location','Pincode']        