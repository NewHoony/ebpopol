from django.urls import path
from . import views

app_name ="main"

urlpatterns = [

    path("index/", views.index, name="index"),
    path('signin/', views.signin_user, name='signin'),
    path('signout/', views.signout_user, name='signout'),
    path('signup/', views.signup, name='signup'),
    path("profile/",views.profile, name ="profile"),
    path("update/",views.update, name ="update"),
    path("delete/",views.delete, name ="delete")


]