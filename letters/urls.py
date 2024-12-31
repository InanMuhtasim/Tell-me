from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("message/", views.show_letter, name="messages"),
    path("login/", views.loginPage, name="login"),
    path("sign-up/", views.signUpPage, name="signUp"),
    path("logout/", views.logoutUser, name="logout"),
    path("user/", views.userPage, name="userPage"),
    path("confession/<str:letter_id>", views.confessionPage, name="confessionPage"),
    path("envelop/<str:letter_id>", views.envelop, name="envelop"),
    path("help/", views.helpPage, name="help"),
    path("create-confession/", views.createConfession, name="createConfession"),
    path("update-confession/<str:letter_id>", views.updateConfession, name="updateConfession"),
    path('confession/delete/<str:letter_id>/', views.deleteConfession, name='deleteConfession'),
]