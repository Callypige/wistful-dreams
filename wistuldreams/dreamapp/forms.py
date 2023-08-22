from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Dream, CATEGORY_CHOICES, MOOD_CHOICES
from django import forms
from tempus_dominus.widgets import DateTimePicker


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
            "date",
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

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full border rounded-lg px-3 py-2",
            }
        )
    )

    date = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                "useCurrent": True,
                "collapse": False,
                "format": "YYYY-MM-DD",
            },
            attrs={
                "class": "w-full border rounded-lg px-3 py-2",
                "append": "fa fa-calendar",
                "icon_toggle": True,
            },
        ),
    )
