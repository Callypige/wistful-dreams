from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    path("add/", views.add_dreams, name="add-dreams"),
    path('show/<int:id>', views.show_dream, name="show-dream"),
    path("signup/", views.signup, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="dreamapp/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]
