from django.shortcuts import render, redirect
from django.contrib.auth import login

from .models import Dream, Tag
from .forms import AddDreamForm


from .forms import SignUpForm
from django.urls import reverse_lazy


def frontpage(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy("login"))

    dreams = Dream.objects.filter(user=request.user)
    return render(request, "dreamapp/frontpage.html", {"dreams": dreams})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("frontpage")
    else:
        form = SignUpForm()

    return render(request, "dreamapp/signup.html", {"form": form})


def add_dreams(request):
    if request.method == "POST":
        form = AddDreamForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            commentary = form.cleaned_data["commentary"]
            is_recurring = form.cleaned_data["is_recurring"]
            category = form.cleaned_data["category"]
            mood = form.cleaned_data["mood"]
            tags = form.cleaned_data["tags"]

            user = request.user  # Assuming you have authentication in place

            dream = Dream(
                title=title,
                content=content,
                commentary=commentary,
                is_recurring=is_recurring,
                category=category,
                mood=mood,
                user=user,
            )
            dream.save()

            # Assuming tags are comma-separated strings, split and create tags
            tag_names = [tag.strip() for tag in tags.split(",")]
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                dream.tags.add(tag)

            return redirect("frontpage")
    else:
        form = AddDreamForm()

    return render(request, "dreamapp/add_dream.html", {"form": form})
