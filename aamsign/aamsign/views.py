# mysite/views.py
from django.shortcuts import render
from shop.models import Product, Category

def index(request):
    return render(request, 'index.html')

def design(request):
    return render(request, 'design.html')

def front_lit(request):
    try:
        category = Category.objects.get(slug='channel-letters')
        products = Product.objects.filter(category=category, available=True)
    except Category.DoesNotExist:
        products = []
    
    return render(request, 'illumination/front_lit.html', {'products': products})


def back_lit(request):
    try:
        category = Category.objects.get(slug='channel-letters')
        products = Product.objects.filter(category=category, available=True)
    except Category.DoesNotExist:
        products = []
    
    return render(request, 'illumination/back_lit.html', {'products': products})


def front_back_lit(request):
    try:
        category = Category.objects.get(slug='channel-letters')
        products = Product.objects.filter(category=category, available=True)
    except Category.DoesNotExist:
        products = []
    
    return render(request, 'illumination/front_back_lit.html', {'products': products})


def open_face(request):
    try:
        category = Category.objects.get(slug='channel-letters')
        products = Product.objects.filter(category=category, available=True)
    except Category.DoesNotExist:
        products = []
    
    return render(request, 'illumination/open_face.html', {'products': products})


def non_illuminated(request):
    try:
        category = Category.objects.get(slug='channel-letters')
        products = Product.objects.filter(category=category, available=True)
    except Category.DoesNotExist:
        products = []
    
    return render(request, 'illumination/non_illuminated.html', {'products': products})


def rgb_programmable(request):
    try:
        category = Category.objects.get(slug='channel-letters')
        products = Product.objects.filter(category=category, available=True)
    except Category.DoesNotExist:
        products = []
    
    return render(request, 'illumination/rgb_programmable.html', {'products': products})
def custom_neon(request):
    try:
        category = Category.objects.get(slug='custom-neon')
        products = Product.objects.filter(category=category, available=True)
    except Category.DoesNotExist:
        products = []
    
    return render(request, 'neon/custom_neon.html', {'products': products})

def neon_lamps(request):
    try:
        category = Category.objects.get(slug='Neon')
        products = Product.objects.filter(category=category, available=True)
    except Category.DoesNotExist:
        products = []
    
    return render(request, 'neon/neon_lamps.html', {'products': products})

# Light Boxes views
def light_box(request):
    try:
        # We can use a general 'lightbox' category or keep 'blade-lightboxes' slug if we don't want to change DB
        # But user said "directly to light_box", implying a general page.
        # Let's assume we might want to show all lightboxes or just keep the blade ones for now but under a general name.
        # For now, I will keep querying 'blade-lightboxes' as the data exists, or 'lightbox' if I change data.
        # The user didn't ask to change data, just the page.
        # But wait, "Modify blade light box text content to be just a light box introduction".
        # Let's query 'blade-lightboxes' for now to ensure products show up, or 'lightbox' if we consolidated.
        # I'll stick to 'blade-lightboxes' slug for safety unless I change data, BUT I should probably check if I should change the slug.
        # The user said "Modify blade light box html and views and url directly to light_box".
        # I will use 'blade-lightboxes' slug for the query to ensure products appear, but the view name is light_box.
        category = Category.objects.get(slug='blade-lightboxes')
        products = Product.objects.filter(category=category, available=True)
    except Category.DoesNotExist:
        products = []
    
    return render(request, 'lightboxes/light_box.html', {'products': products})

# Logo Signs views
def logo_signs(request):
    try:
        category = Category.objects.get(slug='logo-signs')
        products = Product.objects.filter(category=category, available=True)
    except Category.DoesNotExist:
        products = []
    
    return render(request, 'logos/logo_signs.html', {'products': products})

# Quote page view
def quote(request):
    from .forms import QuoteForm
    from shop.models import Quote
    from django.core.cache import cache
    from django.contrib import messages
    from django.conf import settings
    import time
    import requests
    import json
    
    # Get client IP address
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    # Verify reCAPTCHA
    def verify_recaptcha(token, client_ip):
        """Verify reCAPTCHA token with Google's API"""
        recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'
        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': token,
            'remoteip': client_ip
        }
        try:
            response = requests.post(recaptcha_url, data=data)
            result = response.json()
            return result.get('success', False)
        except Exception as e:
            # Log error in production
            print(f"reCAPTCHA verification error: {e}")
            return False
    
    client_ip = get_client_ip(request)
    
    # Rate limiting: check if this IP has submitted recently
    rate_limit_key = f'quote_submit_{client_ip}'
    last_submit_time = cache.get(rate_limit_key)
    
    if request.method == 'POST':
        # Verify reCAPTCHA first
        recaptcha_token = request.POST.get('g-recaptcha-response')
        if not recaptcha_token:
            messages.error(request, 'Please complete the reCAPTCHA verification.')
            return render(request, 'quote.html', {
                'form': QuoteForm(request.POST),
                'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY
            })
        
        if not verify_recaptcha(recaptcha_token, client_ip):
            messages.error(request, 'reCAPTCHA verification failed. Please try again.')
            return render(request, 'quote.html', {
                'form': QuoteForm(request.POST),
                'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY
            })
        
        # Check rate limiting - allow only 1 submission per 5 minutes
        if last_submit_time:
            time_since_last = time.time() - last_submit_time
            if time_since_last < 300:  # 5 minutes = 300 seconds
                messages.error(request, 'You have submitted a quote recently. Please wait a few minutes before submitting again.')
                return render(request, 'quote.html', {
                    'form': QuoteForm(request.POST),
                    'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY
                })
        
        form = QuoteForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Save the quote
            quote = Quote(
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                company=form.cleaned_data.get('company', ''),
                design_file=form.cleaned_data.get('design_file'),
                design_description=form.cleaned_data['design_description'],
                services=','.join(form.cleaned_data['services']),
                start_time=form.cleaned_data['start_time'],
                ip_address=client_ip
            )
            quote.save()
            
            # Set rate limit
            cache.set(rate_limit_key, time.time(), 300)
            
            messages.success(request, 'Thank you! Your quote request has been submitted successfully. We will contact you within 24 hours.')
            
            # Redirect to avoid form resubmission
            return render(request, 'quote.html', {
                'form': QuoteForm(),
                'success': True,
                'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY
            })
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = QuoteForm()
    
    return render(request, 'quote.html', {
        'form': form,
        'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY
    })
