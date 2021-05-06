from django import forms
from  django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class CreateUserForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = fields = ["first_name","last_name", "username","email", "groups",
        "user_permissions","is_staff","is_superuser", "is_active", "date_joined"]