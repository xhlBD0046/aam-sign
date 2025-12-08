import os
import sys
import django

sys.path.insert(0, r'e:\AAC\aam-sign\aamsign')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aamsign.settings')
django.setup()

from shop.models import Category, Product
from decimal import Decimal

print("=" * 60)
print("Creating Sample Products for All Categories")
print("=" * 60)

# Define all products for each category
products_by_category = {
    'back-lit': [
        {
            'name': 'Premium Halo-Lit Office Logo',
            'slug': 'premium-halo-lit-office-logo',
            'description': 'Elegant halo-lit signage perfect for corporate environments. Creates a sophisticated glow effect on the wall.',
            'price': Decimal('599.00'),
            'size_width': Decimal('60.00'),
            'size_height': Decimal('24.00'),
            'depth': Decimal('2.00'),
            'material': 'Brushed Aluminum',
            'led_type': 'LED Strip',
            'power_consumption': '40W',
            'stock': 10,
            'available': True,
        },
        {
            'name': 'Boutique Back-Lit Sign',
            'slug': 'boutique-back-lit-sign',
            'description': 'Sophisticated back-lit signage for upscale retail spaces. Premium quality with elegant halo effect.',
            'price': Decimal('549.00'),
            'size_width': Decimal('48.00'),
            'size_height': Decimal('18.00'),
            'depth': Decimal('2.00'),
            'material': 'Stainless Steel',
            'led_type': 'LED Strip',
            'power_consumption': '35W',
            'stock': 8,
            'available': True,
        },
        {
            'name': 'Executive Halo Letters',
            'slug': 'executive-halo-letters',
            'description': 'Premium executive-grade back-lit channel letters with superior craftsmanship.',
            'price': Decimal('749.00'),
            'size_width': Decimal('72.00'),
            'size_height': Decimal('30.00'),
            'depth': Decimal('2.50'),
            'material': 'Brushed Aluminum',
            'led_type': 'High-Efficiency LED',
            'power_consumption': '50W',
            'stock': 5,
            'available': True,
        },
    ],
    'front-back-lit': [
        {
            'name': 'Dual-Lit Storefront Sign',
            'slug': 'dual-lit-storefront-sign',
            'description': 'Maximum visibility with both front and back illumination. Perfect for high-traffic areas.',
            'price': Decimal('799.00'),
            'size_width': Decimal('72.00'),
            'size_height': Decimal('36.00'),
            'depth': Decimal('3.00'),
            'material': 'Acrylic & Aluminum',
            'led_type': 'Dual LED Modules',
            'power_consumption': '80W',
            'stock': 5,
            'available': True,
        },
        {
            'name': 'Premium Dual Illumination Letters',
            'slug': 'premium-dual-illumination-letters',
            'description': 'Top-of-the-line channel letters with front and back lighting for maximum impact.',
            'price': Decimal('899.00'),
            'size_width': Decimal('84.00'),
            'size_height': Decimal('42.00'),
            'depth': Decimal('3.50'),
            'material': 'Aluminum & Acrylic',
            'led_type': 'LED Modules Front + LED Strip Back',
            'power_consumption': '95W',
            'stock': 3,
            'available': True,
        },
    ],
    'open-face': [
        {
            'name': 'Vintage Marquee Bar Sign',
            'slug': 'vintage-marquee-bar-sign',
            'description': 'Classic open-face channel letters with exposed bulbs for a retro look. Perfect for bars and restaurants.',
            'price': Decimal('450.00'),
            'size_width': Decimal('36.00'),
            'size_height': Decimal('12.00'),
            'depth': Decimal('4.00'),
            'material': 'Rusted Metal Finish',
            'led_type': 'E14 Bulbs',
            'power_consumption': '100W',
            'stock': 3,
            'available': True,
        },
        {
            'name': 'Retro Diner Marquee Letters',
            'slug': 'retro-diner-marquee-letters',
            'description': 'Authentic vintage-style marquee letters with exposed Edison bulbs. Creates a warm, nostalgic atmosphere.',
            'price': Decimal('525.00'),
            'size_width': Decimal('48.00'),
            'size_height': Decimal('18.00'),
            'depth': Decimal('4.50'),
            'material': 'Powder-Coated Steel',
            'led_type': 'Edison Bulbs',
            'power_consumption': '120W',
            'stock': 4,
            'available': True,
        },
        {
            'name': 'Theater Marquee Sign',
            'slug': 'theater-marquee-sign',
            'description': 'Grand theater-style marquee signage with classic bulb illumination.',
            'price': Decimal('675.00'),
            'size_width': Decimal('60.00'),
            'size_height': Decimal('24.00'),
            'depth': Decimal('5.00'),
            'material': 'Metal Frame',
            'led_type': 'C9 Bulbs',
            'power_consumption': '150W',
            'stock': 2,
            'available': True,
        },
    ],
    'non-illuminated': [
        {
            'name': 'Brushed Steel Lobby Sign',
            'slug': 'brushed-steel-lobby-sign',
            'description': 'Professional non-illuminated 3D letters for office lobbies. Clean and modern aesthetic.',
            'price': Decimal('299.00'),
            'size_width': Decimal('48.00'),
            'size_height': Decimal('12.00'),
            'depth': Decimal('1.00'),
            'material': 'Stainless Steel',
            'led_type': 'None',
            'power_consumption': '0W',
            'stock': 15,
            'available': True,
        },
        {
            'name': 'Acrylic 3D Office Letters',
            'slug': 'acrylic-3d-office-letters',
            'description': 'High-quality acrylic dimensional letters. Perfect for reception areas and conference rooms.',
            'price': Decimal('249.00'),
            'size_width': Decimal('36.00'),
            'size_height': Decimal('10.00'),
            'depth': Decimal('0.75'),
            'material': 'Acrylic',
            'led_type': 'None',
            'power_consumption': '0W',
            'stock': 20,
            'available': True,
        },
        {
            'name': 'Premium Metal Logo Letters',
            'slug': 'premium-metal-logo-letters',
            'description': 'Luxury metal 3D letters with brushed finish. Ideal for corporate branding.',
            'price': Decimal('399.00'),
            'size_width': Decimal('60.00'),
            'size_height': Decimal('18.00'),
            'depth': Decimal('1.50'),
            'material': 'Brushed Aluminum',
            'led_type': 'None',
            'power_consumption': '0W',
            'stock': 12,
            'available': True,
        },
    ],
    'rgb-programmable': [
        {
            'name': 'Dynamic RGB Event Sign',
            'slug': 'dynamic-rgb-event-sign',
            'description': 'Programmable RGB sign with app control for dynamic color changing effects. Perfect for entertainment venues.',
            'price': Decimal('899.00'),
            'size_width': Decimal('60.00'),
            'size_height': Decimal('30.00'),
            'depth': Decimal('2.50'),
            'material': 'Acrylic & Aluminum',
            'led_type': 'Smart RGB Pixels',
            'power_consumption': '75W',
            'stock': 4,
            'available': True,
        },
        {
            'name': 'Programmable Nightclub Sign',
            'slug': 'programmable-nightclub-sign',
            'description': 'Full-color RGB channel letters with wireless control. Create stunning light shows and effects.',
            'price': Decimal('1099.00'),
            'size_width': Decimal('84.00'),
            'size_height': Decimal('36.00'),
            'depth': Decimal('3.00'),
            'material': 'Aluminum Housing',
            'led_type': 'Addressable RGB LEDs',
            'power_consumption': '100W',
            'stock': 2,
            'available': True,
        },
        {
            'name': 'Smart Color-Changing Letters',
            'slug': 'smart-color-changing-letters',
            'description': 'WiFi-enabled RGB programmable letters. Control colors, patterns, and effects from your smartphone.',
            'price': Decimal('799.00'),
            'size_width': Decimal('48.00'),
            'size_height': Decimal('24.00'),
            'depth': Decimal('2.00'),
            'material': 'Acrylic',
            'led_type': 'RGB LED Modules',
            'power_consumption': '60W',
            'stock': 6,
            'available': True,
        },
    ],
}

# Create or update products for each category
total_created = 0
total_updated = 0

for category_slug, products_data in products_by_category.items():
    try:
        category = Category.objects.get(slug=category_slug)
        print(f"\n{category.name} ({category_slug}):")
        
        for product_data in products_data:
            product, created = Product.objects.update_or_create(
                slug=product_data['slug'],
                defaults={**product_data, 'category': category}
            )
            
            if created:
                print(f"  ✅ Created: {product.name}")
                total_created += 1
            else:
                print(f"  🔄 Updated: {product.name}")
                total_updated += 1
                
    except Category.DoesNotExist:
        print(f"\n⚠️  Category '{category_slug}' not found - skipping")

print("\n" + "=" * 60)
print(f"Summary: Created {total_created} products, Updated {total_updated} products")
print("=" * 60)

# Show final product counts
print("\nFinal Product Distribution:")
categories = Category.objects.all().order_by('slug')
for category in categories:
    count = Product.objects.filter(category=category, available=True).count()
    print(f"  {category.name}: {count} products")

print("\n✅ Done! All categories now have products.")
