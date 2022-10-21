from django.contrib import admin
from .models import Product ,Variation,TaxCount

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

class TaxCountAdmin(admin.ModelAdmin):
    list_display = ('tax_percentage',)
    def has_add_permission(self, request):
    # if there's already an entry, do not allow adding
        count = TaxCount.objects.all().count()
        if count == 0:
            return True
        return False
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(TaxCount,TaxCountAdmin)