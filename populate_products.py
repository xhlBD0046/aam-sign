import os
import sys
import django

# Add the project directory to the Python path
sys.path.insert(0, r'e:\AAC\aam-sign\aamsign')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aamsign.settings')
django.setup()

from shop.models import Category, Product
from decimal import Decimal

print("Checking current product distribution...")
categories = ['front-lit', 'back-lit', 'front-back-lit', 'open-face', 'non-illuminated', 'rgb-programmable']

for slug in categories:
    try:
        category = Category.objects.get(slug=slug)
        count = Product.objects.filter(category=category).count()
        products = Product.objects.filter(category=category)
        print(f"{slug}: {count} products")
        for product in products:
            print(f"  - {product.name}")
    except Category.DoesNotExist:
        print(f"{slug}: Category not found")

print("\nCreating missing products...")

# Create or update products for each category
categories_to_populate = {
    'open-face': [
        {
            'name': 'Vintage Marquee Bar Sign',
            'slug': 'vintage-marquee-bar-sign',
            'description': 'Classic open-face channel letters with exposed bulbs for a retro look.',
            'price': Decimal('450.00'),
            'size_width': Decimal('36.00'),
            'size_height': Decimal('12.00'),
            'depth': Decimal('4.00'),
            'material': 'Rusted Metal Finish',
            'led_type': 'E14 Bulbs',
            'power_consumption': '100W',
            'stock': 3,
            'available': True,
        }
    ],
    'non-illuminated': [
        {
            'name': 'Brushed Steel Lobby Sign',
            'slug': 'brushed-steel-lobby-sign',
            'description': 'Professional non-illuminated 3D letters for office lobbies.',
            'price': Decimal('299.00'),
            'size_width': Decimal('48.00'),
            'size_height': Decimal('12.00'),
            'depth': Decimal('1.00'),
            'material': 'Stainless Steel',
            'led_type': 'None',
            'power_consumption': '0W',
            'stock': 15,
            'available': True,
        }
    ],
    'rgb-programmable': [
        {
            'name': 'Dynamic RGB Event Sign',
            'slug': 'dynamic-rgb-event-sign',
            'description': 'Programmable RGB sign with app control for dynamic color changing effects.',
            'price': Decimal('899.00'),
            'size_width': Decimal('60.00'),
            'size_height': Decimal('30.00'),
            'depth': Decimal('2.50'),
            'material': 'Acrylic & Aluminum',
            'led_type': 'Smart RGB Pixels',
            'power_consumption': '75W',
            'stock': 4,
            'available': True,
        }
    ],
    'front-back-lit': [
        {
            'name': 'Dual-Lit Storefront Sign',
            'slug': 'dual-lit-storefront-sign',
            'description': 'Maximum visibility with both front and back illumination.',
            'price': Decimal('799.00'),
            'size_width': Decimal('72.00'),
            'size_height': Decimal('36.00'),
            'depth': Decimal('3.00'),
            'material': 'Acrylic & Aluminum',
            'led_type': 'Dual LED Modules',
            'power_consumption': '80W',
            'stock': 5,
            'available': True,
        }
    ]
}

for category_slug, products_data in categories_to_populate.items():
    try:
        category = Category.objects.get(slug=category_slug)
        for product_data in products_data:
            product, created = Product.objects.update_or_create(
                slug=product_data['slug'],
                defaults={**product_data, 'category': category}
            )
            if created:
                print(f"Created: {product.name}")
            else:
                print(f"Updated: {product.name}")
    except Category.DoesNotExist:
        print(f"Category {category_slug} not found, skipping...")

print("\nFinal product distribution:")
for slug in categories:
    try:
        category = Category.objects.get(slug=slug)
        count = Product.objects.filter(category=category).count()
        print(f"{slug}: {count} products")
    except Category.DoesNotExist:
        print(f"{slug}: Category not found")

print("\nDone!")
