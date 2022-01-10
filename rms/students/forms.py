from django import forms
from django.contrib.admin import widgets
from .models import Archieve

class ArchieveForm(forms.ModelForm):
    class Meta:
        model = Archieve
        fields = ("row","bay","shelf","position")
