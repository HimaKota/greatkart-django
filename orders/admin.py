from django.contrib import admin
from .models import Payment, Order, OrderProduct


# Register your models here.
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered')
    extra = 0
    
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'first_name','last_name','email','phone','order_total','status', 'is_ordered','created_at')
    list_display_links = ('order_number','first_name','last_name','email')
    list_filter = ('status','is_ordered')
    search_fields = ('order_number', 'first_name','last_name','email','phone')
    list_per_page = 25
    inlines = [OrderProductInline]

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment','user','quantity','product_price','ordered','created_at')
    list_display_links = ('order', 'payment','user')
    list_per_page = 25

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_id','payment_method','amount_paid','status','created_at')
    list_display_links = ('user', 'payment_id')
    list_per_page = 25

admin.site.register(Payment,PaymentAdmin)
admin.site.register(Order,OrderDetailsAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)