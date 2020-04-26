from django import forms

from .models import MyUser


user_choices = (
        ('Lawyer', 'Lawyer'),
        ('Witness', 'Witness'),
        ('Plaintiff', 'Plaintiff'),
        )

class RegistrationFrom(forms.ModelForm):
    """ registration form """
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'})) 
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    user_type = forms.ChoiceField(choices= user_choices)


    class Meta:
       model = MyUser
       fields = ['email', 'username','user_type','password']



class LoginForm(forms.Form):

    """Docstring for LoginForm. """
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'})) 
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'})) 
