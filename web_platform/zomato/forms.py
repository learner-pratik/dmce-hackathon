from django import forms

from .models import login,Orders,Posts


class loginform(forms.ModelForm):
    class Meta:
        model = login
        exclude=()

class orderform(forms.ModelForm):
    class Meta:
        model = Orders
        exclude=()

class postform(forms.ModelForm):
    class Meta:
        model = Posts
        exclude=()