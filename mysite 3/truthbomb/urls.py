from django.urls import path

from . import views

app_name = "truthbomb"
urlpatterns = [
    path("", views.index, name="index"),
    path("viewed", views.index_viewed, name="index_viewed"),
    path("<int:id>/", views.detail, name="detail"),
    path("<int:id>/submit/", views.submit, name="submit"),
    path("<int:id>/skip/", views.skip, name="skip"),
]
