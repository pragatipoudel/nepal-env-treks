from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from captcha.fields import ReCaptchaField

from .models import Inquiry


class InquiryForm(forms.ModelForm):
    required_css_class = 'required'
    captcha = ReCaptchaField(label=False)

    class Meta:
        model = Inquiry
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={ 'cols': None })
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs, label_suffix='')

