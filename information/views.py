from django.shortcuts import render
from django.views import View
from .models import Information

class InformationView(View):
    def get(self, request, key):
        information = Information.objects.get(key=key)
        return render(request, 'information/details.html', {'information': information})
