from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    date_naissance = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'date_naissance', 'email']