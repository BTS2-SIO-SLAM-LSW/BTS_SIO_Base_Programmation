# 🚀 TP 2.1 - GitHub Codespaces + Python Professionnel
**Module B1.1 Algorithmique - Séance 2.1**  
**Durée :** 1h  
**Objectif :** Découvrir l'environnement professionnel et approfondir Python  
**Plateforme :** GitHub Codespaces + VS Code

---

## 🎯 **OBJECTIFS DU TP (1 HEURE)**

À la fin de ce TP, vous saurez :
- ✅ Créer un GitHub Codespace 
- ✅ Utiliser VS Code comme un pro
- ✅ Faire des interactions Python avec input()
- ✅ Utiliser if/elif/else intelligemment
- ✅ Sauvegarder avec Git

---

## ⏰ **PLANNING SIMPLIFIÉ (1h)**

| **Temps** | **Activité** | **Résultat** |
|-----------|--------------|--------------|
| **0-15min** | Configuration GitHub Codespaces | Environnement prêt |
| **15-30min** | Interactions Python avec input() | Programme interactif |
| **30-45min** | Conditions if/elif/else | Application intelligente |
| **45-60min** | Sauvegarde Git | Code sauvegardé sur GitHub |

---

## 🛠️ **ÉTAPE 1 : CONFIGURATION EXPRESS (15min)**

### **1.1 Créer le Repository GitHub**

1. **Aller sur :** https://github.com
2. **Se connecter** avec votre compte
3. **Cliquer** sur le bouton vert "New" (ou le "+" en haut à droite)
4. **Remplir :**
   ```
   Repository name: b11-tp2-python
   Description: TP2 - Python avec Codespaces
   ✅ Public
   ✅ Add a README file
   ✅ Add .gitignore → choisir "Python"
   ```
5. **Cliquer** "Create repository"

### **1.2 Lancer le Codespace**

1. **Sur votre repository**, cliquer le bouton vert **"Code"**
2. **Onglet "Codespaces"**
3. **Cliquer** "Create codespace on main"
4. **Attendre 1-2 minutes** ⏳

🎉 **Résultat :** VS Code s'ouvre dans votre navigateur !

### **1.3 Test Rapide de l'Environnement**

1. **Dans VS Code**, créer un nouveau fichier : **Ctrl+N**
2. **Sauvegarder** : **Ctrl+S** → nommer `test.py`
3. **Taper ce code simple :**

```python
print("🚀 Mon environnement Codespaces fonctionne !")
print("Python version :", end=" ")

import sys
print(sys.version_info.major, ".", sys.version_info.minor)
```

4. **Exécuter** : **F5** ou **Clic droit** → "Run Python File in Terminal"

**✅ VALIDATION :** Vous voyez le message dans le terminal en bas !

---

## 🗣️ **ÉTAPE 2 : INTERACTIONS PYTHON AVEC INPUT() (15min)**

### **2.1 Créer Votre Première App Interactive**

1. **Nouveau fichier :** `presentation.py`
2. **Code à taper étape par étape :**

```python
# Mon premier programme interactif
print("🎯 CRÉATEUR DE PRÉSENTATION")
print("=" * 30)

# Demander des informations
prenom = input("👤 Votre prénom : ")
age = input("🎂 Votre âge : ")
ville = input("🏠 Votre ville : ")

# Afficher le résultat
print("\n✨ VOTRE PRÉSENTATION :")
print(f"Je m'appelle {prenom}")
print(f"J'ai {age} ans")
print(f"J'habite à {ville}")
```

3. **Tester** : F5 et suivre les questions !

### **2.2 Améliorer avec des Calculs**

**Améliorer le fichier `presentation.py` :**

```python
# Mon premier programme interactif AMÉLIORÉ
print("🎯 CRÉATEUR DE PRÉSENTATION AVANCÉ")
print("=" * 35)

# Demander des informations
prenom = input("👤 Votre prénom : ")
age = int(input("🎂 Votre âge : "))  # int() pour convertir en nombre
ville = input("🏠 Votre ville : ")

# Calculs automatiques
annee_naissance = 2024 - age
age_dans_10_ans = age + 10

# Affichage amélioré
print("\n✨ VOTRE PRÉSENTATION COMPLÈTE :")
print(f"👋 Salut ! Je m'appelle {prenom.title()}")
print(f"🎂 J'ai {age} ans (né en {annee_naissance})")
print(f"🏠 Je vis à {ville.title()}")
print(f"🔮 Dans 10 ans, j'aurai {age_dans_10_ans} ans !")
```

**✅ VALIDATION :** Votre programme pose des questions ET calcule des résultats !

---

## 🤔 **ÉTAPE 3 : CONDITIONS INTELLIGENTES (15min)**

### **3.1 Créer une Calculatrice Intelligente**

1. **Nouveau fichier :** `calculatrice.py`
2. **Code simple mais efficace :**

```python
print("🧮 CALCULATRICE INTELLIGENTE")
print("=" * 30)

# Demander les nombres
nombre1 = float(input("🔢 Premier nombre : "))
nombre2 = float(input("🔢 Deuxième nombre : "))

print("\nChoisissez l'opération :")
print("1. Addition (+)")
print("2. Soustraction (-)")
print("3. Multiplication (×)")
print("4. Division (÷)")

choix = input("\n👆 Votre choix (1, 2, 3 ou 4) : ")

# Conditions intelligentes
if choix == "1":
    resultat = nombre1 + nombre2
    print(f"➕ {nombre1} + {nombre2} = {resultat}")
elif choix == "2":
    resultat = nombre1 - nombre2
    print(f"➖ {nombre1} - {nombre2} = {resultat}")
elif choix == "3":
    resultat = nombre1 * nombre2
    print(f"✖️ {nombre1} × {nombre2} = {resultat}")
elif choix == "4":
    if nombre2 != 0:
        resultat = nombre1 / nombre2
        print(f"➗ {nombre1} ÷ {nombre2} = {resultat}")
    else:
        print("❌ Erreur : Division par zéro impossible !")
else:
    print("❌ Choix invalide !")
```

### **3.2 Ajouter de l'Intelligence**

**Améliorer `calculatrice.py` - ajouter à la fin :**

```python
# Intelligence supplémentaire
if choix in ["1", "2", "3", "4"] and (choix != "4" or nombre2 != 0):
    # Analyser le résultat
    if resultat > 100:
        print("📈 Wahou ! Grand résultat !")
    elif resultat < 0:
        print("📉 Résultat négatif")
    elif resultat == 0:
        print("🎯 Résultat exact : zéro !")
    else:
        print("👌 Résultat raisonnable")
```

**✅ VALIDATION :** Votre calculatrice analyse et commente ses résultats !

### **3.3 App de Notation Scolaire**

1. **Nouveau fichier :** `notes.py`
2. **Code pédagogique :**

```python
print("🎓 ANALYSEUR DE NOTES")
print("=" * 25)

# Demander la note
note = float(input("📝 Entrez votre note sur 20 : "))

# Validation de base
if note < 0 or note > 20:
    print("❌ Note invalide ! (doit être entre 0 et 20)")
else:
    print(f"\n📊 Analyse de votre note : {note}/20")
    
    # Conditions en cascade pour les mentions
    if note >= 16:
        print("🏆 Mention : TRÈS BIEN !")
        print("⭐ Excellent travail, continuez !")
    elif note >= 14:
        print("💪 Mention : BIEN")
        print("👍 Très bon niveau, bravo !")
    elif note >= 12:
        print("👌 Mention : ASSEZ BIEN")
        print("📚 Bon travail, vous progressez !")
    elif note >= 10:
        print("✅ Mention : PASSABLE")
        print("⚠️ Travaillez encore un peu !")
    else:
        print("❌ Mention : INSUFFISANT")
        print("💪 Courage, il faut reprendre !")
    
    # Calculs bonus
    points_manquants = 20 - note
    if points_manquants > 0:
        print(f"🎯 Il vous manque {points_manquants} points pour avoir 20/20")
```

**✅ VALIDATION :** Une app qui donne des mentions ET des conseils !

---

## 💾 **ÉTAPE 4 : SAUVEGARDE GIT (15min)**

### **4.1 Comprendre ce qu'on va faire**

**Git = système de sauvegarde intelligent :**
- 📸 **Prendre une "photo"** de votre code à un instant T
- 📤 **Envoyer sur GitHub** pour ne jamais perdre votre travail
- 🔄 **Revenir en arrière** si nécessaire

### **4.2 Commandes Git Essentielles**

**Dans le terminal VS Code (en bas) :**

1. **Voir ce qui a changé :**
```bash
git status
```
*Résultat : liste des fichiers modifiés*

2. **Ajouter TOUS les fichiers :**
```bash
git add .
```
*Le point = "tout"*

3. **Prendre la "photo" (commit) :**
```bash
git commit -m "✨ TP2 : Mes premières apps Python interactives"
```
*Le -m = message de description*

4. **Envoyer sur GitHub :**
```bash
git push
```

### **4.3 Vérification sur GitHub**

1. **Aller sur votre repository** GitHub dans un nouvel onglet
2. **F5** pour actualiser
3. **Voir vos fichiers** : `test.py`, `presentation.py`, `calculatrice.py`, `notes.py`

🎉 **Résultat :** Votre code est sauvegardé pour toujours !

---

## 🏆 **BILAN : VOTRE ARCHITECTURE PROFESSIONNELLE MAÎTRISÉE**

### **🏗️ Architecture de Développement Construite**

**Vous venez de mettre en place une infrastructure complète :**

```
🎯 VOTRE STACK TECHNOLOGIQUE PROFESSIONNELLE

┌─ COUCHE STOCKAGE ────────────────────────┐
│ 🌐 GitHub Repository                    │ ← Code source centralisé
│   ├── 📂 Gestion de versions (Git)      │
│   ├── 👥 Collaboration native           │
│   └── ♾️ Sauvegarde permanente          │
└─────────────────────────────────────────┘
                    ↕️ Synchronisation
┌─ COUCHE DÉVELOPPEMENT ───────────────────┐
│ ☁️ GitHub Codespace                     │ ← Environnement isolé  
│   ├── 🖥️ VS Code (IDE professionnel)    │
│   ├── 🐍 Python 3.11+ (runtime)        │
│   ├── 🔧 Extensions automatiques        │
│   └── 💻 Terminal intégré              │
└─────────────────────────────────────────┘
                    ↕️ Workflow Git
┌─ COUCHE APPLICATIONS ────────────────────┐
│ 📱 Vos Applications Python              │ ← Code métier
│   ├── 🎯 Présentation interactive       │
│   ├── 🧮 Calculatrice intelligente      │
│   └── 🎓 Analyseur de notes             │
└─────────────────────────────────────────┘
```

### **💼 Équivalent Entreprise SISR/SLAM**

| **Ce que vous avez fait** | **En entreprise SISR** | **En entreprise SLAM** |
|---------------------------|-------------------------|-------------------------|
| 🏗️ Architecture Codespaces | Infrastructure cloud (AWS, Azure) | Environnements de développement |
| 📦 Repository GitHub | Gestion de configurations système | Gestion du code source |
| 🔄 Workflow Git | Déploiement automatisé (DevOps) | Intégration continue (CI/CD) |
| 🐍 Applications Python | Scripts d'administration | Applications métier |

### **🛠️ Compétences Professionnelles Acquises**

#### **🏗️ Architecture & Infrastructure**
- ✅ **Cloud-Native Development** : Développement délocalisé
- ✅ **Containerisation** : Environnements isolés et reproductibles  
- ✅ **Version Control** : Git workflow professionnel
- ✅ **DevOps mindset** : Integration développement/déploiement

#### **🐍 Développement Python Avancé**
- ✅ **Input/Output interactif** : Collecte et traitement de données utilisateur
- ✅ **Logique conditionnelle** : if/elif/else pour créer des comportements intelligents
- ✅ **Validation de données** : Contrôle de la qualité des saisies
- ✅ **Formatage avancé** : f-strings pour des interfaces professionnelles

#### **💻 Outils Professionnels**
- ✅ **VS Code maîtrisé** : IDE utilisé par 70% des développeurs mondiaux
- ✅ **Terminal intégré** : Ligne de commande pour l'automatisation
- ✅ **Extensions intelligentes** : Auto-complétion, debugging, linting
- ✅ **Workflow moderne** : Développement, test, déploiement intégrés

### **📊 Applications Développées (Portfolio)**

1. **🎯 Présentation Interactive** 
   - Collecte de données utilisateur
   - Calculs automatiques (âge, projections)
   - Formatage intelligent des chaînes

2. **🧮 Calculatrice Intelligente**
   - Interface à menu (UX)
   - Logique conditionnelle complexe  
   - Analyse et commentaire des résultats

3. **🎓 Analyseur de Notes**
   - Validation des données d'entrée
   - Conditions en cascade (mentions)
   - Conseils personnalisés automatiques

### **🚀 Architecture Évolutive**

**Cette base vous permet maintenant d'ajouter :**
- 🔄 **Boucles for/while** : Traitement de données en masse
- 📋 **Listes et dictionnaires** : Structures de données complexes  
- 🔧 **Fonctions avancées** : Modularité et réutilisabilité
- 📊 **APIs et bases de données** : Applications connectées
- 🌐 **Interfaces web** : Applications accessibles via navigateur

### **💡 Réflexion Métier**

**🖥️ Pour SISR (Solutions d'Infrastructure) :**
- Cette architecture = **Infrastructure as Code (IaC)**
- Codespaces = **Containers et orchestration**  
- Git = **Configuration management**
- Applications Python = **Automation et monitoring**

**📱 Pour SLAM (Solutions Logicielles) :**
- Cette architecture = **Modern Development Stack**
- Codespaces = **Development environments**
- Git = **Source control et CI/CD**  
- Applications Python = **Business logic et services**

---

## 🚀 **PROCHAINS DÉFIS (Optionnels)**

### **🎯 Pour cette semaine :**

**Enrichir vos applications existantes :**

1. **presentation.py** → Ajouter sport favori, couleur préférée, calcul IMC
2. **calculatrice.py** → Ajouter puissance (x^y) et pourcentage  
3. **notes.py** → Calculer moyenne de plusieurs matières

**🆕 Nouveau défi architecture :**
```python
# Créer quiz_interactif.py
print("🧠 QUIZ ARCHITECTURE INFORMATIQUE")
score = 0

# Question 1
q1 = input("Que signifie 'Git' ? (A: Chat, B: Outil de versioning) : ")
if q1.upper() == "B":
    print("✅ Correct ! Git = outil de versioning")
    score += 1
else:
    print("❌ Faux, Git = outil de versioning")

# Question 2  
q2 = input("GitHub Codespaces s'exécute où ? (A: Sur votre PC, B: Dans le cloud) : ")
if q2.upper() == "B":
    print("✅ Correct ! Codespaces = cloud")
    score += 1
else:
    print("❌ Faux, Codespaces s'exécute dans le cloud")

print(f"\n🏆 Score final : {score}/2")
if score == 2:
    print("🎉 Parfait ! Vous maîtrisez l'architecture moderne !")
```

### **📚 Préparation TP suivant :**
- **Boucles for** : Automatiser des traitements répétitifs
- **Listes Python** : Gérer des collections de données
- **Fonctions** : Organiser et réutiliser votre code  
- **Fichiers** : Persistance des données (CSV, JSON)
- **APIs simples** : Récupérer des données externes

---

## 🎉 **FÉLICITATIONS !**

**En 1 heure, vous avez :**
- 🏗️ **Construit une architecture** de développement moderne et professionnelle
- ☁️ **Maîtrisé les outils cloud** : GitHub Codespaces comme environnement principal  
- 🐍 **Développé en Python** dans un contexte professionnel
- 🔄 **Implémenté un workflow Git** pour la sauvegarde et le versioning
- 💻 **Créé des applications interactives** avec validation et logique métier

**Vous développez maintenant avec les mêmes outils et méthodologies que les équipes techniques des grandes entreprises ! 🚀**

**🎯 Vous êtes prêts pour les architectures plus complexes : microservices, APIs, bases de données, déploiement automatique...** S` : Sauvegarder
- `F5` : Exécuter Python
- `Ctrl + `` ` : Ouvrir/fermer terminal

### **🐍 Python Essentiel**
```python
# Saisie utilisateur
nom = input("Question ? ")
age = int(input("Âge ? "))  # Pour un nombre entier
prix = float(input("Prix ? "))  # Pour un nombre décimal

# Conditions
if age >= 18:
    print("Majeur")
elif age >= 16:
    print("Presque majeur")  
else:
    print("Mineur")

# Formatage
print(f"Bonjour {nom}, tu as {age} ans")
```

### **📤 Git Essentiel**
```bash
git status      # Voir les changements
git add .       # Ajouter tous les fichiers
git commit -m "message"  # Sauvegarder avec message
git push        # Envoyer sur GitHub
```

---

## 🎉 **FÉLICITATIONS !**

**En 1 heure, vous avez :**
- 🛠️ Configuré un environnement de développement professionnel
- 🐍 Créé vos premières applications Python interactives
- 🧠 Maîtrisé les conditions intelligentes
- 💾 Appris à sauvegarder votre code comme un pro

**Vous êtes maintenant capable de développer en Python dans un environnement professionnel ! 🚀**

---

