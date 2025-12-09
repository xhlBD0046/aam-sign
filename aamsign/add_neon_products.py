import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aamsign.settings')
django.setup()

from shop.models import Category, Product
from django.core.files.base import ContentFile

def add_neon_products():
    # Create or get the category
    category, created = Category.objects.get_or_create(
        slug='Neon',
        defaults={
            'name': 'Neon Signs',
            'description': 'Custom and standard neon signs.'
        }
    )
    
    if created:
        print(f"Created category: {category.name} (slug: {category.slug})")
    else:
        print(f"Found existing category: {category.name} (slug: {category.slug})")

    # Sample products data
    products_data = [
        {
            'name': 'Open Sign',
            'slug': 'open-sign',
            'description': 'Classic "OPEN" neon sign for businesses.',
            'price': 150.00,
            'size_width': 20.00,
            'size_height': 10.00,
            'depth': 2.00,
            'material': 'Acrylic, LED Neon Flex',
            'led_type': 'Standard',
            'power_consumption': '24W',
            'stock': 10,
        },
        {
            'name': 'Coffee Cup Neon',
            'slug': 'coffee-cup-neon',
            'description': 'Bright coffee cup neon sign for cafes.',
            'price': 120.00,
            'size_width': 15.00,
            'size_height': 15.00,
            'depth': 2.00,
            'material': 'Acrylic, LED Neon Flex',
            'led_type': 'Standard',
            'power_consumption': '18W',
            'stock': 5,
        },
        {
            'name': 'Custom Text Neon',
            'slug': 'custom-text-neon',
            'description': 'Customizable text neon sign.',
            'price': 200.00,
            'size_width': 30.00,
            'size_height': 10.00,
            'depth': 2.00,
            'material': 'Acrylic, LED Neon Flex',
            'led_type': 'RGB',
            'power_consumption': '36W',
            'stock': 100,
        }
    ]

    for p_data in products_data:
        product, created = Product.objects.get_or_create(
            slug=p_data['slug'],
            defaults={
                'category': category,
                'name': p_data['name'],
                'description': p_data['description'],
                'price': p_data['price'],
                'size_width': p_data['size_width'],
                'size_height': p_data['size_height'],
                'depth': p_data['depth'],
                'material': p_data['material'],
                'led_type': p_data['led_type'],
                'power_consumption': p_data['power_consumption'],
                'stock': p_data['stock'],
                'available': True
            }
        )
        if created:
            print(f"Created product: {product.name}")
        else:
            print(f"Product already exists: {product.name}")

if __name__ == '__main__':
    add_neon_products()
