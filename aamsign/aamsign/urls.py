# mysite/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('design/', views.design, name='design'),
    
    # Channel Letters URLs
    path('illumination/front-lit/', views.front_lit, name='front_lit'),
    path('illumination/back-lit/', views.back_lit, name='back_lit'),
    path('illumination/front-back-lit/', views.front_back_lit, name='front_back_lit'),
    path('illumination/open-face/', views.open_face, name='open_face'),
    path('illumination/non-illuminated/', views.non_illuminated, name='non_illuminated'),
    path('illumination/rgb-programmable/', views.rgb_programmable, name='rgb_programmable'),
    
    # LED Neon Signs URLs
    path('neon/custom-neon/', views.custom_neon, name='custom_neon'),
    path('neon/neon-lamps/', views.neon_lamps, name='neon_lamps'),
    
    # Light Boxes URLs
    path('lightboxes/light-box/', views.light_box, name='light_box'),
    
    # Logo Signs URLs
    path('logos/logo-signs/', views.logo_signs, name='logo_signs'),
    
    # Quote page
    path('quote/', views.quote, name='quote'),
    
    # Shop URLs
    path('shop/', include('shop.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

