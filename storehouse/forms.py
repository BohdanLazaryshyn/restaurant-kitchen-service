from django import forms
from .models import Ingredient


class IngredientSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."})
    )


class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ['name']
