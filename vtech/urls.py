from django.urls import path
from . import views

app_name = "vtech"

urlpatterns = [

    path('index/', views.PortListView.as_view(), name="index"),
    path("index/upload/", views.UploadPortView.as_view(), name="upload"),
    path("delete/<pk>", views.delete, name="delete"),
    path("index/create/", views.UploadBookView.as_view(), name="create"),
]