from django import forms
from .models import User, Besoins

class UserCreationForm(forms.ModelForm):

    password = forms.CharField(label="Mot de passe", max_length=254, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))
    password1 = forms.CharField(label="Confirmer le mot de passe", max_length=254, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmer votre mot de passe'}))

    
    class Meta:
        model = User
        fields = ("username", "email", 'phone', 'password', 'password1', 'news',)
        widgets = {
            'username': forms.TextInput(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Nom utilisateur'
					}
				),
            'email': forms.TextInput(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Votre mail'
					}
				),
            'phone': forms.TextInput(
				attrs={
					'class': 'form-control',
                    'placeholder': 'Votre contact'
					}
				),
            'news': forms.CheckboxInput(
				attrs={
					'class': 'form-check-input'
					}
				),
            
			}

class BesoinForm(forms.ModelForm):
    
    class Meta:
        model = Besoins
        fields = ("__all__")
       

            