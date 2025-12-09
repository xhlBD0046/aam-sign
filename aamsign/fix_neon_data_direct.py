import os
import django
import sys

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aamsign.settings')
django.setup()

from shop.models import Category, Product

def fix_neon_data_direct():
    try:
        # 1. Fix Category
        target_slug = 'Neon'
        category = Category.objects.filter(slug=target_slug).first()
        
        if not category:
            print(f"Category '{target_slug}' not found. Creating it...")
            category = Category.objects.create(
                name='Neon Signs',
                slug=target_slug,
                description='Standard pre-made neon signs.'
            )
            print(f"Created category: {category.name} (slug: {category.slug})")
        else:
            print(f"Category '{target_slug}' already exists.")

        # 2. Fix Products
        product_count = Product.objects.filter(category=category).count()
        print(f"Found {product_count} products in category '{target_slug}'.")

        if product_count == 0:
            print("Adding sample products...")
            products_data = [
                {
                    'name': 'Open Sign',
                    'slug': 'open-sign',
                    'price': 150.00,
                    'stock': 10,
                    'description': 'Classic OPEN sign',
                    'size_width': 20, 'size_height': 10, 'depth': 2
                },
                {
                    'name': 'Coffee Neon',
                    'slug': 'coffee-neon',
                    'price': 120.00,
                    'stock': 5,
                    'description': 'Coffee cup sign',
                    'size_width': 15, 'size_height': 15, 'depth': 2
                },
                {
                    'name': 'Bar Neon',
                    'slug': 'bar-neon',
                    'price': 180.00,
                    'stock': 8,
                    'description': 'Bar sign',
                    'size_width': 25, 'size_height': 12, 'depth': 2
                }
            ]

            for p_data in products_data:
                Product.objects.get_or_create(
                    slug=p_data['slug'],
                    defaults={
                        'category': category,
                        'name': p_data['name'],
                        'price': p_data['price'],
                        'stock': p_data['stock'],
                        'description': p_data['description'],
                        'size_width': p_data['size_width'],
                        'size_height': p_data['size_height'],
                        'depth': p_data['depth'],
                        'available': True
                    }
                )
                print(f"Ensured product exists: {p_data['name']}")
        
        print("DONE: Neon data check complete.")

    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == '__main__':
    fix_neon_data_direct()
