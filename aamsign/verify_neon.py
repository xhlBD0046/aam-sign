import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aamsign.settings')
django.setup()

from shop.models import Category, Product

def verify_neon():
    try:
        category = Category.objects.get(slug='Neon')
        print(f"Category found: {category.name}")
        products = Product.objects.filter(category=category)
        print(f"Products found: {products.count()}")
        for p in products:
            print(f"- {p.name}")
    except Category.DoesNotExist:
        print("Category 'Neon' NOT found.")

if __name__ == '__main__':
    verify_neon()
