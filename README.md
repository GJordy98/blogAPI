API Django Rest Framework pour Blog
Cette API a été développée avec Django Rest Framework pour gérer un blog avec des fonctionnalités d'authentification, de gestion d'articles, de commentaires et de catégories.
Fonctionnalités
•	Authentification des utilisateurs et des administrateurs via SimpleJWT (token)
•	Gestion des articles (création, lecture, mise à jour, suppression)
•	Gestion des commentaires (création, lecture, suppression)
•	Gestion des catégories (création, lecture, mise à jour, suppression - réservée aux administrateurs)
•	Gestion des utilisateurs (création, lecture, mise à jour, suppression - certaines actions réservées aux administrateurs)
Installation
1.	•  Clonez le dépôt : 
git clone https://github.com/votre-nom/ApiBlog.git
cd ApiBlog

2.	Créez un environnement virtuel et activez-le :
py -m venv venv
source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
3.	Installez les dépendances :
pip install -r requirements.txt
4.	Effectuez les migrations :
py manage.py migrate
5.	Créez un superutilisateur :
py manage.py createsuperuser
6.	Lancez le serveur :
python manage.py runserver
Endpoints de l'API
•	/api/token/ : Obtenir un token JWT (POST)
•	/api/token/refresh/ : Rafraîchir un token JWT (POST)
•	/api/articles/ : Liste et création d'articles (GET, POST)
•	/api/articles/<id>/ : Détail, mise à jour et suppression d'un article (GET, PUT, DELETE)
•	/api/comments/ : Liste et création de commentaires (GET, POST)
•	/api/comments/<id>/ : Détail et suppression d'un commentaire (GET, DELETE)
•	/api/categories/ : Liste et création de catégories (GET, POST - création réservée aux admins)
•	/api/categories/<id>/ : Détail, mise à jour et suppression d'une catégorie (GET, PUT, DELETE - réservé aux admins)
•	/api/users/ : Liste et création d'utilisateurs (GET, POST)
•	/api/users/<id>/ : Détail, mise à jour et suppression d'un utilisateur (GET, PUT, DELETE - certaines actions réservées aux admins)
Authentification
L'API utilise SimpleJWT pour l'authentification. Pour accéder aux endpoints protégés, incluez le token JWT dans l'en-tête de vos requêtes :
Authorization: Bearer <votre_token_jwt>
Permissions
•	Les utilisateurs non authentifiés peuvent lire les articles, commentaires et catégories.
•	Les utilisateurs authentifiés peuvent créer des articles et des commentaires.
•	Les auteurs d'articles peuvent mettre à jour ou supprimer leurs propres articles.
•	Les administrateurs ont un accès complet à toutes les fonctionnalités, y compris la gestion des catégories et la suppression de tout contenu.
Exemple d'utilisation
Obtenir un token :
	curl -X POST http://localhost:8000/api/token/ -d "username=votre_username&password=votre_mot_de_passe"
Créer un article (en tant qu'utilisateur authentifié) :
	curl -X POST http://localhost:8000/api/articles/ -H "Authorization: Bearer <votre_token>" -d "title=Mon Article&content=Contenu de l'article&category=1"
Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

