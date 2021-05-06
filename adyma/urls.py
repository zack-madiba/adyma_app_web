from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home, name='home'),
    path('coach/', views.coach, name ='coach'),
    path('search', views.search,  name ='search'),
    
    
    
    
    
    path('activite/', views.activite, name='activite'),
    path('presence/', views.presence, name='presence'),


    #___beneficiaires

    path('inscription/', views.entretien, name='inscription'),
    path('filtre/', views.filtre, name='filtre'),
    path('beneficiaire/', views.beneficiaire_vue, name='beneficiaire'),
    path('beneficiaire/detail/<int:pk>/', views.beneficiaire_detail, name='beneficiaire_detail'),
    path('beneficiaire/delete/<int:pk>/', views.beneficiaire_delete, name='beneficiaire_delete'),
    path('beneficiaire/update/<int:pk>/', views.beneficiaire_update, name='beneficiaire_update'),


    #___________psychosocial

    path('psychosocial/', views.psychosocial, name='psychosocial'),
    path('psychosocial_vue/', views.psychosocial_vue, name='psychosocial_vue'),
    path('psychosocial/detail/<int:id>/', views.psychosocial_detail, name='psychosocial_detail'),
    path('psychosocial/delete/<int:pk>/', views.psychosocial_delete, name='psychosocialt_delete'),
    #___________physique
    
    path('physique/', views.physique, name='physique'),
    path('physique/detail/<int:id>/', views.physique_detail, name='physique_detail'),
    path('physique/delete/<int:pk>/', views.physique_delete, name='physique_delete'),
    #path('physique/update/<int:pk>/', views.physique_update, name='physique_update'),

    #____________fiche test

    path('test/', views.test, name='test'),
    path('test/detail/<int:id>/', views.test_detail, name='test_detail'),
    path('test/delete/<int:pk>/', views.test_delete, name='test_delete'),
    path('test/update/<int:pk>/', views.test_update, name='test_update'),

    #_______etablissement
    path('etablissement/', views.etablissement, name='etablissement'),
    path('etablissement_vue/', views.etablissement_vue, name='etablissement_vue'),
    path('etablissement/detail/<int:pk>/', views.etablissement_detail, name='etablissement_detail'),
    path('etablissement/delete/<int:pk>/', views.etablissement_delete, name='etablissement_delete'),
    path('etablissement/update/<int:pk>/', views.etablissement_update, name='etablissement_update'),

    #___________groupe

    path('groupe/', views.groupe, name='groupe'),
    path('groupe_vue/', views.groupe_vue, name='groupe_vue'),
    path('groupe/delete/<int:pk>/', views.groupe_delete, name='groupe_delete'),
    path('groupe/update/<int:pk>/', views.groupe_update, name='groupe_update'),
    #__________Structurel

    path('structurel/', views.structurel, name='structurel'),


] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)