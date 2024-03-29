from django import forms
from django.core.exceptions import ValidationError
from .models import Course, Contact, IndiaCities, IndianStates

class ContactForm(forms.ModelForm):
    city = forms.ModelChoiceField(queryset=IndiaCities.objects.all(), empty_label='Select City')
    state = forms.ModelChoiceField(queryset=IndianStates.objects.all(), empty_label='Select State')

    course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label='Select Course')

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'city', 'state', 'course', 'message']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        city = cleaned_data.get('city')
        state = cleaned_data.get('state')
        course = cleaned_data.get('course')
        message = cleaned_data.get('message')

        if not (name or email or phone or city or state or course or message):
            raise ValidationError("Please fill out at least one field.")

        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(char.isdigit() for char in name):
            raise ValidationError("Name should not contain numbers.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Email field is required.")
        forms.EmailField().clean(email)
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise ValidationError("Phone field is required.")
        if not phone.isdigit():
            raise ValidationError("Phone number should contain digits only.")
        if len(phone) != 10:
            raise ValidationError("Phone number should be 10 digits long.")
        return phone

    def clean(self):
        cleaned_data = super().clean()
        # Check if any field is empty
        if not any(cleaned_data.values()):
            raise ValidationError("Please fill in at least one field.")
        return cleaned_data