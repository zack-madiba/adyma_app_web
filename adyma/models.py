from django.contrib import admin
from django.db import models
from multiselectfield import *
from django.utils import timezone
from datetime import date 
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User





# Register your models here.

oui_non = (
    ("1", 'oui'), ("0", 'non')
    )

adaptatibilité =(
        (1, "Espace bien adapté"),
        (0.5, "espace peu adapté"),
        (0, "Espace pas du tout adapté")
        )

nombre_activite =(
    (1,"4 et +"),
    (0.5, "Entre 2 et 4"),
    (0, "2 ou moins")
    )

salle_activite = (
    (1, "Salle bien adapté"),
    (0.5, "Salle peu adaptée"),
    (0, "Pas de salle réservée")
    )


materiel =(
    (1, "2 matériels ou +"),
    (0.5, "1 matériel"),
    (0, "Pas de matériel")
    )

lien = (
    (1, "2 ou +"),
    (0.5, "1"),
    (0, "0")
    )

externes = (
    (1, "4 ou +"),
    (0.5, "Quelques unes"),
    (0, "aucune")
    )

sorties = (
    (1 ,"2 et +"),
    (0.5, "1"),
    (0, "0")
    )
commerces = (
    (1, "3 et +"),
    (0.5, "1 ou 2"),
    (0, "0")
    )

parcs = (
    (1, "2 et +"),
    (0.5, "1"),
    (0,"0"),
    )

transport = (
    (1, "< 100 mètres"),
    (0.5, "Entre 250 et 500 mètres"),
    (0, "> 500 mètres")
    )




interet_projet = (
    ('équilibre','équilibre'),('marcher', 'marcher'),('sortir','sortir'),('rencontre','rencontre'),("bouger - m'entretenir", "bouger - m'entretenir"),('aucun intérêt', 'aucun intérêt')
    )

freins_mobilite = (
    ("peur de tomber", "peur de tomber"),
    ("perte de motivation lié à l'isolement","perte de motivation lié à l'isolement"),
    ("fatigabilité", "fatigabilité"),
    ("perte de sens et intérêt","perte de sens et intérêt"),
    ("aucun frein", "aucun frein"),
    ("douleurs", "douleurs"),
    )
theme_travail = (
    ("souplesse", "souplesse"),
    ("renforcement musculaire", "renforcement musculaire"),
    ("gestes quotidiens","gestes quotidiens"),
    ("remobilsation et reconditionnement", "remobilisation et reconditionnement"),
    ("enduance, gestion, effort", "endurance, gestion, effort"),
    ("gestion du stress","gestion du stress"),
    ("coordination", "coordination"),
    )
coll_ind =(
    ("individuel", "individuel"),("collectif","collectif")
    )



class Activite(models.Model):
    name = models.CharField(verbose_name="Nom de l'activité", max_length=100)
    descriptif = models.TextField(null = True, verbose_name="Description de l'activité")
    horaire = models.DateField(default=timezone.now, verbose_name="Horaire")

    class Meta:
        verbose_name="Activité"
        verbose_name="Activité"

    def __str__(self):
        return self.name

class Groupe(models.Model):
    nom_groupe = models.CharField(max_length=100)
    description = models.TextField( null=False, verbose_name="Description du groupe")
    activite = models.ManyToManyField(Activite, verbose_name="les Activités du groupe")
    DisplayFields =['beneficiaire']
    class Meta:
        verbose_name="Groupe au sein de l'établissement"
        verbose_name_plural = "Groupe au sein de l'établissement"

    def __str__(self):
        return self.nom_groupe


class Etablissement(models.Model):
    nom_etablissement = models.CharField(max_length=100, verbose_name="Nom de l'établissement")
    nom_directeur = models.CharField(max_length=100, verbose_name="Nom du directeur")
    adresse = models.CharField(max_length=100, verbose_name="Adresse")
    ville = models.CharField(max_length=50)
    descriptif = models.TextField(null = True, verbose_name="Description de l'établissement")
    groupe = models.ManyToManyField(Groupe, verbose_name="Groupe")
    class Meta:
        verbose_name="Etablissement"
        verbose_name_plural = "Etablissement"
        ordering = ["nom_etablissement"]

    def __str__(self):
        return self.nom_etablissement

class Structurel(models.Model):

    nom_etablissement =  models.ForeignKey(Etablissement, on_delete=models.CASCADE, verbose_name="Nom de l'etablissement")
    date = models.DateField(default=timezone.now, verbose_name="Date du diagnostique structurel")
    adaptat_env = models.FloatField(choices = adaptatibilité, verbose_name="Adaptabilité de l'environnement et de la structure à la mobilité (escaliers, barres d'appuis, luminosité...)")
    nbe_act = models.FloatField(choices = nombre_activite, verbose_name="Nombre d'activité (mémoire, gym, informatique...) par semaine proposées")
    salle_act = models.FloatField( choices = salle_activite, verbose_name="Salle d'activité réservée pour les activités physiques")
    materiel_act = models.FloatField(choices = materiel, verbose_name="Matériel d'activité physique (tapis,machines, espalier...)")
    lien_reg = models.FloatField(choices = lien, verbose_name="Liens réguliers avec organisation extérieure (centresocial, amicale...)")
    nbe_externes = models.FloatField(choices = externes, verbose_name="Nombre de personnes extérieures venant régulièrement dans l'établissement")
    sortie_sejour = models.FloatField(choices = sorties, verbose_name="Sorties et séjours organisés dans l'année")
    nbe_commerces =  models.FloatField(choices = commerces, verbose_name="Nombre de commerces de proximité (<250 mètres)")
    nbe_parc = models.FloatField(choices = parcs, verbose_name="Nombre de parcs à proximité (<500 mètres)")
    trans_commun = models.FloatField(choices = transport, verbose_name="Transports en commun à proximité")
    DisplayFields = ['Sommes de points', 'Alertes']

    class Meta():
        verbose_name="Diagnostic structurel établissement"

    def __str__(self):
        return self.nom_etablissement 
        


class Beneficiaire(models.Model):
    ok_nonok =(
    ('ok','ok'),('non ok','non ok')
    )
    coach = models.ForeignKey(User, models.CASCADE, null=True)
    residence = models.ForeignKey(Etablissement, null=True,on_delete=models.CASCADE, verbose_name="Résidence")
    date = models.DateTimeField(default=timezone.now, verbose_name="Date inscription")
    nom = models.CharField(null=True, max_length=100, verbose_name="Nom")
    prenom = models.CharField(null=True, max_length=100, verbose_name="Prenom")
    date_naissance = models.DateField(null=True, blank=True,verbose_name="Date de naissance")
    appartement = models.PositiveIntegerField(verbose_name="Numéro d'appartement")
    phone = PhoneNumberField(null=True, blank=False, verbose_name="Num. Tél.")
    maladie_path = models.CharField(max_length=300, verbose_name="Maladie/Pathologie")
    hospitalisation_année = models.PositiveIntegerField(verbose_name="Hospitalisation dans l'année")
    chute_annuel = models.PositiveSmallIntegerField(null= True, verbose_name="Chutes dans l'année")
    kiné = models.BooleanField(max_length=3)
    metre_outil = models.CharField(null=True, max_length=10, choices=ok_nonok, verbose_name="5 mètres – outils – levers de chaise")
    nb_activité_residence = models.PositiveIntegerField(verbose_name="nombre d'activitées dans la residence")
    nb_sorties_semaine = models.PositiveIntegerField(verbose_name="Nombre de sorties par semaine")
    durée_sortie_moy_minut = models.PositiveIntegerField(verbose_name="Durée des sorties en moyenne (en minutes)")
    sol_relevé = models.CharField(max_length=50 , choices=ok_nonok, verbose_name="Aller au sol et se relever")
    inte_proj = MultiSelectField(max_length=300, choices=interet_projet, verbose_name="Intérêt du projet")
    frein_mob = MultiSelectField(max_length=300, choices=freins_mobilite, verbose_name ="Freins à la mobilité")
    them_trav_souh =MultiSelectField(max_length=300, choices=theme_travail, verbose_name="Thème de travail souhaité")
    orientation = models.CharField(max_length=50, choices=coll_ind, verbose_name="Orientation")
    contractualisation = models.BooleanField(max_length=50, verbose_name="Contractualisation")
    comment = models.TextField(blank=True, null=True, verbose_name="Commentaire")
    groupe = models.ForeignKey(Groupe, null= True,on_delete=models.CASCADE)
    #Alertes = models.IntegerField(default=0, null=True)
    DisplayFields =['Age', 'Alertes']


    @property
    def Age(self):
        if(self.date_naissance != None):
            Age = date.today().year - self.date_naissance.year  
            return Age
    @property
    def Alertes(self):
        if(self.hospitalisation_année >= 1):
            Alertes =  1
        else:
            Alertes = "Pas d'alertes"
        return Alertes


    def __str__(self):
        return f'{self.nom} {self.prenom} Inscription faite par  {self.coach.username}'
    
    class Meta:
        verbose_name = "Entretien initial individuel"
        verbose_name_plural = "Entretien initial individuel"
        ordering=["nom", "prenom"]


class Test(models.Model):
    ok_nonok =(
    ('ok','ok'),('non ok','non ok')
    )
    coach = models.ForeignKey(User, models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date du test")
    beneficiaire = models.ForeignKey(Beneficiaire, on_delete=models.CASCADE)
    tug = models.FloatField(verbose_name="Time Up and GO", help_text='Durée en secondes')
    relev_chaise = models.PositiveIntegerField(verbose_name="Relevé de chaise par minute")
    Aller_soll = models.CharField(max_length=50 , choices=ok_nonok, verbose_name="Aller au sol")
    peri_marche = models.PositiveIntegerField(blank=True,default=0, verbose_name="Périmétrage de marche en minutes (facultatif)", help_text='durée maximale de marche estimée par la personne (durée en min / heures)')
    
    class Meta():
        verbose_name="Suivi fiche test"
        verbose_name_plural = "Suivi fiche test"

    def __str__(self):
        return f' Fiche test de {self.beneficiaire} Test passé par  {self.coach.username}' 

class Presence(models.Model):
    groupe = models.ForeignKey(Groupe, models.CASCADE, null=True, verbose_name="Groupe")
    activite =  models.ManyToManyField(Activite, verbose_name="Activité")
    date = models.DateField(default=timezone.now, verbose_name="Date de séance")
    descriptif = models.TextField( null= True, verbose_name="Description de l'activité")

    def __str__(self):
        return f'{self.nom} {self.prenom} Inscription faite par  {self.coach.username}'

class Physique(models.Model):
    Mouv =(
        (1,"Sans déséquilibre ni difficulté"),
        (0.5,"Quelques déséquilibres et/ou difficultés"),
        (0,"Déséquilibres et/ou des difficultés")
    )
    beneficiaire = models.ForeignKey(Beneficiaire, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date du diagnostic")
    lever_chaise = models.FloatField( choices=Mouv, verbose_name="Se lever d'une chaise")
    debout_immoble = models.FloatField( choices=Mouv, verbose_name="Tenir debout immobile")
    tourner_tete =models.FloatField( choices=Mouv,verbose_name="Tourner la tête à gauche et à droite")
    main_nuq =models.FloatField(choices=Mouv, verbose_name="Passer une main puis l'autre vers la nuque")
    enr_vertebral=models.FloatField( choices=Mouv,verbose_name="Enroulement_vertebral")
    marcher_droit = models.FloatField(choices=Mouv, verbose_name="Marcher en ligne droite")
    releve_pied = models.FloatField(choices=Mouv, verbose_name="Relevé du pied / hauteur du pas")
    long_pas = models.FloatField(choices=Mouv, verbose_name="Longueur du pas")
    regard_horizont = models.FloatField(choices=Mouv, verbose_name="Regerd horizontal")
    coord_bras_jamb = models.FloatField(choices=Mouv, verbose_name="Coordination bras/jambes")
    alig_vert = models.FloatField( choices=Mouv, verbose_name="Alignement vertebral")
    respiration = models.FloatField( choices=Mouv, verbose_name="Respiration")
    march_droit_yeu_fermé = models.FloatField(choices=Mouv, verbose_name="Marcher en ligne droite yeux fermés")
    marc_arriére =models.FloatField(choices=Mouv, verbose_name="Marcher en ligne droite en arrière")
    fent_jamb_droit = models.FloatField(choices=Mouv, verbose_name="Tenir 10 secondes en fente avant jambe droite")
    fent_jamb_gauche = models.FloatField(choices=Mouv, verbose_name="Tenir 10 secondes en fente avant jambe gauche")
    cap_sol_lever = models.FloatField(choices=Mouv, verbose_name="Capacité d'aller au sol et se lever")
    essouff = models.FloatField(choices=Mouv, verbose_name="essoufflement et/ou rougeur en fin de session")
    nbe_chute_ann = models.FloatField(choices=Mouv, verbose_name="Nombre de chutes dans l'année")
    depl_dehors = models.FloatField( choices=Mouv, verbose_name="Deplacement dehors au quotidien")
    DisplayFields = ['Sommes de points', 'Alertes']
    
    class Meta():
        verbose_name="Diagnostic individuel physique Résidence"

    def __str__(self):
        return f'{self.beneficiaire}'


class Psychosocial(models.Model):
    quartier = (
        (1, "oui"),
        (0.5, "un peu"),
        (0, "non")
    )
    dure_marche = (
        (1, "> 1H"),
        (0.5, "> 30 min"),
        (0, "< 30 min")
    )
    effort = (
    (1, "oui"),(0.5, "doutes"),(0, "non")
    )
    capacite = (
    (1, "oui facilement"),
    (0.5, "oui avec quelques difficultés"),
    (0, "non")
    )

    desequilibre = (
    (1, "non"), (0.5, "quelques fois"),(0, "oui")
    )
    ok_nonok =(
    (1,'ok'),(0,'non ok')
    )
    chute=(
        (1, "0"),
        (0.5, "1 à 3"),
        (0, "+ de 3")
    )
    sorti_sem =(
        (1, "3 fois ou plus"),
        (0.5, "Entre 1 et 3 fois"),
        (0, "1 ou moins")
    )

    oui_non = (
    (1, 'oui'), (0, 'non')
    )
    date_jour = models.DateTimeField(default=timezone.now, verbose_name="Date du diagnostic")
    beneficiaire = models.ForeignKey(Beneficiaire, on_delete=models.CASCADE)
    instru_marche = models.BooleanField(verbose_name="Instrument de Marche")
    duree_moy_sorti_ext = models.FloatField( choices= dure_marche, verbose_name="Durée moyenne des sorties extérieures( en minutes)") #durée en minute
    sorties_par_sem = models.FloatField(choices= sorti_sem,verbose_name="Nombre de sorties (en moyenne) par semaine")
    chute_annuel = models.FloatField(choices= chute, verbose_name="Nombre de chutes dans l'année")
    nbe_hospitali = models.FloatField(choices= chute,verbose_name="Nombre d'hospitalisation dans l'année")
    durée_marche = models.FloatField(choices= dure_marche, verbose_name="Durée de marche maximale estimée")  # en  minute
    marche_canne = models.FloatField(choices=oui_non, verbose_name="Marche avec canne ?")
    deambulateur = models.FloatField(choices=oui_non, verbose_name="Marche avec déambulteur ?")  #coder les points
    cap_sol_releve = models.FloatField(choices=capacite, verbose_name="Capacité à aller au sol et se releve")
    envie_sortir = models.FloatField(choices=effort, verbose_name="Envie de sortir et d'entretenir ma capacité à marcher/bouger")
    envie_groupe = models.FloatField(choices=effort, verbose_name="Envie de retrouver régulièrement un partenaire ou groupe pour marcher/bouger")
    desequilibre = models.FloatField(choices=desequilibre, verbose_name="Avez-vous des déséquilibres dans vos déplacements au quotidien")
    quartier = models.FloatField(choices=quartier, verbose_name="Connaissez-vous bien ce quartier")
    alimentation = models.FloatField( choices=ok_nonok)
    repos = models.FloatField(choices=ok_nonok)



    def __str__(self):
        return f'{self.beneficiaire}'
    
    class Meta:
        verbose_name = "Fiche de diagnostic psychosocial"
        verbose_name_plural = "Fiche de diagnostic psychosocial"
        ordering=["beneficiaire"]