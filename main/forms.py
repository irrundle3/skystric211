from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CartProduct, ReviewableProduct

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class OrderForm(forms.Form):
    post = forms.IntegerField(min_value=1)

class QuantityEditForm(forms.Form):
    post = forms.IntegerField(min_value=1)

class ContactForm(forms.Form):
    email = forms.EmailField()
    message_description = forms.CharField(max_length=100)
    message_content = forms.CharField(max_length=1000)
