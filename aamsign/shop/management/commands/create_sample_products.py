from django.core.management.base import BaseCommand
from shop.models import Category, Product, ProductImage
from decimal import Decimal


class Command(BaseCommand):
    help = 'Create sample product data for testing'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample product data...')

        # Create categories
        categories_data = [
            {'name': 'Front-Lit', 'slug': 'front-lit', 'description': 'Bright, bold, and visible channel letters'},
            {'name': 'Back-Lit', 'slug': 'back-lit', 'description': 'Sophisticated halo-lit signs'},
            {'name': 'Front + Back-Lit', 'slug': 'front-back-lit', 'description': 'Double illumination impact'},
            {'name': 'Open-Face', 'slug': 'open-face', 'description': 'Vintage marquee style signs'},
            {'name': 'Non-Illuminated', 'slug': 'non-illuminated', 'description': 'Professional 3D letters'},
            {'name': 'RGB Programmable', 'slug': 'rgb-programmable', 'description': 'Dynamic color-changing signs'},
        ]

        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Sample products for Front-Lit category
        front_lit_category = Category.objects.get(slug='front-lit')
        
        products_data = [
            {
                'category': front_lit_category,
                'name': 'Custom LED Neon Sign "Customize"',
                'slug': 'custom-led-neon-customize',
                'description': 'Customizable neon sign with vibrant LED lighting. Perfect for businesses, events, and home decor.',
                'price': Decimal('299.00'),
                'size_width': Decimal('36.00'),
                'size_height': Decimal('18.00'),
                'depth': Decimal('1.50'),
                'material': 'Aluminum & Acrylic',
                'led_type': 'LED Modules',
                'power_consumption': '50W',
                'stock': 15,
                'available': True,
                'featured': True,
            },
            {
                'category': front_lit_category,
                'name': '"THE WORLD IS YOURS" Neon Sign',
                'slug': 'the-world-is-yours-neon',
                'description': 'Inspirational neon sign with bright white illumination. Great for offices and studios.',
                'price': Decimal('349.00'),
                'size_width': Decimal('48.00'),
                'size_height': Decimal('24.00'),
                'depth': Decimal('1.50'),
                'material': 'Aluminum & Acrylic',
                'led_type': 'LED Modules',
                'power_consumption': '60W',
                'stock': 20,
                'available': True,
                'featured': False,
            },
            {
                'category': front_lit_category,
                'name': '"THIS MUST BE THE PLACE" Neon Sign',
                'slug': 'this-must-be-place-neon',
                'description': 'Vibrant pink neon sign perfect for cafes, boutiques, and Instagram-worthy spaces.',
                'price': Decimal('399.00'),
                'size_width': Decimal('40.00'),
                'size_height': Decimal('28.00'),
                'depth': Decimal('1.50'),
                'material': 'Aluminum & Acrylic',
                'led_type': 'RGB LED',
                'power_consumption': '55W',
                'stock': 12,
                'available': True,
                'featured': True,
            },
            {
                'category': front_lit_category,
                'name': 'Nu99ty Neon Sign Pink',
                'slug': 'nu99ty-neon-pink',
                'description': 'Stylish barcode-style neon sign with pink and blue accent lighting.',
                'price': Decimal('329.00'),
                'size_width': Decimal('32.00'),
                'size_height': Decimal('20.00'),
                'depth': Decimal('1.50'),
                'material': 'Aluminum & Acrylic',
                'led_type': 'LED Modules',
                'power_consumption': '45W',
                'stock': 18,
                'available': True,
                'featured': False,
            },
        ]

        for product_data in products_data:
            product, created = Product.objects.update_or_create(
                slug=product_data['slug'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        # Add more products for other categories
        back_lit_category = Category.objects.get(slug='back-lit')
        back_lit_products = [
            {
                'category': back_lit_category,
                'name': 'Halo-Lit Office Logo',
                'slug': 'halo-lit-office-logo',
                'description': 'Elegant halo-lit signage perfect for corporate environments.',
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
                'category': back_lit_category,
                'name': 'Boutique Back-Lit Sign',
                'slug': 'boutique-back-lit-sign',
                'description': 'Sophisticated back-lit signage for upscale retail spaces.',
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
        ]

        for product_data in back_lit_products:
            product, created = Product.objects.update_or_create(
                slug=product_data['slug'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        # Front + Back-Lit Products
        front_back_lit_category = Category.objects.get(slug='front-back-lit')
        front_back_lit_products = [
            {
                'category': front_back_lit_category,
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
            },
        ]

        for product_data in front_back_lit_products:
            product, created = Product.objects.update_or_create(
                slug=product_data['slug'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        # Open-Face Products
        open_face_category = Category.objects.get(slug='open-face')
        open_face_products = [
            {
                'category': open_face_category,
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
            },
        ]

        for product_data in open_face_products:
            product, created = Product.objects.update_or_create(
                slug=product_data['slug'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        # Non-Illuminated Products
        non_illuminated_category = Category.objects.get(slug='non-illuminated')
        non_illuminated_products = [
            {
                'category': non_illuminated_category,
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
            },
        ]

        for product_data in non_illuminated_products:
            product, created = Product.objects.update_or_create(
                slug=product_data['slug'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        # RGB Programmable Products
        rgb_category = Category.objects.get(slug='rgb-programmable')
        rgb_products = [
            {
                'category': rgb_category,
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
            },
        ]

        for product_data in rgb_products:
            product, created = Product.objects.update_or_create(
                slug=product_data['slug'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
