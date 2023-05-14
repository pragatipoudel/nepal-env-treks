from typing import Any, Dict
import os
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .forms import InquiryForm


class InquirySuccessView(TemplateView):
    template_name = 'inquiries/success.html'


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
            from_email='nepalenvtrek@gmail.com',
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
            from_email='nepalenvtrek@gmail.com',
            to=[inquiry.contact_email],
        )
        confirmation_message.content_subtype = 'html'
        confirmation_message.send(fail_silently=True)

        return super().form_valid(form)
    