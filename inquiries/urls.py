from django.urls import path
from . import views


app_name = 'inquiries'
urlpatterns = [
    path('inquiry/', views.InquiryFormView.as_view(), name='inquiry'),
    path('success/', views.InquirySuccessView.as_view(), name='success'),
    path('event-booking/', views.EventBookingView.as_view(), name='event-booking'),
    path('<str:slug>/', views.EventAdminInquiryFormView.as_view(), name='event-admin-inquiry'),
    path('<str:slug>/event-success/', views.EventInquirySuccessView.as_view(), name='event-success'),
]