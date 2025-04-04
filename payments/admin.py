# from django.contrib import admin

# # Register your models here.
# from django.contrib import admin
# from .models import Payment

# class PaymentAdmin(admin.ModelAdmin):
#     list_display = ['user', 'transaction_id', 'total', 'confirmed', 'created_at']
#     list_filter = ['confirmed', 'created_at']
#     search_fields = ['user__username', 'transaction_id']
#     actions = ['confirm_orders']

#     def confirm_orders(self, request, queryset):
#         queryset.update(confirmed=True)
#     confirm_orders.short_description = 'Confirm selected orders'

# admin.site.register(Payment, PaymentAdmin)

# payments/admin.py

from django.contrib import admin
from .models import Payment  # Ensure the model exists and is properly imported

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'transaction_id', 'amount', 'confirmed', 'created_at')
    list_filter = ('confirmed', 'created_at')
