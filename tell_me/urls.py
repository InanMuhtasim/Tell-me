from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('bigboss-inan/', admin.site.urls),
    path("", include("letters.urls")),
]
