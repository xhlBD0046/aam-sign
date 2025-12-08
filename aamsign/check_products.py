import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aamsign.settings')
django.setup()

from shop.models import Category, Product

categories = ['front-lit', 'back-lit', 'front-back-lit', 'open-face', 'non-illuminated', 'rgb-programmable']

print("Checking product counts:", flush=True)
for slug in categories:
    try:
        category = Category.objects.get(slug=slug)
        count = Product.objects.filter(category=category).count()
        print(f"{slug}: {count} products", flush=True)
    except Category.DoesNotExist:
        print(f"{slug}: Category not found", flush=True)
