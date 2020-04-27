from django import forms
from .models import Witness


class WitnessUpdateForm(forms.ModelForm):

    class Meta:
        model = Witness
        fields = ['profile_pic','description','phone_number']