from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime


# ===================== UTILISATEUR HIERARCHY =====================

class Utilisateur(AbstractUser):
    """Classe de base pour tous les utilisateurs du système"""
    nom = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    type_utilisateur = models.CharField(max_length=30, default="chercheur")
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
    
    def inscrire(self):
        """Enregistrer un nouveau utilisateur"""
        self.save()
    
    def connecter(self):
        """Connecter l'utilisateur"""
        pass
    
    def modifier_profil(self):
        """Modifier le profil de l'utilisateur"""
        self.save()
    
    def __str__(self):
        return f"{self.nom or self.get_full_name()}"


class Chercheur(Utilisateur):
    """Utilisateur qui cherche un logement"""
    
    class Meta:
        verbose_name = "Chercheur"
        verbose_name_plural = "Chercheurs"
    
    def rechercher_logement(self):
        """Rechercher un logement"""
        return Logement.objects.filter(disponible=True)
    
    def ajouter_favori(self, logement):
        """Ajouter un logement aux favoris"""
        return Favori.objects.create(logement=logement, chercheur=self)
    
    def reserver(self, logement, date_debut, date_fin):
        """Réserver un logement"""
        return Reservation.objects.create(
            logement=logement,
            chercheur=self,
            date_debut=date_debut,
            date_fin=date_fin
        )
    
    def lancer_visite_3d(self, logement):
        """Lancer une visite 3D"""
        return Visite3D.objects.create(logement=logement, chercheur=self)
    
    def __str__(self):
        return f"Chercheur: {self.nom or self.get_full_name()}"


class Administrateur(Utilisateur):
    """Administrateur qui gère les logements"""
    rib = models.CharField(max_length=50, blank=True)
    
    class Meta:
        verbose_name = "Administrateur"
        verbose_name_plural = "Administrateurs"
    
    def publier_logement(self, titre, description, prix):
        """Publier un nouveau logement"""
        return Logement.objects.create(
            administrateur=self,
            titre=titre,
            description=description,
            prix=prix
        )
    
    def modifier_logement(self, logement):
        """Modifier un logement"""
        logement.save()
    
    def valider_reservation(self, reservation):
        """Valider une réservation"""
        reservation.statut = "confirmée"
        reservation.save()
    
    def gerer_utilisateurs(self):
        """Gérer les utilisateurs"""
        return Utilisateur.objects.all()
    
    def __str__(self):
        return f"Admin: {self.nom or self.get_full_name()}"


class Locataire(Chercheur):
    """Utilisateur qui loue un logement"""
    date_debut_contrat = models.DateField(null=True, blank=True)
    caution = models.FloatField(default=0.0)
    
    class Meta:
        verbose_name = "Locataire"
        verbose_name_plural = "Locataires"
    
    def payer_loyer(self, montant, methode="virement"):
        """Payer le loyer"""
        # Implement payment logic
        pass
    
    def demander_quittance(self):
        """Demander une quittance"""
        # Implement quittance generation
        pass
    
    def __str__(self):
        return f"Locataire: {self.nom or self.get_full_name()}"


# ===================== TYPE LOGEMENT =====================

class TypeLogement(models.Model):
    """Catégorie de logement"""
    libelle = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Type Logement"
        verbose_name_plural = "Types Logements"
    
    def __str__(self):
        return self.libelle


# ===================== LOGEMENT =====================

class Logement(models.Model):
    """Propriété à louer"""
    administrateur = models.ForeignKey(Administrateur, on_delete=models.CASCADE, related_name="logements")
    type_logement = models.ForeignKey(TypeLogement, on_delete=models.SET_NULL, null=True, blank=True, related_name="logements")
    titre = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.FloatField()
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    superficie = models.FloatField()
    nombre_pieces = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    caution = models.FloatField(default=0.0)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Logement"
        verbose_name_plural = "Logements"
    
    def get_details(self):
        """Retourner les détails du logement"""
        return {
            "titre": self.titre,
            "description": self.description,
            "prix": self.prix,
            "adresse": self.adresse,
            "ville": self.ville,
            "superficie": self.superficie,
            "nombre_pieces": self.nombre_pieces,
            "disponible": self.disponible,
        }
    
    def mettre_a_jour(self):
        """Mettre à jour le logement"""
        self.save()
    
    def __str__(self):
        return f"{self.titre} - {self.ville}"


# ===================== IMAGES & VIDEOS =====================

class Image(models.Model):
    """Image d'un logement"""
    logement = models.ForeignKey(Logement, on_delete=models.CASCADE, related_name="images")
    url = models.URLField()
    description = models.CharField(max_length=255, blank=True)
    ordre_affichage = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering = ["ordre_affichage"]
    
    def __str__(self):
        return f"Image - {self.logement.titre}"


class Video3D(models.Model):
    """Vidéo 3D d'un logement"""
    logement = models.ForeignKey(Logement, on_delete=models.CASCADE, related_name="videos_3d")
    url = models.URLField()
    description = models.CharField(max_length=255, blank=True)
    ordre_affichage = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Vidéo 3D"
        verbose_name_plural = "Vidéos 3D"
        ordering = ["ordre_affichage"]
    
    def __str__(self):
        return f"Vidéo 3D - {self.logement.titre}"


# ===================== FAVORI =====================

class Favori(models.Model):
    """Logement ajouté aux favoris"""
    logement = models.ForeignKey(Logement, on_delete=models.CASCADE, related_name="favoris")
    chercheur = models.ForeignKey(Chercheur, on_delete=models.CASCADE, related_name="favoris")
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Favori"
        verbose_name_plural = "Favoris"
        unique_together = ("logement", "chercheur")
    
    def __str__(self):
        return f"{self.chercheur.nom} - {self.logement.titre}"


# ===================== RESERVATION =====================

STATUT_RESERVATION_CHOICES = [
    ("en_attente", "En attente"),
    ("confirmée", "Confirmée"),
    ("annulée", "Annulée"),
    ("terminée", "Terminée"),
]


class Reservation(models.Model):
    """Réservation d'un logement"""
    logement = models.ForeignKey(Logement, on_delete=models.CASCADE, related_name="reservations")
    chercheur = models.ForeignKey(Chercheur, on_delete=models.CASCADE, related_name="reservations")
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUT_RESERVATION_CHOICES, default="en_attente")
    montant_total = models.FloatField(default=0.0)
    acompte = models.FloatField(default=0.0)
    date_reservation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Réservation"
        verbose_name_plural = "Réservations"
    
    def confirmer(self):
        """Confirmer la réservation"""
        self.statut = "confirmée"
        self.save()
    
    def annuler(self):
        """Annuler la réservation"""
        self.statut = "annulée"
        self.save()
    
    def terminer(self):
        """Terminer la réservation"""
        self.statut = "terminée"
        self.save()
    
    def __str__(self):
        return f"Réservation - {self.logement.titre} ({self.chercheur.nom})"


# ===================== PAIEMENT =====================

METHODE_PAIEMENT_CHOICES = [
    ("virement", "Virement bancaire"),
    ("carte", "Carte bancaire"),
    ("cheque", "Chèque"),
    ("especes", "Espèces"),
]

STATUT_PAIEMENT_CHOICES = [
    ("en_attente", "En attente"),
    ("effectué", "Effectué"),
    ("remboursé", "Remboursé"),
    ("échoué", "Échoué"),
]


class Paiement(models.Model):
    """Paiement pour une réservation"""
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="paiements")
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE, related_name="paiements")
    date_paiement = models.DateField(null=True, blank=True)
    montant = models.FloatField()
    methode = models.CharField(max_length=20, choices=METHODE_PAIEMENT_CHOICES)
    statut = models.CharField(max_length=20, choices=STATUT_PAIEMENT_CHOICES, default="en_attente")
    reference_transaction = models.CharField(max_length=100, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Paiement"
        verbose_name_plural = "Paiements"
    
    def effectuer(self):
        """Effectuer le paiement"""
        self.statut = "effectué"
        self.date_paiement = datetime.now().date()
        self.save()
    
    def rembourser(self):
        """Rembourser le paiement"""
        self.statut = "remboursé"
        self.save()
    
    def generer_recu(self):
        """Générer un reçu"""
        return f"Reçu n°{self.id} - {self.montant}€"
    
    def __str__(self):
        return f"Paiement {self.id} - {self.montant}€"


# ===================== VISITE 3D =====================

class Visite3D(models.Model):
    """Visite 3D d'un logement"""
    logement = models.ForeignKey(Logement, on_delete=models.CASCADE, related_name="visites_3d")
    chercheur = models.ForeignKey(Chercheur, on_delete=models.CASCADE, related_name="visites_3d")
    duree_visite = models.PositiveIntegerField(default=0, help_text="Durée en secondes")
    date_visite = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Visite 3D"
        verbose_name_plural = "Visites 3D"
    
    def demarrer(self):
        """Démarrer la visite"""
        self.date_visite = timezone.now()
        self.save()
    
    def changer_piece(self):
        """Changer de pièce pendant la visite"""
        pass
    
    def terminer(self):
        """Terminer la visite"""
        self.save()
    
    def __str__(self):
        return f"Visite 3D - {self.logement.titre}"
