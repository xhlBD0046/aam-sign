from django.contrib import admin
from .models import Category, Product, ProductImage, Order, OrderItem, Quote


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'alt_text', 'is_primary', 'order')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'available', 'created_at']
    list_filter = ['available', 'category', 'created_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]
    search_fields = ['name', 'description']
    fieldsets = (
        ('Basic Information', {
            'fields': ('category', 'name', 'slug', 'description', 'price', 'image')
        }),
        ('Specifications', {
            'fields': ('size_width', 'size_height', 'depth', 'material', 'led_type', 'power_consumption')
        }),
        ('Inventory', {
            'fields': ('stock', 'available', 'featured')
        }),
    )


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'price', 'quantity', 'get_cost')
    
    def get_cost(self, obj):
        return f"${obj.get_cost()}"
    get_cost.short_description = 'Total'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'status', 'paid', 'total_amount', 'created_at']
    list_filter = ['status', 'paid', 'created_at']
    list_editable = ['status']
    search_fields = ['email', 'first_name', 'last_name']
    inlines = [OrderItemInline]
    readonly_fields = ('stripe_payment_intent', 'created_at', 'updated_at')
    fieldsets = (
        ('Customer Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Shipping Address', {
            'fields': ('address', 'city', 'state', 'zip_code', 'country')
        }),
        ('Order Status', {
            'fields': ('status', 'paid', 'total_amount')
        }),
        ('Payment Details', {
            'fields': ('stripe_payment_intent',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'company', 'services', 'start_time', 'created_at']
    list_filter = ['start_time', 'created_at']
    search_fields = ['full_name', 'email', 'phone', 'company']
    readonly_fields = ('created_at', 'ip_address')
    fieldsets = (
        ('Contact Information', {
            'fields': ('full_name', 'email', 'phone', 'company')
        }),
        ('Project Details', {
            'fields': ('design_file', 'design_description', 'services', 'start_time')
        }),
        ('Metadata', {
            'fields': ('ip_address', 'created_at'),
            'classes': ('collapse',)
        }),
    )
