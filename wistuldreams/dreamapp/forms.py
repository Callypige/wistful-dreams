from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Dream, CATEGORY_CHOICES, MOOD_CHOICES
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class AddDreamForm(forms.ModelForm):
    class Meta:
        model = Dream
        fields = [
            "title",
            "content",
            "commentary",
            "is_recurring",
            "category",
            "mood",
            "tags",
        ]

    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={"class": "w-full border rounded-lg px-3 py-2"}),
    )
    mood = forms.ChoiceField(
        choices=MOOD_CHOICES,
        widget=forms.Select(attrs={"class": "w-full border rounded-lg px-3 py-2"}),
    )
    tags = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full border rounded-lg px-3 py-2",
                "placeholder": "Tag1, Tag2, ...",
            }
        )
    )
