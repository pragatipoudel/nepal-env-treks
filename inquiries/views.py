import os
from typing import Any, Optional
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from packages.models import SpecialEvent
from .forms import InquiryForm, EventAdminInquiryForm


class InquirySuccessView(TemplateView):
    template_name = 'inquiries/success.html'


class EventInquirySuccessView(TemplateView):
    template_name = 'inquiries/success_event.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['event'] = SpecialEvent.objects.get(slug=self.kwargs['slug'])
        return context_data


class InquiryFormView(FormView):
    template_name = 'inquiries/inquiry.html'
    form_class = InquiryForm

    def get_initial(self):
        initial = super().get_initial()

        title = self.request.GET.get('title')
        if title:
            initial['title'] = title
        
        return initial

    def get_success_url(self):
        return reverse('inquiries:success')
    
    def form_valid(self, form):
        inquiry = form.save()

        html_message = render_to_string('inquiries/email_to_business.html', {
            'inquiry': inquiry
        })

        request_message = EmailMessage(
            f'New booking request for {inquiry.title}',
            body=html_message,
            from_email=inquiry.contact_email,
            to=[os.environ['EMAIL_BUSINESS']],
        )
        request_message.content_subtype = 'html'
        request_message.send(fail_silently=True)

        html_message = render_to_string('inquiries/email_to_customer.html', {
            'inquiry': inquiry
        })

        confirmation_message = EmailMessage(
            f'Booking confirmation for {inquiry.title}',
            body=html_message,
            from_email=os.environ['EMAIL_BUSINESS'],
            to=[inquiry.contact_email],
        )
        confirmation_message.content_subtype = 'html'
        confirmation_message.send(fail_silently=True)

        return super().form_valid(form)
    

class EventAdminInquiryFormView(LoginRequiredMixin, FormView):
    template_name = 'inquiries/inquiry.html'
    form_class = EventAdminInquiryForm
    raise_exception = True

    def get_initial(self):
        initial = super().get_initial()

        title = self.request.GET.get('title')
        if title:
            initial['title'] = title
        
        return initial
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['event'] = SpecialEvent.objects.get(slug=self.kwargs['slug'])
        return context_data

    def get_success_url(self):
        event_slug = self.kwargs['slug']
        return reverse('inquiries:event-success', kwargs={'slug': event_slug})
    
    def form_valid(self, form):
        inquiry = form.save()

        event = SpecialEvent.objects.get(slug=self.kwargs['slug'])

        html_message = render_to_string('inquiries/email_to_business_event.html', {
            'inquiry': inquiry,
            'event': event
        })

        request_message = EmailMessage(
            f'New booking request for {inquiry.title}',
            body=html_message,
            from_email=inquiry.contact_email,
            to=[os.environ['EMAIL_BUSINESS']],
        )
        request_message.content_subtype = 'html'
        request_message.send(fail_silently=True)

        html_message = render_to_string('inquiries/email_to_customer_event.html', {
            'inquiry': inquiry,
            'event': event
        })

        confirmation_message = EmailMessage(
            f'Booking confirmation for {inquiry.title}',
            body=html_message,
            from_email=os.environ['EMAIL_BUSINESS'],
            to=[inquiry.contact_email],
        )
        confirmation_message.content_subtype = 'html'
        confirmation_message.send(fail_silently=True)

        return super().form_valid(form)
    

class EventBookingView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        event = SpecialEvent.objects.filter(is_active=True).first()
        if not event:
            return '/'
        return reverse('inquiries:event-admin-inquiry', kwargs={'slug': event.slug})