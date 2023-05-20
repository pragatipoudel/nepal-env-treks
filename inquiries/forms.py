from django import forms
from captcha.fields import ReCaptchaField

from .models import Inquiry, EventAdminInquiry


class InquiryForm(forms.ModelForm):
    required_css_class = 'required'
    captcha = ReCaptchaField(label=False)

    class Meta:
        model = Inquiry
        fields = '__all__'
        labels = {
            'title': 'Trip you are interested in'
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={ 'cols': None })
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs, label_suffix='')


class EventAdminInquiryForm(forms.ModelForm):
    required_css_class = 'required'
    captcha = ReCaptchaField(label=False)

    class Meta:
        model = EventAdminInquiry
        fields = '__all__'
        labels = {
            'title': 'Trip you are interested in'
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={ 'cols': None })
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs, label_suffix='')

