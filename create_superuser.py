# create_superuser.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

email = 'henry-n2@outlook.com'
password = 'Boss@1234Eco'

if not User.objects.filter(email=email).exists():
    user = User.objects.create_superuser(
        email=email,
        password=password,
        first_name='Ujjal',
        last_name='Bhattacharya',
        mobile='8250'  # change this field name if it's different
    )
    print("Superuser created successfully!")
else:
    print("Superuser already exists.")
