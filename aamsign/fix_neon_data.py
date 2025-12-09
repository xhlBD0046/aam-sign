import os
import django
import sys

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aamsign.settings')
django.setup()

from shop.models import Category, Product

def fix_neon_data():
    log_file = 'neon_fix_log.txt'
    with open(log_file, 'w') as f:
        try:
            # 1. Fix Category
            # Check if 'Neon' or 'neon-lamps' exists and unify them
            target_slug = 'Neon'
            
            # Try to get the category
            category = Category.objects.filter(slug=target_slug).first()
            
            if not category:
                f.write(f"Category '{target_slug}' not found. Creating it...\n")
                category = Category.objects.create(
                    name='Neon Signs',
                    slug=target_slug,
                    description='Standard pre-made neon signs.'
                )
                f.write(f"Created category: {category.name} (slug: {category.slug})\n")
            else:
                f.write(f"Category '{target_slug}' already exists.\n")

            # 2. Fix Products
            # Check if we have products in this category
            product_count = Product.objects.filter(category=category).count()
            f.write(f"Found {product_count} products in category '{target_slug}'.\n")

            if product_count == 0:
                f.write("Adding sample products...\n")
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
                    f.write(f"Ensured product exists: {p_data['name']}\n")
            
            f.write("DONE: Neon data check complete.\n")

        except Exception as e:
            f.write(f"ERROR: {str(e)}\n")

if __name__ == '__main__':
    fix_neon_data()
