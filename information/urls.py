from django.urls import path

from . import views

app_name = "information"

urlpatterns = [
    path('<key>/', views.InformationView.as_view(), name='information')
]