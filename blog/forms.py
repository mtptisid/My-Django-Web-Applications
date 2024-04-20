from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
     def clean_phone_number(self):
        # Optional phone number validation
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            # Perform any additional validation if needed
            # For example, check if the phone number format is valid
            pass
        return phone_number

        def clean_username(self):
        # Ignore username if it already exists
            username = self.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
             return None
            return username

        def clean_password1(self):
            password1 = self.cleaned_data.get('password1')
            if password1:
                # Validate password complexity
                password_validation.validate_password(password1, self.instance)
            return password1

        def clean(self):
            cleaned_data = super().clean()
            if 'username' not in cleaned_data:
                raise ValidationError("Username already exists.")
            return cleaned_data
        class Meta(UserCreationForm.Meta):
            model = CustomUser
            fields = ('username', 'email', 'phone_number', 'password1', 'password2')