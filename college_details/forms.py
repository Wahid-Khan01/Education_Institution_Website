from django import forms
from .models import  UserProfile2


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile2
        fields = ['name', 'email', 'phone', 'date_of_birth', 'city', 'state', 'course']