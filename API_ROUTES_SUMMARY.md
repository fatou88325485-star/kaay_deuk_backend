# Résumé des Routes API - Kaay Deuk

## Tableau récapitulatif des endpoints

| Ressource | Méthode | Endpoint | Description |
|-----------|---------|----------|-------------|
| **Utilisateurs** |
| | GET | `/api/utilisateurs/` | Lister tous les utilisateurs |
| | POST | `/api/utilisateurs/` | Créer un utilisateur |
| | GET | `/api/utilisateurs/{id}/` | Détails d'un utilisateur |
| | PUT | `/api/utilisateurs/{id}/` | Mettre à jour un utilisateur |
| | DELETE | `/api/utilisateurs/{id}/` | Supprimer un utilisateur |
| | POST | `/api/utilisateurs/{id}/changer_mot_de_passe/` | Changer le mot de passe |
| **Chercheurs** |
| | GET | `/api/chercheurs/` | Lister tous les chercheurs |
| | POST | `/api/chercheurs/` | Créer un chercheur |
| | GET | `/api/chercheurs/{id}/` | Détails d'un chercheur |
| | PUT | `/api/chercheurs/{id}/` | Mettre à jour un chercheur |
| | DELETE | `/api/chercheurs/{id}/` | Supprimer un chercheur |
| **Administrateurs** |
| | GET | `/api/administrateurs/` | Lister tous les administrateurs |
| | POST | `/api/administrateurs/` | Créer un administrateur |
| | GET | `/api/administrateurs/{id}/` | Détails d'un administrateur |
| | PUT | `/api/administrateurs/{id}/` | Mettre à jour un administrateur |
| | DELETE | `/api/administrateurs/{id}/` | Supprimer un administrateur |
| **Locataires** |
| | GET | `/api/locataires/` | Lister tous les locataires |
| | POST | `/api/locataires/` | Créer un locataire |
| | GET | `/api/locataires/{id}/` | Détails d'un locataire |
| | PUT | `/api/locataires/{id}/` | Mettre à jour un locataire |
| | DELETE | `/api/locataires/{id}/` | Supprimer un locataire |
| **Types de Logement** |
| | GET | `/api/types-logement/` | Lister tous les types |
| | POST | `/api/types-logement/` | Créer un type |
| | GET | `/api/types-logement/{id}/` | Détails d'un type |
| | PUT | `/api/types-logement/{id}/` | Mettre à jour un type |
| | DELETE | `/api/types-logement/{id}/` | Supprimer un type |
| **Logements** |
| | GET | `/api/logements/` | Lister tous les logements |
| | POST | `/api/logements/` | Créer un logement |
| | GET | `/api/logements/{id}/` | Détails d'un logement avec médias |
| | PUT | `/api/logements/{id}/` | Mettre à jour un logement |
| | DELETE | `/api/logements/{id}/` | Supprimer un logement |
| | GET | `/api/logements/disponibles/` | Logements disponibles |
| | GET | `/api/logements/rechercher/` | Rechercher des logements |
| **Images** |
| | GET | `/api/images/` | Lister toutes les images |
| | POST | `/api/images/` | Ajouter une image |
| | GET | `/api/images/{id}/` | Détails d'une image |
| | PUT | `/api/images/{id}/` | Mettre à jour une image |
| | DELETE | `/api/images/{id}/` | Supprimer une image |
| **Vidéos 3D** |
| | GET | `/api/videos-3d/` | Lister toutes les vidéos |
| | POST | `/api/videos-3d/` | Ajouter une vidéo 3D |
| | GET | `/api/videos-3d/{id}/` | Détails d'une vidéo |
| | PUT | `/api/videos-3d/{id}/` | Mettre à jour une vidéo |
| | DELETE | `/api/videos-3d/{id}/` | Supprimer une vidéo |
| **Favoris** |
| | GET | `/api/favoris/` | Lister tous les favoris |
| | POST | `/api/favoris/` | Ajouter un favori |
| | GET | `/api/favoris/mes_favoris/` | Favoris d'un chercheur |
| | DELETE | `/api/favoris/{id}/` | Supprimer un favori |
| **Réservations** |
| | GET | `/api/reservations/` | Lister toutes les réservations |
| | POST | `/api/reservations/` | Créer une réservation |
| | GET | `/api/reservations/{id}/` | Détails d'une réservation |
| | PUT | `/api/reservations/{id}/` | Mettre à jour une réservation |
| | POST | `/api/reservations/{id}/confirmer/` | Confirmer une réservation |
| | POST | `/api/reservations/{id}/annuler/` | Annuler une réservation |
| | POST | `/api/reservations/{id}/terminer/` | Terminer une réservation |
| | DELETE | `/api/reservations/{id}/` | Supprimer une réservation |
| **Paiements** |
| | GET | `/api/paiements/` | Lister tous les paiements |
| | POST | `/api/paiements/` | Créer un paiement |
| | GET | `/api/paiements/{id}/` | Détails d'un paiement |
| | PUT | `/api/paiements/{id}/` | Mettre à jour un paiement |
| | POST | `/api/paiements/{id}/effectuer/` | Effectuer un paiement |
| | POST | `/api/paiements/{id}/rembourser/` | Rembourser un paiement |
| | DELETE | `/api/paiements/{id}/` | Supprimer un paiement |
| **Visites 3D** |
| | GET | `/api/visites-3d/` | Lister toutes les visites |
| | POST | `/api/visites-3d/` | Créer une visite 3D |
| | GET | `/api/visites-3d/{id}/` | Détails d'une visite |
| | POST | `/api/visites-3d/{id}/demarrer/` | Démarrer une visite |
| | POST | `/api/visites-3d/{id}/terminer/` | Terminer une visite |
| | DELETE | `/api/visites-3d/{id}/` | Supprimer une visite |

---

## Documentation Interactive

### Swagger UI
**URL** : http://127.0.0.1:8000/api/docs/

Interface interactive pour tester tous les endpoints avec interface utilisateur graphique.

### ReDoc
**URL** : http://127.0.0.1:8000/api/redoc/

Documentation alternative avec un layout différent.

### Schéma OpenAPI (JSON)
**URL** : http://127.0.0.1:8000/api/schema/

Schéma JSON brut pour l'intégration automatisée.

---

## Exemples de Paramètres

### Recherche et Filtrage

#### Logements - Rechercher
```
GET /api/logements/rechercher/?ville=Casablanca&prix_min=3000&prix_max=8000
```

Paramètres disponibles :
- `ville` : Filtrer par village
- `prix_min` : Prix minimum
- `prix_max` : Prix maximum

#### Logements - Trier
```
GET /api/logements/?ordering=prix
GET /api/logements/?ordering=-date_creation
```

#### Favoris - Mes favoris
```
GET /api/favoris/mes_favoris/?chercheur_id=1
```

### Pagination

Par défaut : 10 items par page
```
GET /api/logements/?page=2
```

---

## Authentification (À implémenter)

Les permissions actuelles sont `AllowAny`. Pour activer l'authentification :

1. Installer `djangorestframework-simplejwt` ou `django-rest-knox`
2. Ajouter les endpoints de login
3. Mettre à jour les ViewSets avec les permissions appropriées

---

## Codes de Statut HTTP

| Code | Signification |
|------|--------------|
| 200 | OK - Succès |
| 201 | Created - Ressource créée |
| 204 | No Content - Suppression réussie |
| 400 | Bad Request - Requête invalide |
| 401 | Unauthorized - Non authentifié |
| 403 | Forbidden - Accès refusé |
| 404 | Not Found - Ressource non trouvée |
| 500 | Server Error - Erreur serveur |

---

## Installation et Démarrage

```bash
# Installer les dépendances
pip install djangorestframework drf-spectacular django-cors-headers

# Appliquer les migrations
python manage.py migrate

# Créer un superuser (optionnel)
python manage.py createsuperuser

# Démarrer le serveur
python manage.py runserver
```

---

## Fichiers créés

1. **kaaydeuk/serializers.py** - Sérializeurs pour tous les modèles
2. **kaaydeuk/views.py** - ViewSets pour tous les modèles
3. **kaaydeuk/urls.py** - Configuration des routes API et Swagger
4. **kaaydeuk/settings.py** - Configuration de REST Framework

---

## Configuration CORS

La configuration CORS permet les requêtes depuis :
- `http://localhost:3000`
- `http://127.0.0.1:3000`
- `http://localhost:8000`
- `http://127.0.0.1:8000`

Pour ajouter d'autres domaines, modifiez `CORS_ALLOWED_ORIGINS` dans `settings.py`.

---

## Prochaines étapes

1. **Authentification** : Implémenter JWT ou Token-based auth
2. **Permissions** : Ajouter des permissions par rôle (admin, chercheur, etc.)
3. **Tests** : Créer des tests unitaires pour les endpoints
4. **Validation** : Ajouter des validateurs personnalisés
5. **Versioning** : Implémenter le versioning API si nécessaire
