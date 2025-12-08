from django import forms
from .models import QuoteRequest

class QuoteRequestForm(forms.ModelForm):
    captcha_answer = forms.IntegerField(
        label='Security Question',
        help_text='Please solve the math problem to prove you are human.',
        required=True
    )
    
    # Custom choices for services to allow multiple selection
    SERVICES_CHOICES = [
        ('Channel Letters', 'Channel Letters'),
        ('LED Neon Signs', 'LED Neon Signs'),
        ('Light Boxes', 'Light Boxes'),
        ('Logo Signs', 'Logo Signs'),
    ]
    
    services_list = forms.MultipleChoiceField(
        choices=SERVICES_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Services you require"
    )

    class Meta:
        model = QuoteRequest
        fields = [
            'full_name', 'email', 'phone', 'company',
            'design_file', 'design_description', 'start_time'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ex: myname@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'design_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'start_time': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'full_name': 'Full Name',
            'email': 'E-mail',
            'phone': 'Phone Number',
            'company': 'Company',
            'design_description': 'Describe your design/s',
            'start_time': 'How soon are you ready to start?',
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        
        # Handle services list to string conversion
        services = cleaned_data.get('services_list')
        if services:
            cleaned_data['services'] = ', '.join(services)
        
        # CAPTCHA validation
        captcha_answer = cleaned_data.get('captcha_answer')
        if self.request:
            expected_answer = self.request.session.get('captcha_answer')
            if expected_answer is not None and captcha_answer != expected_answer:
                self.add_error('captcha_answer', 'Incorrect answer. Please try again.')
        
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.services = self.cleaned_data.get('services', '')
        if commit:
            instance.save()
        return instance
