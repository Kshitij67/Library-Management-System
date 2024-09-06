# from django import views
from django.contrib import admin
from django.urls import include, path
import lims_app.views as views
urlpatterns = [
    path('', views.index, name='index'),
    path('addbook',views.addbook, name='addbook'),
    path('editbook/',views.editbook,name="editbook"),
    path('deletebook/',views.deletebook,name="deletebook"),
    path('details/',views.details,name="details"),
    path('users/',views.users,name="users"),
    path('register-user/',views.register_user,name="register_user"),
    path('issue/',views.issue,name="issue"),
    path('return',views.returnbook,name="return"),
]