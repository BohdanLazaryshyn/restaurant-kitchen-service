from django import forms
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Cook


class DriverCreationForm(UserCreationForm):
    class Cook(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "experience",
            "first_name",
            "last_name",
        )


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username..."})
    )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."})
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."})
    )

