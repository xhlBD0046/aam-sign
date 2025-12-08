from django import forms


class QuoteForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your full name',
            'class': 'form-input'
        })
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'your.email@example.com',
            'class': 'form-input'
        })
    )
    
    phone = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '(123) 456-7890',
            'class': 'form-input'
        })
    )
    
    company = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your company name (optional)',
            'class': 'form-input'
        })
    )
    
    design_file = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-file-input',
            'accept': '.pdf,.jpg,.jpeg,.png,.ai,.psd'
        }),
        help_text='Upload your design file or draft (PDF, JPG, PNG, AI, PSD)'
    )
    
    design_description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Describe your design requirements...',
            'class': 'form-textarea',
            'rows': 5
        })
    )
    
    SERVICES_CHOICES = [
        ('channel_letters', 'Channel Letters'),
        ('led_neon_signs', 'LED Neon Signs'),
        ('light_boxes', 'Light Boxes'),
        ('logo_signs', 'Logo Signs'),
    ]
    
    services = forms.MultipleChoiceField(
        choices=SERVICES_CHOICES,
        required=True,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-checkbox'
        })
    )
    
    TIMELINE_CHOICES = [
        ('immediate', 'Immediate'),
        ('1-2weeks', '1-2 Weeks'),
        ('1month', '1 Month'),
        ('more_than_1_month', 'More than 1 Month'),
    ]
    
    start_time = forms.ChoiceField(
        choices=TIMELINE_CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='How soon are you ready to start?'
    )
    
    # Honeypot field - should remain empty
    website = forms.CharField(
        required=False,
        widget=forms.HiddenInput(attrs={
            'class': 'honeypot-field'
        })
    )
    
    def clean_website(self):
        website = self.cleaned_data.get('website', '')
        if website:
            raise forms.ValidationError('Spam detected.')
        return website
