# Projet OCR Dockerisé avec Gradio

Ce projet vise à déployer un moteur OCR récent et à l'exposer à l'aide d'une interface web Gradio. Le projet est divisé en plusieurs étapes, chacune construisant sur la précédente pour augmenter progressivement la complexité. Chaque étape implique la dockerisation de l'application et la mise en place des services nécessaires.

---

## Présentation du Projet

L'objectif est de construire un système OCR (Reconnaissance Optique de Caractères) performant et évolutif, capable de traiter des tâches de traitement d'images en temps réel.

### Objectifs du Projet

- Déployer un OCR avec Gradio.
- Mettre en place une file d'attente de tâches pour gérer plusieurs travailleurs.
- Implémenter un système asynchrone pour gérer les tâches longues et gourmandes en CPU.

---

## Étapes du Projet

### Étape 1: Dockerisation "Hello World" avec Gradio

#### Description :
- Dockerisation d'un exemple "Hello World" de Gradio pour créer une application d'exemple.
- Affichage d'une image en niveaux de gris avec le texte "Hello World".

#### Fichiers Requis :
1. **main.py :** Contient l'application "Hello World" utilisant Gradio.
2. **requirements.txt :** Liste des dépendances pour une construction reproductible.
3. **Dockerfile :** Recette pour construire l'image Docker.
4. **docker-compose.yaml :** Configuration de lancement pour le conteneur.

#### Instructions d'exécution :
1. Assurez-vous d'avoir Docker installé sur votre système.
2. Clonez ce dépôt sur votre machine.
3. Naviguez jusqu'au répertoire contenant les fichiers Docker.
4. Lancez le conteneur avec `docker compose up`.
5. Accédez à l'application via http://localhost:7860 dans votre navigateur (de préference sur Mozilla Firefox ou Google Chrome).

### Étape 2: Service de traitement d'images factice

#### Description :
- Cette étape déploie un service de traitement d'images factice pour tester le comportement de Gradio avec des entrées d'images.
- Le service applique un filtre sépia aux images d'entrée.

#### Fichiers Requis :
- Similaire à l'étape 1.
- **docker-compose.yaml :** Limiter la quantité maximale de la RAM d'un conteneur à 8Go.
- Creez un dossier **"donnees"** à la racine de stage 2 afin de configurer un volume pour stocker les fichiers générés lors de l'utilisation de la fonctionnalité **"Flag"** sur Gradio.

#### Instructions d'exécution :
- Similaire à l'étape 1.

### Étape 3: Système OCR Dockerisé

#### Description :
- Installation et utilisation de TrOCR avec Gradio pour la reconnaissance de texte.
- Utilisation d'un modèle pré-entraîné pour la reconnaissance de texte sur des images.

#### Fichiers Requis :
- Mêmes que l'étape 1 avec des ajustements pour TrOCR.
- Creez un dossier **"donnees"** à la racine de stage 3 afin de configurer un volume pour stocker les fichiers générés lors de l'utilisation de la fonctionnalité **"Flag"** sur Gradio.
- Creez un dossier **"huggingface_cache"** à la racine de stage 3. Cela permet d'éviter de télécharger les modèles à chaque demarrage du conteneur afin d'améliorer les performances. 

#### Instructions d'exécution :
- Similaire à l'étape 1.

#### Temps d'éxécution : 
- 2 à 3 minutes lors du premier téléchargement des modèles.
- Avec le volume **huggingface_cache**, 10 à 15 secondes pour les autres téléchargements.

### Étape 4: Asynchronous, High-Performance Processing using a Task Manager

#### Description :
- Utilisation de Celery pour la gestion des tâches et la mise en place d'un système asynchrone pour le traitement des images.
- Déploiement d'un système de gestion de tâches distribuées avec RabbitMQ.

#### Fichiers Requis :
- Mêmes que l'étape 1 avec des fichiers supplémentaires pour Celery.

#### Instructions d'exécution :
- Similaire à l'étape 1 avec l'ajout de services pour RabbitMQ et Celery.

---

## Auteurs :
- Kévin Berkant AKDOGAN (stage1 / stage4)
- Abdoulaye BALDE (stage2 / stage3)
