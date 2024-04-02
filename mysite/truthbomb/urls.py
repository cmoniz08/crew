from django.urls import path

from . import views

app_name = "truthbomb"
urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("viewed", views.index_viewed, name="index_viewed"),
    path("<int:id>/", views.detail, name="detail"),
    path("home/submit_topic/<int:id>/", views.detailtopics, name="detailtopics"),
    path("<int:id>/submit/", views.submit, name="submit"),
    path("<int:id>/skip/", views.skip, name="skip"),
    path("home/submit_topic/", views.submit_topic, name="submit_topic"),
    path("home/submit_initials/", views.submit_initials, name="submit_initials"),
    path("<int:id>/submit_topic/", views.submit_topic, name="submit"),
    path("<int:id>/skip_topic/", views.skip_topic, name="skip_topic"),


]
