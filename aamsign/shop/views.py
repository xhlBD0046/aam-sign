from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import Category, Product, Order, OrderItem
from .cart import Cart
from django.conf import settings
import json
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def product_list_by_category(request, category_slug):
    """Display products for a specific category"""
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, available=True)
    
    context = {
        'category': category,
        'products': products
    }
    return render(request, f'illumination/{category_slug}.html', context)


def product_detail(request, id, slug):
    """Display product detail page"""
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    
    context = {
        'product': product
    }
    return render(request, 'shop/product_detail.html', context)


@require_POST
def cart_add(request, product_id):
    """Add product to cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    
    update_quantity = request.POST.get('update_quantity') == 'True'
    cart.add(product=product, quantity=quantity, update_quantity=update_quantity)
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'cart_count': len(cart),
            'message': f'{product.name} added to cart'
        })
    
    return redirect('shop:cart_detail')


@require_POST
def cart_remove(request, product_id):
    """Remove product from cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'cart_count': len(cart),
            'cart_total': cart.get_total_price()
        })
    
    return redirect('shop:cart_detail')


def cart_detail(request):
    """Display cart"""
    cart = Cart(request)
    
    context = {
        'cart': cart
    }
    return render(request, 'shop/cart_new.html', context)


def checkout(request):
    """Checkout page"""
    cart = Cart(request)
    
    if request.method == 'POST':
        #  Create order
        order = Order.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            city=request.POST['city'],
            state=request.POST['state'],
            zip_code=request.POST['zip_code'],
            total_amount=cart.get_total_price()
        )
        
        # Create order items
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        
        # Clear cart
        cart.clear()
        
        # Store order id in session for payment
        request.session['order_id'] = order.id
        
        return redirect('shop:payment')
    
    context = {
        'cart': cart
    }
    return render(request, 'shop/checkout.html', context)


def payment(request):
    """Payment page with Stripe integration"""
    order_id = request.session.get('order_id')
    if not order_id:
        return redirect('shop:checkout')
    
    order = get_object_or_404(Order, id=order_id)
    
    if request.method == 'POST':
        # Get the token from the form
        token = request.POST.get('stripeToken')
        
        if token:
            # Create the charge on Stripe's servers - this will charge the user's card
            try:
                # Charge the user's card:
                stripe.Charge.create(
                    amount=int(order.total_amount * 100), # Amount in cents
                    currency='usd',
                    description=f'Order {order.id}',
                    source=token,
                )
                
                # Mark order as paid
                order.paid = True
                order.stripe_payment_intent = token # Storing token as ref for now
                order.save()
                
                return redirect('shop:order_confirmation', order_id=order.id)
                
            except stripe.error.CardError as e:
                # The card has been declined
                pass
            except Exception as e:
                # Handle other errors
                pass
    
    context = {
        'order': order,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'shop/payment.html', context)


def create_checkout_session(request):
    """Create Stripe Checkout Session"""
    order_id = request.session.get('order_id')
    if not order_id:
        return JsonResponse({'error': 'Order not found'}, status=404)
        
    order = get_object_or_404(Order, id=order_id)
    
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(order.total_amount * 100),
                    'product_data': {
                        'name': f'Order {order.id}',
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/payment/success/'),
            cancel_url=request.build_absolute_uri('/payment/cancel/'),
            client_reference_id=str(order.id),
            metadata={
                'order_id': order.id
            }
        )
        return JsonResponse({'url': checkout_session.url})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def payment_success(request):
    """Payment success page"""
    # In a real app, you might want to verify the session here or via webhook
    # For now, we'll assume if they got here, it's good, but ideally we check session_id
    
    # Try to get order from session if available, or just show success
    order_id = request.session.get('order_id')
    if order_id:
        order = get_object_or_404(Order, id=order_id)
        order.paid = True
        order.save()
        # Clear cart
        cart = Cart(request)
        cart.clear()
        
    return render(request, 'shop/payment_success.html')


def payment_cancel(request):
    """Payment cancel page"""
    return render(request, 'shop/payment_cancel.html')


def order_confirmation(request, order_id):
    """Order confirmation page"""
    order = get_object_or_404(Order, id=order_id)
    
    context = {
        'order': order
    }
    return render(request, 'shop/order_confirmation.html', context)


@require_POST
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        
        # Fulfill the purchase...
        order_id = session.get('client_reference_id')
        if order_id:
            try:
                order = Order.objects.get(id=order_id)
                order.paid = True
                order.stripe_payment_intent = session.get('payment_intent')
                order.save()
            except Order.DoesNotExist:
                pass

    return HttpResponse(status=200)
