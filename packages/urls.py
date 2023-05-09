from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.PackageSearchView.as_view(), name='list'),
    path('details/<int:pk>/', views.PackageDetailsView.as_view(), name='detail')
]