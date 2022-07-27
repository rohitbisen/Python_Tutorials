from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_form),
    path('/submit_form', views.submit_form)
]
