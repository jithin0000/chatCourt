from django import forms
from .models import Lawyer


class LawyerUpdateForm(forms.ModelForm):

    class Meta:
        model = Lawyer
        fields = ['profile_pic','description','phone_number']