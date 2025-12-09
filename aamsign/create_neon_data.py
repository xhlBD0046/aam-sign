import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aamsign.settings')
django.setup()

from shop.models import Category, Product

def create_data():
    print("--- Starting Data Creation ---")

    # 1. Create 'Neon' Category
    # Note: We use slug='Neon' because your view code specifically looks for Category.objects.get(slug='Neon')
    category, created = Category.objects.get_or_create(
        slug='Neon',
        defaults={
            'name': 'Neon',  # This is what shows in the dropdown
            'description': 'Neon Signs Category'
        }
    )
    
    if created:
        print(f"[SUCCESS] Created Category: {category.name} (slug: {category.slug})")
    else:
        print(f"[INFO] Category already exists: {category.name} (slug: {category.slug})")

    # 2. Create Sample Products
    # These will appear in the product list for this category
    products_to_create = [
        {
            'name': 'Custom Neon Text',
            'slug': 'custom-neon-text',
            'price': 199.00,
            'description': 'Custom text neon sign',
            'stock': 100
        },
        {
            'name': 'Coffee Bar Sign',
            'slug': 'coffee-bar-sign',
            'price': 149.00,
            'description': 'LED Neon sign for coffee shops',
            'stock': 50
        }
    ]

    for p_data in products_to_create:
        product, p_created = Product.objects.get_or_create(
            slug=p_data['slug'],
            defaults={
                'category': category,
                'name': p_data['name'],
                'price': p_data['price'],
                'description': p_data['description'],
                'stock': p_data['stock'],
                'available': True,
                # Required fields with defaults
                'size_width': 10.0,
                'size_height': 10.0,
                'depth': 1.0
            }
        )
        if p_created:
            print(f"[SUCCESS] Created Product: {product.name}")
        else:
            print(f"[INFO] Product already exists: {product.name}")

    print("--- Data Creation Complete ---")
    print("You should now see 'Neon' in the Category dropdown in Django Admin.")

if __name__ == '__main__':
    create_data()
