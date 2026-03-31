from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import (
    Utilisateur, Chercheur, Administrateur, Locataire, TypeLogement,
    Logement, Image, Video3D, Favori, Reservation, Paiement, Visite3D
)
from .serializers import (
    UtilisateurSerializer, ChercheurSerializer, AdministrateurSerializer,
    LocataireSerializer, TypeLogementSerializer, LogementSerializer,
    LogementDetailSerializer, ImageSerializer, Video3DSerializer,
    FavoriSerializer, ReservationSerializer, PaiementSerializer,
    Visite3DSerializer
)


# ===================== ROOT VIEW =====================

def api_root(request):
    """Vue racine de l'API"""
    return JsonResponse({
        'message': 'Bienvenue sur l\'API Kaay Deuk',
        'description': 'Plateforme de location immobilière avec visites 3D',
        'version': '1.0.0',
        'documentation': 'http://127.0.0.1:8000/api/docs/',
        'endpoints': {
            'utilisateurs': 'http://127.0.0.1:8000/api/utilisateurs/',
            'chercheurs': 'http://127.0.0.1:8000/api/chercheurs/',
            'administrateurs': 'http://127.0.0.1:8000/api/administrateurs/',
            'locataires': 'http://127.0.0.1:8000/api/locataires/',
            'types_logement': 'http://127.0.0.1:8000/api/types-logement/',
            'logements': 'http://127.0.0.1:8000/api/logements/',
            'images': 'http://127.0.0.1:8000/api/images/',
            'videos_3d': 'http://127.0.0.1:8000/api/videos-3d/',
            'favoris': 'http://127.0.0.1:8000/api/favoris/',
            'reservations': 'http://127.0.0.1:8000/api/reservations/',
            'paiements': 'http://127.0.0.1:8000/api/paiements/',
            'visites_3d': 'http://127.0.0.1:8000/api/visites-3d/'
        }
    })


# ===================== UTILISATEUR VIEWSETS =====================

class UtilisateurViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les utilisateurs.
    
    list: Récupérer la liste de tous les utilisateurs
    create: Créer un nouvel utilisateur
    retrieve: Récupérer les détails d'un utilisateur
    update: Mettre à jour un utilisateur
    destroy: Supprimer un utilisateur
    """
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [AllowAny]
    
    @action(detail=True, methods=['post'])
    def changer_mot_de_passe(self, request, pk=None):
        """Changer le mot de passe d'un utilisateur"""
        utilisateur = self.get_object()
        nouveau_mot_de_passe = request.data.get('nouveau_mot_de_passe')
        if nouveau_mot_de_passe:
            utilisateur.set_password(nouveau_mot_de_passe)
            utilisateur.save()
            return Response({'detail': 'Mot de passe changé avec succès'})
        return Response({'error': 'nouveau_mot_de_passe est requis'}, status=status.HTTP_400_BAD_REQUEST)


class ChercheurViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les chercheurs.
    
    list: Récupérer la liste de tous les chercheurs
    create: Créer un nouveau chercheur
    retrieve: Récupérer les détails d'un chercheur
    update: Mettre à jour un chercheur
    destroy: Supprimer un chercheur
    """
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer
    permission_classes = [AllowAny]


class AdministrateurViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les administrateurs.
    
    list: Récupérer la liste de tous les administrateurs
    create: Créer un nouvel administrateur
    retrieve: Récupérer les détails d'un administrateur
    update: Mettre à jour un administrateur
    destroy: Supprimer un administrateur
    """
    queryset = Administrateur.objects.all()
    serializer_class = AdministrateurSerializer
    permission_classes = [AllowAny]


class LocataireViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les locataires.
    
    list: Récupérer la liste de tous les locataires
    create: Créer un nouveau locataire
    retrieve: Récupérer les détails d'un locataire
    update: Mettre à jour un locataire
    destroy: Supprimer un locataire
    """
    queryset = Locataire.objects.all()
    serializer_class = LocataireSerializer
    permission_classes = [AllowAny]


# ===================== TYPE LOGEMENT VIEWSET =====================

class TypeLogementViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les types de logement.
    
    list: Récupérer la liste de tous les types de logement
    create: Créer un nouveau type de logement
    retrieve: Récupérer les détails d'un type de logement
    update: Mettre à jour un type de logement
    destroy: Supprimer un type de logement
    """
    queryset = TypeLogement.objects.all()
    serializer_class = TypeLogementSerializer
    permission_classes = [AllowAny]


# ===================== LOGEMENT VIEWSET =====================

class LogementViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les logements.
    
    list: Récupérer la liste de tous les logements
    create: Créer un nouveau logement
    retrieve: Récupérer les détails d'un logement avec images et vidéos
    update: Mettre à jour un logement
    destroy: Supprimer un logement
    disponibles: Récupérer les logements disponibles
    rechercher: Rechercher les logements par ville ou titre
    """
    queryset = Logement.objects.all()
    serializer_class = LogementSerializer
    permission_classes = [AllowAny]
    search_fields = ['titre', 'description', 'ville', 'adresse']
    ordering_fields = ['prix', 'date_creation', 'superficie']
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return LogementDetailSerializer
        return LogementSerializer
    
    @action(detail=False, methods=['get'])
    def disponibles(self, request):
        """Récupérer les logements disponibles"""
        logements = Logement.objects.filter(disponible=True)
        serializer = self.get_serializer(logements, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def rechercher(self, request):
        """Rechercher les logements par village"""
        ville = request.query_params.get('ville', None)
        prix_min = request.query_params.get('prix_min', None)
        prix_max = request.query_params.get('prix_max', None)
        
        logements = Logement.objects.all()
        
        if ville:
            logements = logements.filter(ville__icontains=ville)
        if prix_min:
            logements = logements.filter(prix__gte=prix_min)
        if prix_max:
            logements = logements.filter(prix__lte=prix_max)
        
        serializer = self.get_serializer(logements, many=True)
        return Response(serializer.data)


# ===================== IMAGE & VIDEO VIEWSETS =====================

class ImageViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les images des logements.
    
    list: Récupérer la liste de toutes les images
    create: Ajouter une nouvelle image
    retrieve: Récupérer les détails d'une image
    update: Mettre à jour une image
    destroy: Supprimer une image
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]


class Video3DViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les vidéos 3D des logements.
    
    list: Récupérer la liste de toutes les vidéos 3D
    create: Ajouter une nouvelle vidéo 3D
    retrieve: Récupérer les détails d'une vidéo 3D
    update: Mettre à jour une vidéo 3D
    destroy: Supprimer une vidéo 3D
    """
    queryset = Video3D.objects.all()
    serializer_class = Video3DSerializer
    permission_classes = [AllowAny]


# ===================== FAVORI VIEWSET =====================

class FavoriViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les favoris.
    
    list: Récupérer la liste des favoris
    create: Ajouter un logement aux favoris
    retrieve: Récupérer les détails d'un favori
    destroy: Supprimer un favori
    mes_favoris: Récupérer les favoris de l'utilisateur courant
    """
    queryset = Favori.objects.all()
    serializer_class = FavoriSerializer
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['get'])
    def mes_favoris(self, request):
        """Récupérer les favoris de l'utilisateur courant"""
        chercheur_id = request.query_params.get('chercheur_id')
        if chercheur_id:
            favoris = Favori.objects.filter(chercheur_id=chercheur_id)
            serializer = self.get_serializer(favoris, many=True)
            return Response(serializer.data)
        return Response({'error': 'chercheur_id est requis'}, status=status.HTTP_400_BAD_REQUEST)


# ===================== RESERVATION VIEWSET =====================

class ReservationViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les réservations.
    
    list: Récupérer la liste de toutes les réservations
    create: Créer une nouvelle réservation
    retrieve: Récupérer les détails d'une réservation
    update: Mettre à jour une réservation
    destroy: Supprimer une réservation
    confirmer: Confirmer une réservation
    annuler: Annuler une réservation
    terminer: Terminer une réservation
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [AllowAny]
    
    @action(detail=True, methods=['post'])
    def confirmer(self, request, pk=None):
        """Confirmer une réservation"""
        reservation = self.get_object()
        reservation.confirmer()
        serializer = self.get_serializer(reservation)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def annuler(self, request, pk=None):
        """Annuler une réservation"""
        reservation = self.get_object()
        reservation.annuler()
        serializer = self.get_serializer(reservation)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def terminer(self, request, pk=None):
        """Terminer une réservation"""
        reservation = self.get_object()
        reservation.terminer()
        serializer = self.get_serializer(reservation)
        return Response(serializer.data)


# ===================== PAIEMENT VIEWSET =====================

class PaiementViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les paiements.
    
    list: Récupérer la liste de tous les paiements
    create: Créer un nouveau paiement
    retrieve: Récupérer les détails d'un paiement
    update: Mettre à jour un paiement
    destroy: Supprimer un paiement
    effectuer: Effectuer un paiement
    rembourser: Rembourser un paiement
    """
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer
    permission_classes = [AllowAny]
    
    @action(detail=True, methods=['post'])
    def effectuer(self, request, pk=None):
        """Effectuer un paiement"""
        paiement = self.get_object()
        paiement.effectuer()
        serializer = self.get_serializer(paiement)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def rembourser(self, request, pk=None):
        """Rembourser un paiement"""
        paiement = self.get_object()
        paiement.rembourser()
        serializer = self.get_serializer(paiement)
        return Response(serializer.data)


# ===================== VISITE 3D VIEWSET =====================

class Visite3DViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les visites 3D.
    
    list: Récupérer la liste de toutes les visites 3D
    create: Créer une nouvelle visite 3D
    retrieve: Récupérer les détails d'une visite 3D
    update: Mettre à jour une visite 3D
    destroy: Supprimer une visite 3D
    demarrer: Démarrer une visite 3D
    terminer: Terminer une visite 3D
    """
    queryset = Visite3D.objects.all()
    serializer_class = Visite3DSerializer
    permission_classes = [AllowAny]
    
    @action(detail=True, methods=['post'])
    def demarrer(self, request, pk=None):
        """Démarrer une visite 3D"""
        visite = self.get_object()
        visite.demarrer()
        serializer = self.get_serializer(visite)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def terminer(self, request, pk=None):
        """Terminer une visite 3D"""
        visite = self.get_object()
        visite.terminer()
        serializer = self.get_serializer(visite)
        return Response(serializer.data)
