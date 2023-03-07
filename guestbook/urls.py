from django.urls import path
from . import views

app_name = "guestbook"

urlpatterns = [

    path("index/", views.index, name="index"),
    path('delete/<int:guest_id>/', views.delete_guest, name='delete_guest'),
]