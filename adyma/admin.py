from django.contrib import admin
from .models import Activite, Groupe, Etablissement, Beneficiaire, Test, Presence, Physique, Structurel, Psychosocial
from django.contrib.admin.views.main import ChangeList
from adyma.forms import GroupeChangeListForm
from django import forms
from django.contrib.auth.models import Group

admin.site.site_header = "Administration Adyma"
# Register your models here.

class ActiviteAdmin(admin.ModelAdmin):
    list_display = ( "name", "descriptif", "horaire",)
    list_filter = ("name",)
admin.site.register(Activite, ActiviteAdmin)

class GroupeChangeList(ChangeList):
    def __init__(self, request, model, list_display,
        list_display_links, list_filter, date_hierarchy,
        search_fields, list_select_related, list_per_page,
        list_max_show_all, list_editable, model_admin):
        super(GroupeChangeList, self).__init__(request, model,
            list_display, list_display_links, list_filter,
            date_hierarchy, search_fields, list_select_related,
            list_per_page, list_max_show_all, list_editable, 
            model_admin)
        self.list_display = [ 'nom_groupe', 'description','activite']
        self.list_display_links = ['nom_groupe', 'description', 'activite']
        self.list_editable = ['activite']
class GroupeAdmin(admin.ModelAdmin):
    list_display = (  "nom_groupe", "description", "activite")
    def get_changelist(self, request, **kwargs):
        return GroupeChangeList

    def get_changelist_form(self, request, **kwargs):
        return GroupeChangeListForm

class BeneficiaireAdmin(admin.ModelAdmin):
    list_display = (  "prenom", "nom", "residence", "date_naissance", "Age", "phone", "groupe", "coach")
    list_filter = ("nom", "prenom")
admin.site.register(Beneficiaire, BeneficiaireAdmin)


admin.site.register(Test)
admin.site.register(Presence)
admin.site.register(Structurel)
admin.site.register(Physique)
admin.site.register(Etablissement)
admin.site.register(Psychosocial)
admin.site.register(Groupe)
