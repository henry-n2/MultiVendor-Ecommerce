from django.urls import path
from . import views
app_name = 'payments'

urlpatterns = [
    path('payment-details/',views.display_payment_details, name='display_payment_details'),
    path('create-payment-intent/', views.create_checkout_session, name='strip_checkout'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('download-bill/', views.download_bill, name='download_bill'),
    # path('payment-details/', views.display_payment_details, name='payment_details'),
    path('process/', views.process_payment, name='process_payment'),
]
