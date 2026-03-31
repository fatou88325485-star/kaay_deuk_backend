from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Utilisateur, Chercheur, Administrateur, Locataire,
    TypeLogement, Logement, Image, Video3D,
    Favori, Reservation, Paiement, Visite3D
)


# ===================== UTILISATEUR ADMIN =====================

@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informations personnalisées', {
            'fields': ('nom', 'telephone', 'type_utilisateur', 'date_creation')
        }),
    )
    list_display = ('username', 'email', 'nom', 'telephone', 'type_utilisateur', 'date_creation')
    list_filter = ('type_utilisateur', 'date_creation', 'is_staff')
    search_fields = ('username', 'email', 'nom', 'first_name', 'last_name')
    readonly_fields = ('date_creation',)


@admin.register(Chercheur)
class ChercheurAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informations personnalisées', {
            'fields': ('nom', 'telephone', 'date_creation')
        }),
    )
    list_display = ('username', 'email', 'nom', 'telephone', 'date_creation')
    list_filter = ('date_creation',)
    search_fields = ('username', 'email', 'nom', 'first_name', 'last_name')
    readonly_fields = ('date_creation',)


@admin.register(Administrateur)
class AdministrateurAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informations personnalisées', {
            'fields': ('nom', 'telephone', 'rib', 'date_creation')
        }),
    )
    list_display = ('username', 'email', 'nom', 'telephone', 'rib', 'date_creation')
    list_filter = ('date_creation',)
    search_fields = ('username', 'email', 'nom', 'first_name', 'last_name')
    readonly_fields = ('date_creation',)


@admin.register(Locataire)
class LocataireAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informations personnalisées', {
            'fields': ('nom', 'telephone', 'date_debut_contrat', 'caution', 'date_creation')
        }),
    )
    list_display = ('username', 'email', 'nom', 'telephone', 'date_debut_contrat', 'caution')
    list_filter = ('date_debut_contrat', 'date_creation')
    search_fields = ('username', 'email', 'nom', 'first_name', 'last_name')
    readonly_fields = ('date_creation',)


# ===================== TYPE LOGEMENT ADMIN =====================

@admin.register(TypeLogement)
class TypeLogementAdmin(admin.ModelAdmin):
    list_display = ('libelle',)
    search_fields = ('libelle',)


# ===================== LOGEMENT ADMIN =====================

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('url', 'description', 'ordre_affichage')


class Video3DInline(admin.TabularInline):
    model = Video3D
    extra = 1
    fields = ('url', 'description', 'ordre_affichage')


@admin.register(Logement)
class LogementAdmin(admin.ModelAdmin):
    inlines = [ImageInline, Video3DInline]
    list_display = ('titre', 'administrateur', 'ville', 'prix', 'disponible', 'date_creation')
    list_filter = ('disponible', 'type_logement', 'date_creation', 'ville')
    search_fields = ('titre', 'description', 'adresse', 'ville')
    fieldsets = (
        ('Informations générales', {
            'fields': ('titre', 'description', 'administrateur', 'type_logement')
        }),
        ('Localisation', {
            'fields': ('adresse', 'ville')
        }),
        ('Caractéristiques', {
            'fields': ('superficie', 'nombre_pieces', 'disponible')
        }),
        ('Tarification', {
            'fields': ('prix', 'caution')
        }),
        ('Dates', {
            'fields': ('date_creation',)
        }),
    )
    readonly_fields = ('date_creation',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'logement', 'ordre_affichage')
    list_filter = ('logement', 'ordre_affichage')
    search_fields = ('logement__titre', 'description')


@admin.register(Video3D)
class Video3DAdmin(admin.ModelAdmin):
    list_display = ('id', 'logement', 'ordre_affichage')
    list_filter = ('logement', 'ordre_affichage')
    search_fields = ('logement__titre', 'description')


# ===================== FAVORI ADMIN =====================

@admin.register(Favori)
class FavoriAdmin(admin.ModelAdmin):
    list_display = ('chercheur', 'logement', 'date_ajout')
    list_filter = ('date_ajout', 'chercheur')
    search_fields = ('chercheur__nom', 'logement__titre')
    readonly_fields = ('date_ajout',)


# ===================== RESERVATION ADMIN =====================

class PaiementInline(admin.TabularInline):
    model = Paiement
    extra = 0
    fields = ('montant', 'methode', 'statut', 'date_paiement')
    readonly_fields = ('date_creation',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    inlines = [PaiementInline]
    list_display = ('id', 'logement', 'chercheur', 'date_debut', 'date_fin', 'statut', 'montant_total')
    list_filter = ('statut', 'date_debut', 'date_reservation')
    search_fields = ('logement__titre', 'chercheur__nom')
    fieldsets = (
        ('Informations générales', {
            'fields': ('logement', 'chercheur')
        }),
        ('Dates', {
            'fields': ('date_debut', 'date_fin')
        }),
        ('Montants', {
            'fields': ('montant_total', 'acompte')
        }),
        ('Statut', {
            'fields': ('statut',)
        }),
        ('Dates de création', {
            'fields': ('date_reservation',)
        }),
    )
    readonly_fields = ('date_reservation',)


# ===================== PAIEMENT ADMIN =====================

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ('id', 'reservation', 'montant', 'methode', 'statut', 'date_paiement')
    list_filter = ('statut', 'methode', 'date_creation')
    search_fields = ('reservation__logement__titre', 'locataire__nom', 'reference_transaction')
    fieldsets = (
        ('Informations générales', {
            'fields': ('reservation', 'locataire')
        }),
        ('Montants', {
            'fields': ('montant',)
        }),
        ('Méthode de paiement', {
            'fields': ('methode', 'reference_transaction')
        }),
        ('Statut', {
            'fields': ('statut',)
        }),
        ('Dates', {
            'fields': ('date_paiement', 'date_creation')
        }),
    )
    readonly_fields = ('date_creation',)


# ===================== VISITE 3D ADMIN =====================

@admin.register(Visite3D)
class Visite3DAdmin(admin.ModelAdmin):
    list_display = ('id', 'logement', 'chercheur', 'date_visite', 'duree_visite')
    list_filter = ('date_visite', 'logement')
    search_fields = ('logement__titre', 'chercheur__nom')
    fieldsets = (
        ('Informations générales', {
            'fields': ('logement', 'chercheur')
        }),
        ('Détails de la visite', {
            'fields': ('date_visite', 'duree_visite')
        }),
    )
