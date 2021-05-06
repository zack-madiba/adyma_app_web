from .models import Activite,Groupe,Beneficiaire ,  Etablissement, Test, Psychosocial, Physique, Presence, Structurel
from django.forms import ModelForm
from django import forms




class BeneficiaireForm(forms.ModelForm):
    class Meta:
        model = Beneficiaire
        fields = '__all__'
        widgets = {'date_naissance' : forms.DateInput(attrs={'type':'date', 'class':'datepicker'})}
        date_naissance = forms.DateField()

class EtablissementForm(forms.ModelForm):
    class Meta:
        model = Etablissement
        fields = '__all__'


class ActiviteForm(forms.ModelForm):
    class Meta:
        model = Activite
        fields = '__all__'


class GroupeForm(forms.ModelForm):
    class Meta:
        model = Groupe
        fields = '__all__'

class GroupeChangeListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    activite = forms.ModelMultipleChoiceField(
        queryset=Activite.objects.all(), required=False)

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'

class PsychosocialForm(forms.ModelForm):
    class Meta:
        model = Psychosocial
        fields = '__all__'

class StructurelForm(forms.ModelForm):
    class Meta:
        model = Structurel
        fields = '__all__'

class PhysiqueForm(forms.ModelForm):
    class Meta:
        model = Physique
        fields = '__all__'


class PresenceForm(forms.ModelForm):
    class Meta:
        model = Presence
        fields = '__all__'