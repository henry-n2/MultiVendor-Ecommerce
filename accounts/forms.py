# # from django import forms
# # from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# # from django.contrib.auth import get_user_model
# # from . models import CustomUser

# # class RegistrationForm(UserCreationForm):

# #     class Meta:
# #         model = CustomUser
# #         fields = ('email','first_name', 'last_name','mobile', 'password1', 'password2')  # Add any other fields you want to include in the registration form



# # class CustomUserEditForm(forms.ModelForm):
# #     class Meta:
# #         model = CustomUser
# #         fields = ['email', 'first_name', 'last_name', 'mobile']
# #         widgets = {
# #             'first_name': forms.TextInput(attrs={'class':'form-control'}),
# #             'last_name': forms.TextInput(attrs={'class':'form-control'}),
# #             'mobile': forms.NumberInput(attrs={'class':'form-control'}),
# #             'email':forms.EmailInput(attrs={'class':'form-control'}),
# #         } 


# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import get_user_model
# from .models import CustomUser

# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'first_name', 'last_name', 'mobile', 'password1', 'password2')
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }

# class VendorRegistrationForm(UserCreationForm):
#     trade_license_number = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     gst_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'first_name', 'last_name', 'mobile', 'trade_license_number', 'gst_number', 'password1', 'password2')
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
#             'trade_license_number': forms.TextInput(attrs={'class': 'form-control'}),
#             'gst_number': forms.TextInput(attrs={'class': 'form-control'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }

# class CustomUserEditForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'first_name', 'last_name', 'mobile']
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#         }


# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import get_user_model
# from .models import CustomUser

# class RegistrationForm(UserCreationForm):
#     # New fields
#     profile_picture = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
#     customer_type = forms.ChoiceField(
#         choices=[('Personal', 'Personal'), ('Corporate', 'Corporate')],
#         required=True,
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'first_name', 'last_name', 'mobile', 'profile_picture', 'customer_type', 'password1', 'password2')
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }

# class VendorRegistrationForm(UserCreationForm):
#     trade_license_number = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     gst_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     profile_picture = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
#     # customer_type = forms.ChoiceField(
#     #     choices=[('Personal', 'Personal'), ('Corporate', 'Corporate')],
#     #     required=True,
#     #     widget=forms.Select(attrs={'class': 'form-control'})
#     # )

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'first_name', 'last_name', 'mobile', 'trade_license_number', 'gst_number', 'profile_picture', 'customer_type', 'password1', 'password2')
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
#             'trade_license_number': forms.TextInput(attrs={'class': 'form-control'}),
#             'gst_number': forms.TextInput(attrs={'class': 'form-control'}),
#             'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
#             'customer_type': forms.Select(attrs={'class': 'form-control'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }

# class CustomUserEditForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'first_name', 'last_name', 'mobile', 'profile_picture', 'customer_type']
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
#             'customer_type': forms.Select(attrs={'class': 'form-control'})
#         }


# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import get_user_model
# from .models import CustomUser

# class RegistrationForm(UserCreationForm):
#     # New fields
#     profile_picture = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
#     customer_type = forms.ChoiceField(
#         choices=[('Personal', 'Personal'), ('Corporate', 'Corporate')],
#         required=True,
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'first_name', 'last_name', 'mobile', 'profile_picture', 'customer_type', 'password1', 'password2')
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }

# class VendorRegistrationForm(UserCreationForm):
#     trade_license_number = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     gst_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     profile_picture = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'first_name', 'last_name', 'mobile', 'trade_license_number', 'gst_number', 'profile_picture', 'password1', 'password2')
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
#             'trade_license_number': forms.TextInput(attrs={'class': 'form-control'}),
#             'gst_number': forms.TextInput(attrs={'class': 'form-control'}),
#             'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }

# class CustomUserEditForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'first_name', 'last_name', 'mobile', 'profile_picture']  # Removed 'customer_type'
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'})
#         }



from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    # New fields
    profile_picture = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    customer_type = forms.ChoiceField(
        choices=[('Personal', 'Personal'), ('Corporate', 'Corporate')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'mobile', 'profile_picture', 'customer_type' , 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
# 'customer_type',
class VendorRegistrationForm(UserCreationForm):
    trade_license_number = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gst_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    profile_picture = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'mobile', 'trade_license_number', 'gst_number', 'profile_picture', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'trade_license_number': forms.TextInput(attrs={'class': 'form-control'}),
            'gst_number': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'mobile', 'profile_picture']  # Removed 'customer_type'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
