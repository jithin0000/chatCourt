from django import forms
from .models import Judge


class JudgeUpdateForm(forms.ModelForm):

    class Meta:
        model = Judge
        fields = ['profile_pic','description','phone_number']