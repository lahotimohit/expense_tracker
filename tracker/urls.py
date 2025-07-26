from django.urls import path
from tracker import views

urlpatterns = [
    path("", views.index),
    path("delete/<uuid>", views.delete, name='delete-expense')
]
