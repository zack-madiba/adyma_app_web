import django_filters 
from .models import *


class BeneficiaireFilter(django_filters.FilterSet):
    class Meta:
        model = Beneficiaire
        fields = ['residence','orientation']
         