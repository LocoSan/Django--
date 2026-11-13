from django.urls import path

from catalog import views

urlpatterns = [
    path("", views.catalog, name="catalog"),
    path("reset/", views.reset, name="reset"),
]
