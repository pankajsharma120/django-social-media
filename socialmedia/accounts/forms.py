from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','first_name','last_name','password1',
                    'password2')
        model = get_user_model()
