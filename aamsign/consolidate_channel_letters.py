import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aamsign.settings')
django.setup()

from shop.models import Category, Product

def consolidate_products():
    print("--- Starting Consolidation ---")

    # 1. Create 'Channel Letters' Category
    target_category, created = Category.objects.get_or_create(
        slug='channel-letters',
        defaults={
            'name': 'Channel Letters',
            'description': 'All types of channel letter signs.'
        }
    )
    if created:
        print(f"Created target category: {target_category.name}")
    else:
        print(f"Found target category: {target_category.name}")

    # 2. Define Mapping
    # Map old category slugs to new subcategory choices
    # Keys should match the slugs currently in your database
    slug_map = {
        'front-lit': 'front-lit',
        'back-lit': 'back-lit',
        'front-back-lit': 'front-back-lit',
        'open-face': 'open-face',
        'non-illuminated': 'non-illuminated',
        'rgb-programmable': 'rgb-programmable',
        # Add others if needed
    }

    # 3. Migrate Products
    for old_slug, new_subcat in slug_map.items():
        try:
            old_category = Category.objects.get(slug=old_slug)
            products = Product.objects.filter(category=old_category)
            
            count = products.count()
            if count > 0:
                print(f"Migrating {count} products from '{old_slug}' to '{target_category.name}' (subcategory: {new_subcat})...")
                
                # Update products
                # We iterate to save() so signals might fire if needed, or just bulk_update
                # For safety and simplicity in this script, we'll iterate
                for p in products:
                    p.category = target_category
                    p.subcategory = new_subcat
                    p.save()
                    print(f"  - Moved: {p.name}")
                
                # Optionally delete old category? 
                # User didn't explicitly ask to delete, but "规整为一个" implies cleaning up.
                # Let's keep them for now to be safe, or maybe delete if empty.
                # old_category.delete() 
                # print(f"  - Deleted old category: {old_slug}")
            else:
                print(f"No products found in '{old_slug}'.")
                
        except Category.DoesNotExist:
            print(f"Old category '{old_slug}' not found. Skipping.")

    print("--- Consolidation Complete ---")

if __name__ == '__main__':
    consolidate_products()
