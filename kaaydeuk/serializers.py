from rest_framework import serializers
from .models import (
    Utilisateur, Chercheur, Administrateur, Locataire, TypeLogement,
    Logement, Image, Video3D, Favori, Reservation, Paiement, Visite3D
)


# ===================== UTILISATEUR SERIALIZERS =====================

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'nom', 'telephone', 'type_utilisateur', 'date_creation',
            'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ChercheurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chercheur
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


class AdministrateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrateur
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


class LocataireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locataire
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


# ===================== TYPE LOGEMENT SERIALIZER =====================

class TypeLogementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeLogement
        fields = ['id', 'libelle']


# ===================== IMAGE & VIDEO SERIALIZERS =====================

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'logement', 'url', 'description', 'ordre_affichage']


class Video3DSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video3D
        fields = ['id', 'logement', 'url', 'description', 'ordre_affichage']


# ===================== LOGEMENT SERIALIZERS =====================

class LogementDetailSerializer(serializers.ModelSerializer):
    type_logement = TypeLogementSerializer(read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    videos_3d = Video3DSerializer(many=True, read_only=True)
    
    class Meta:
        model = Logement
        fields = [
            'id', 'administrateur', 'type_logement', 'titre', 'description',
            'prix', 'adresse', 'ville', 'superficie', 'nombre_pieces',
            'disponible', 'caution', 'date_creation', 'images', 'videos_3d'
        ]


class LogementSerializer(serializers.ModelSerializer):
    type_logement_detail = TypeLogementSerializer(source='type_logement', read_only=True)
    
    class Meta:
        model = Logement
        fields = [
            'id', 'administrateur', 'type_logement', 'type_logement_detail',
            'titre', 'description', 'prix', 'adresse', 'ville',
            'superficie', 'nombre_pieces', 'disponible', 'caution', 'date_creation'
        ]


# ===================== FAVORI SERIALIZER =====================

class FavoriSerializer(serializers.ModelSerializer):
    logement = LogementSerializer(read_only=True)
    
    class Meta:
        model = Favori
        fields = ['id', 'logement', 'chercheur', 'date_ajout']


# ===================== RESERVATION SERIALIZER =====================

class ReservationSerializer(serializers.ModelSerializer):
    logement = LogementSerializer(read_only=True)
    
    class Meta:
        model = Reservation
        fields = [
            'id', 'logement', 'chercheur', 'date_debut', 'date_fin',
            'statut', 'montant_total', 'acompte', 'date_reservation'
        ]


# ===================== PAIEMENT SERIALIZER =====================

class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = [
            'id', 'reservation', 'locataire', 'date_paiement',
            'montant', 'methode', 'statut', 'reference_transaction',
            'date_creation'
        ]


# ===================== VISITE 3D SERIALIZER =====================

class Visite3DSerializer(serializers.ModelSerializer):
    logement = LogementSerializer(read_only=True)
    
    class Meta:
        model = Visite3D
        fields = ['id', 'logement', 'chercheur', 'duree_visite', 'date_visite']
