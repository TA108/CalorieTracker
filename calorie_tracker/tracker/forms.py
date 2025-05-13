from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FoodItem, FoodLog
from django.forms.widgets import DateInput

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ('name', 'calories', 'protein', 'carbohydrates', 'fats')

class FoodLogForm(forms.ModelForm):
    class Meta:
        model = FoodLog
        fields = ('food_item', 'date', 'quantity')
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }
