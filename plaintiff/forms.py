from django import forms
from .models import Plaintiff


class PlaintiffUpdateForm(forms.ModelForm):

    class Meta:
        model = Plaintiff
        fields = ['profile_pic','description','phone_number']