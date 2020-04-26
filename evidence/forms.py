from django import forms
from .models import Evidence

class EvidenceForm(forms.ModelForm):
    """ form for uploading evidence """

    class Meta:
        model = Evidence
        fields ="__all__"