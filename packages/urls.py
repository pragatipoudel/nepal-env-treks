from django.urls import path

from . import views

app_name = "packages"
urlpatterns = [
    path('search/', views.PackageSearchView.as_view(), name='search'),
    path('details/<int:pk>/', views.PackageDetailsView.as_view(), name='detail')
]