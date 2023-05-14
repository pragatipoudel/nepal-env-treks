from django.urls import path
from . import views


app_name = 'inquiries'
urlpatterns = [
    path('inquiry/', views.InquiryFormView.as_view(), name='inquiry'),
    path('success/', views.InquirySuccessView.as_view(), name='success')
]