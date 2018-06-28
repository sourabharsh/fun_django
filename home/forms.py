from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models  import User

    
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=50)
    last_name = forms.CharField(label="Last Name", max_length=50)
    email = forms.EmailField(label="Email", help_text="required, provide a valid email id")

    class Meta:
        model = User 
        fields  =('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

