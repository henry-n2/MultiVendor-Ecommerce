# from django.db import models

# # Create your models here.
# from django.db import models
# from products.models import PlacedOder, PlacedeOderItem,CustomerAddress
# from accounts.models import CustomUser

# class Payment(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     placed_order = models.ForeignKey(PlacedOder, on_delete=models.CASCADE, related_name="payments")
#     address = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE)
#     transaction_id = models.CharField(max_length=100, unique=True)
#     amount = models.FloatField()
#     payment_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')

#     def __str__(self):
#         return f"Payment {self.transaction_id} - {self.status}"


# products/models.py

# payments/models.py

from django.db import models
from django.contrib.auth import get_user_model
from products.models import PlacedOder  # Make sure this is correct!

User = get_user_model()

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(PlacedOder, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.transaction_id} - {self.user.username}"
