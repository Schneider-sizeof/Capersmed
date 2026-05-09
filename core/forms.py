from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone', 'company', 'country', 'message', 'wholesale_interest']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name*'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address*'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message*', 'rows': 4}),
            'wholesale_interest': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
