import os
import sys
import django

sys.path.insert(0, r'e:\AAC\aam-sign\aamsign')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aamsign.settings')
django.setup()

from shop.models import Category, Product

print("=" * 60)
print("Current Products in Database")
print("=" * 60)

categories = Category.objects.all().order_by('slug')
for category in categories:
    products = Product.objects.filter(category=category)
    print(f"\n{category.name} ({category.slug}):")
    print(f"  Total products: {products.count()}")
    for product in products:
        print(f"  - {product.name} (${product.price}) - Available: {product.available}")

print("\n" + "=" * 60)
