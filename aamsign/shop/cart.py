# Shopping cart session management

class Cart:
    """Shopping cart using Django sessions"""
    
    def __init__(self, request):
        """Initialize the cart"""
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
    
    def add(self, product, quantity=1, update_quantity=False):
        """Add a product to the cart or update its quantity"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
    
    def save(self):
        """Save cart to session"""
        self.session.modified = True
    
    def remove(self, product):
        """Remove a product from the cart"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def __iter__(self):
        """Iterate over items in the cart and get products from the database"""
        from .models import Product
        
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    
    def __len__(self):
        """Count all items in the cart"""
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        """Calculate total cost of cart"""
        return sum(float(item['price']) * item['quantity'] 
                  for item in self.cart.values())
    
    def clear(self):
        """Remove cart from session"""
        del self.session['cart']
        self.save()
