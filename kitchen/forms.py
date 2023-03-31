from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from kitchen.models import Cook, Dish
from storehouse.models import Ingredient


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = Cook
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class CookChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old password",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    new_password2 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Cook
        fields = ["old_password", "new_password1", "new_password2"]


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Dish
        fields = "__all__"


class CookCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience", "first_name", "last_name"
        )


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["first_name", "last_name", "years_of_experience"]


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
