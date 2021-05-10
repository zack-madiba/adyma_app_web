# Adyma : bien-vieillir. 
##### Projet turbine
## Contexte 
Adyma est une association qui intervient pour encourager la mobilité et favoriser le bien-vieillir dans les résidences autonomie, les résidences seniors et les Ehpad. Adyma s’appuie sur une méthodologie qui propose une approche globale, à la fois physique, psychologique et relationnelle. Au sein d’un établissement ou d’un territoire, l’accompagnateur Adyma formé en Activité Physique Adaptée co-construit avec les équipes gérontologiques un parcours pour accompagner les personnes vers plus de mobilité. 
Cet accompagnement comporte : 
Une phase de diagnostic, permettant la mise en place de projets individualisés de mobilité Des accompagnements individuels et collectifs, pour stimuler l’équilibre et la marche, renouer des liens 
L’organisation d’activités extérieures: sorties, balades urbaines, rencontres inter-résidences… pour réinvestir son quartier 
La formation des professionnels et aidants sur les questions de mobilité. 
https://adyma.fr/ 
## Enjeu 
Afin de pouvoir appuyer sa démarche, Adyma souhaite développer une plateforme de suivi des bénéficiaires qui permettent de tracer leur participation au programme d’accompagnement et le restituer notamment aux directeurs d’établissement. 
Un enjeu de recueil des données personnelles et du consentement à les traiter est à prévoir.

## Livrable attendu 
- Base de données + interface web optimisée responsive pour qu’une tablette puisse accéder aux formulaires Le projet accessible sur un Git. 
- La démarche du traitement des données qui a été effectuée et la modélisation de la base de données. 
- Un document plus « projet » pourra également être remis avec les choix techniques et fonctionnels effectués pour répondre au besoin.

## Appropoos de notre applicaton

### La base de données

  Notre projet fonctionne sur un système de modèle form ou nos modèles sont les tables de notre base de données. En plus de ces tables, le framework en cré deux supplémentaires (Groues & User). 
  Ce projet est constitué de deux applications : adyma et user. Cette dernière est nous sera insipensable pour le création des droits d'accès et differents comptes utilisateurs.
  
  
### L'interface

- Pour ce connecter à notre interface, il faut créer un super utilisateur depuis le terminal (  "python3 manage.py createsuperuser" ).
- Lancer le serveur à l'aide depuis le terminal  ( "python3 manage.py runserver" ) ou alors depuis la page déconexion il y'a un onglet créer un compte.
- une fois connecté, vous pouvez enregistrer un bénéficiaire et lui faire suivre des diagnostics.


#### Attention

Dans l'onglet "Vues" ne pas prrendre en compte le coutton "Compte coach",  cette fonction est encore en dévéloppement. Faites aussi attention au boutton "supprimer" car il supprime de la base de donnée l'information supprimer et toutes les informations rattachées à celle ci. Il y'a donc pas de fonction d'archivage.

##### NB : Cette application est encore en dévelloppement.
 
Merci
