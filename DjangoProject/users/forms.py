from cProfile import label
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # 'password1' is the first password field. 'password2' is the confirmation password field.
        fields = ['first_name', 'email', 'username',  'password1', 'password2']

        labels = {
            'first_name': 'Full Name',
        }
