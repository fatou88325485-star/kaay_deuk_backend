# Documentation API - Kaay Deuk

## Vue d'ensemble

L'API Kaay Deuk est une API REST complète pour une plateforme de location immobilière avec support des visites 3D. Cette API est construite avec Django REST Framework et documentée avec Swagger/OpenAPI.

## Accès à la Documentation Swagger

La documentation interactive Swagger est disponible à : `http://127.0.0.1:8000/api/docs/`

Documentation alternative ReDoc : `http://127.0.0.1:8000/api/redoc/`

Schéma OpenAPI (JSON) : `http://127.0.0.1:8000/api/schema/`

---

## Endpoints API

### 1. UTILISATEURS

#### Récupérer la liste des utilisateurs
```
GET /api/utilisateurs/
```

#### Créer un nouvel utilisateur
```
POST /api/utilisateurs/
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "secure_password123",
  "first_name": "John",
  "last_name": "Doe",
  "nom": "John Doe",
  "telephone": "+212612345678",
  "type_utilisateur": "chercheur"
}
```

#### Récupérer un utilisateur spécifique
```
GET /api/utilisateurs/{id}/
```

#### Mettre à jour un utilisateur
```
PUT /api/utilisateurs/{id}/
PATCH /api/utilisateurs/{id}/
```

#### Supprimer un utilisateur
```
DELETE /api/utilisateurs/{id}/
```

#### Changer le mot de passe d'un utilisateur
```
POST /api/utilisateurs/{id}/changer_mot_de_passe/
Content-Type: application/json

{
  "nouveau_mot_de_passe": "new_password123"
}
```

---

### 2. CHERCHEURS

Endpoints identiques aux utilisateurs pour la gestion des chercheurs.

```
GET    /api/chercheurs/              # Liste les chercheurs
POST   /api/chercheurs/              # Créer un chercheur
GET    /api/chercheurs/{id}/         # Détails du chercheur
PUT    /api/chercheurs/{id}/         # Mettre à jour
DELETE /api/chercheurs/{id}/         # Supprimer
```

---

### 3. ADMINISTRATEURS

Endpoints pour la gestion des administrateurs.

```
GET    /api/administrateurs/         # Liste les administrateurs
POST   /api/administrateurs/         # Créer un administrateur
GET    /api/administrateurs/{id}/    # Détails de l'administrateur
PUT    /api/administrateurs/{id}/    # Mettre à jour
DELETE /api/administrateurs/{id}/    # Supprimer
```

---

### 4. LOCATAIRES

Endpoints pour la gestion des locataires.

```
GET    /api/locataires/              # Liste les locataires
POST   /api/locataires/              # Créer un locataire
GET    /api/locataires/{id}/         # Détails du locataire
PUT    /api/locataires/{id}/         # Mettre à jour
DELETE /api/locataires/{id}/         # Supprimer
```

---

### 5. TYPES DE LOGEMENT

#### Récupérer la liste des types de logement
```
GET /api/types-logement/
```

#### Créer un nouveau type de logement
```
POST /api/types-logement/
Content-Type: application/json

{
  "libelle": "Appartement"
}
```

#### Récupérer un type de logement spécifique
```
GET /api/types-logement/{id}/
```

#### Mettre à jour un type de logement
```
PUT /api/types-logement/{id}/
PATCH /api/types-logement/{id}/
```

#### Supprimer un type de logement
```
DELETE /api/types-logement/{id}/
```

---

### 6. LOGEMENTS

#### Récupérer la liste de tous les logements
```
GET /api/logements/
```

Paramètres de recherche et filtrage :
- `search=` : Recherche par titre, description, ville ou adresse
- `ordering=prix` : Trier par prix
- `ordering=-date_creation` : Trier par date décroissante

#### Créer un nouveau logement
```
POST /api/logements/
Content-Type: application/json

{
  "administrateur": 1,
  "type_logement": 1,
  "titre": "Bel appartement à Casablanca",
  "description": "Spacieux apartement avec vue sur la mer",
  "prix": 5000.00,
  "adresse": "123 Boulevard Hassan II",
  "ville": "Casablanca",
  "superficie": 120.5,
  "nombre_pieces": 3,
  "disponible": true,
  "caution": 10000.00
}
```

#### Récupérer les détails d'un logement
```
GET /api/logements/{id}/
```

Retourne aussi les images et vidéos 3D associées.

#### Mettre à jour un logement
```
PUT /api/logements/{id}/
PATCH /api/logements/{id}/
```

#### Supprimer un logement
```
DELETE /api/logements/{id}/
```

#### Récupérer les logements disponibles
```
GET /api/logements/disponibles/
```

#### Rechercher les logements
```
GET /api/logements/rechercher/?ville=Casablanca&prix_min=3000&prix_max=8000
```

Paramètres :
- `ville` : Nom de la ville
- `prix_min` : Prix minimum
- `prix_max` : Prix maximum

---

### 7. IMAGES

#### Récupérer la liste des images
```
GET /api/images/
```

#### Ajouter une image
```
POST /api/images/
Content-Type: application/json

{
  "logement": 1,
  "url": "https://example.com/image1.jpg",
  "description": "Facade du logement",
  "ordre_affichage": 1
}
```

#### Récupérer une image spécifique
```
GET /api/images/{id}/
```

#### Mettre à jour une image
```
PUT /api/images/{id}/
PATCH /api/images/{id}/
```

#### Supprimer une image
```
DELETE /api/images/{id}/
```

---

### 8. VIDÉOS 3D

#### Récupérer la liste des vidéos 3D
```
GET /api/videos-3d/
```

#### Ajouter une vidéo 3D
```
POST /api/videos-3d/
Content-Type: application/json

{
  "logement": 1,
  "url": "https://example.com/video3d.mp4",
  "description": "Visite 3D complète du logement",
  "ordre_affichage": 1
}
```

#### Récupérer une vidéo 3D spécifique
```
GET /api/videos-3d/{id}/
```

#### Mettre à jour une vidéo 3D
```
PUT /api/videos-3d/{id}/
PATCH /api/videos-3d/{id}/
```

#### Supprimer une vidéo 3D
```
DELETE /api/videos-3d/{id}/
```

---

### 9. FAVORIS

#### Récupérer la liste des favoris
```
GET /api/favoris/
```

#### Ajouter un logement aux favoris
```
POST /api/favoris/
Content-Type: application/json

{
  "logement": 1,
  "chercheur": 1
}
```

#### Récupérer les favoris d'un chercheur
```
GET /api/favoris/mes_favoris/?chercheur_id=1
```

#### Supprimer un favori
```
DELETE /api/favoris/{id}/
```

---

### 10. RÉSERVATIONS

#### Récupérer la liste des réservations
```
GET /api/reservations/
```

#### Créer une réservation
```
POST /api/reservations/
Content-Type: application/json

{
  "logement": 1,
  "chercheur": 1,
  "date_debut": "2026-04-15",
  "date_fin": "2026-06-15",
  "montant_total": 10000.00,
  "acompte": 2000.00
}
```

#### Récupérer une réservation spécifique
```
GET /api/reservations/{id}/
```

#### Mettre à jour une réservation
```
PUT /api/reservations/{id}/
PATCH /api/reservations/{id}/
```

#### Confirmer une réservation
```
POST /api/reservations/{id}/confirmer/
```

#### Annuler une réservation
```
POST /api/reservations/{id}/annuler/
```

#### Terminer une réservation
```
POST /api/reservations/{id}/terminer/
```

#### Supprimer une réservation
```
DELETE /api/reservations/{id}/
```

---

### 11. PAIEMENTS

#### Récupérer la liste des paiements
```
GET /api/paiements/
```

#### Créer un paiement
```
POST /api/paiements/
Content-Type: application/json

{
  "reservation": 1,
  "locataire": 1,
  "montant": 5000.00,
  "methode": "virement",
  "reference_transaction": "REF123456"
}
```

#### Récupérer un paiement spécifique
```
GET /api/paiements/{id}/
```

#### Effectuer un paiement
```
POST /api/paiements/{id}/effectuer/
```

#### Rembourser un paiement
```
POST /api/paiements/{id}/rembourser/
```

#### Supprimer un paiement
```
DELETE /api/paiements/{id}/
```

Méthodes de paiement acceptées :
- `virement` : Virement bancaire
- `carte` : Carte bancaire
- `cheque` : Chèque
- `especes` : Espèces

Statuts de paiement :
- `en_attente` : En attente
- `effectué` : Effectué
- `remboursé` : Remboursé
- `échoué` : Échoué

---

### 12. VISITES 3D

#### Récupérer la liste des visites 3D
```
GET /api/visites-3d/
```

#### Créer une visite 3D
```
POST /api/visites-3d/
Content-Type: application/json

{
  "logement": 1,
  "chercheur": 1
}
```

#### Récupérer une visite 3D spécifique
```
GET /api/visites-3d/{id}/
```

#### Démarrer une visite 3D
```
POST /api/visites-3d/{id}/demarrer/
```

#### Terminer une visite 3D
```
POST /api/visites-3d/{id}/terminer/
```

#### Supprimer une visite 3D
```
DELETE /api/visites-3d/{id}/
```

---

## Statuts de Réservation

- `en_attente` : La réservation est en attente de confirmation
- `confirmée` : La réservation a été confirmée
- `annulée` : La réservation a été annulée
- `terminée` : La réservation est terminée

---

## Codes de Statut HTTP

- `200 OK` : Succès
- `201 CREATED` : Ressource créée avec succès
- `204 NO CONTENT` : Suppression réussie
- `400 BAD REQUEST` : Requête invalide
- `401 UNAUTHORIZED` : Non authentifié
- `404 NOT FOUND` : Ressource non trouvée
- `500 INTERNAL SERVER ERROR` : Erreur serveur

---

## Exemple d'utilisation complet (curl)

### 1. Créer un administrateur
```bash
curl -X POST http://127.0.0.1:8000/api/administrateurs/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin1",
    "email": "admin@example.com",
    "password": "admin123",
    "nom": "Admin User",
    "telephone": "+212612345678",
    "rib": "RIB123456789"
  }'
```

### 2. Créer un type de logement
```bash
curl -X POST http://127.0.0.1:8000/api/types-logement/ \
  -H "Content-Type: application/json" \
  -d '{"libelle": "Appartement"}'
```

### 3. Créer un logement
```bash
curl -X POST http://127.0.0.1:8000/api/logements/ \
  -H "Content-Type: application/json" \
  -d '{
    "administrateur": 1,
    "type_logement": 1,
    "titre": "Bel appartement à Casablanca",
    "description": "Spacieux avec vue sur la mer",
    "prix": 5000,
    "adresse": "123 Boulevard Hassan II",
    "ville": "Casablanca",
    "superficie": 120.5,
    "nombre_pieces": 3,
    "disponible": true,
    "caution": 10000
  }'
```

### 4. Récupérer les logements disponibles
```bash
curl http://127.0.0.1:8000/api/logements/disponibles/
```

### 5. Rechercher des logements
```bash
curl "http://127.0.0.1:8000/api/logements/rechercher/?ville=Casablanca&prix_min=3000&prix_max=8000"
```

---

## Pagination

Les réponses de liste sont paginées par défaut (10 items par page).

Exemple de réponse paginée :
```json
{
  "count": 50,
  "next": "http://127.0.0.1:8000/api/logements/?page=2",
  "previous": null,
  "results": [...]
}
```

---

## Notes importantes

1. **CORS configuré** pour localhost:3000 et localhost:8000
2. **Base de données** : SQLite (db.sqlite3)
3. **Serveur de développement** : http://127.0.0.1:8000/
4. **Documentation interactive** : http://127.0.0.1:8000/api/docs/

---

## Support et Questions

Pour des questions techniques, consultez :
- Documentation Swagger : http://127.0.0.1:8000/api/docs/
- Django REST Framework : https://www.django-rest-framework.org/
- drf-spectacular : https://drf-spectacular.readthedocs.io/
