from django.shortcuts import render


def frontpage(request):
    return render(request, "dreamapp/frontpage.html")
