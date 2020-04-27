from django import forms
from .models import Evidence

class EvidenceForCase(forms.ModelForm):
    """ form for uploading evidence """

    class Meta:
        model = Evidence
        fields =['name','content']


class EvidenceCreateForm(forms.ModelForm):
    """ form for uploading evidence """

    class Meta:
        model = Evidence
        fields = ['case','name', 'content']


