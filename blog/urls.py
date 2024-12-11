from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index),
    path("base/", views.base),
    path("about/", views.adbout),
    path("news/", views.news),
    path("banner/", views.banner),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
]