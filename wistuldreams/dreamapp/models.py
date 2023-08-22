from django.db import models
from django.contrib.auth.models import User
import datetime


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


CATEGORY_CHOICES = (
    ("normal", "Normal"),
    ("lucid", "Lucide"),
    ("nightmare", "Cauchemar"),
)

MOOD_CHOICES = (
    ("horrible", "Horrible"),
    ("unpleasant", "Désagréable"),
    ("nothing_special", "Rien de spécial"),
    ("rather_nice", "Plutôt sympatique"),
    ("nice", "Sympa"),
    ("incredible", "Incroyable"),
)


class Dream(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=300)
    commentary = models.TextField(max_length=150)
    is_recurring = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.datetime.now)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
