# 🚀 TP 1.1 - Premiers Pas Tri-linguistiques
**Module B1.1 Algorithmique - Tronc Commun SISR/SLAM**  
**Durée :** 2h  
**Objectif :** Découvrir les bases dans les 3 langages par la pratique immédiate  
**Plateforme :** Glot.io (SANS INSTALLATION - Pratique directe !)

---

## 🎯 **OBJECTIFS DU TP**

À la fin de ce TP, vous saurez :
- ✅ Comprendre ce qu'est une variable
- ✅ Afficher du texte dans les 3 langages  
- ✅ Faire des calculs simples
- ✅ Créer des applications personnalisées
- ✅ Comparer Python, JavaScript et Java

---

## ⏰ **PLANNING SIMPLIFIÉ DU TP**

| **Temps** | **Activité** | **Objectif** |
|-----------|--------------|--------------|
| **0-20min** | Configuration + Premier contact avec les 3 langages | Hello World immédiat |
| **20-50min** | Variables et calculs très simples | Manipulation de données |
| **50-80min** | Messages personnalisés et combinaisons | Interaction simulée |
| **80-110min** | Mini-calculatrices utiles | Applications pratiques |
| **110-120min** | Comparaison et bilan | Réflexion critique |

**🎯 Objectif réaliste :**
- ✅ Comprendre ce qu'est une variable
- ✅ Afficher du texte dans les 3 langages
- ✅ Faire des calculs simples
- ✅ Créer des applications personnalisées

---

## 🌐 **ÉTAPE 1 : PREMIER CONTACT (20 min)**

### **🔧 Découverte de Glot.io**

1. **Ouvrir** https://glot.io/
2. **Créer 3 onglets** dans votre navigateur :
   - https://glot.io/new/python
   - https://glot.io/new/javascript  
   - https://glot.io/new/java

### **👋 Exercice 1.1 : Dire Bonjour**

**🐍 ÉTAPE 1 - Dans l'onglet Python :**

1. **Allez** dans votre onglet Python (https://glot.io/new/python)
2. **Effacez** tout ce qui est déjà écrit dans la zone de code
3. **Tapez EXACTEMENT** cette ligne (respectez les guillemets) :

```python
print("Bonjour le monde !")
```

4. **Cliquez** sur le bouton vert "Run" en haut à droite
5. **Regardez** la zone du bas : vous devez voir "Bonjour le monde !"
6. **Si ça marche** : 🎉 BRAVO ! Vous venez de créer votre premier programme !
7. **Si ça ne marche pas** : vérifiez les guillemets " et les parenthèses ( )

---

**🌐 ÉTAPE 2 - Dans l'onglet JavaScript :**

1. **Allez** dans votre onglet JavaScript (https://glot.io/new/javascript)
2. **Effacez** tout ce qui est déjà écrit
3. **Tapez EXACTEMENT** cette ligne :

```javascript
console.log("Bonjour le monde !");
```

4. **Cliquez** sur "Run"
5. **Regardez** en bas : même résultat qu'en Python !
6. **Observation** : le résultat est identique, mais on écrit `console.log` au lieu de `print`

---

**☕ ÉTAPE 3 - Dans l'onglet Java :**

1. **Allez** dans votre onglet Java (https://glot.io/new/java)
2. **Effacez** tout et **tapez EXACTEMENT** ce code (attention aux majuscules) :

```java
public class Bonjour {
    public static void main(String[] args) {
        System.out.println("Bonjour le monde !");
    }
}
```

3. **Cliquez** sur "Run"
4. **Regardez** : encore le même résultat !
5. **Observation** : Java est plus compliqué à écrire, mais fait la même chose

**✅ VALIDATION :** Vous devez avoir "Bonjour le monde !" qui s'affiche dans les 3 onglets

**🤔 Première observation :** Lequel vous semble le plus simple ? Pourquoi ?

---

### **👋 Exercice 1.2 : Afficher Plusieurs Messages**

**🎯 Objectif :** Apprendre à afficher plusieurs lignes de texte

**🐍 ÉTAPE 1 - Python :**

1. **Dans votre onglet Python**, effacez l'ancien code
2. **Tapez EXACTEMENT** ces 3 lignes (une par une) :

```python
print("Je m'appelle Alice")
print("J'apprends la programmation")  
print("C'est parti !")
```

3. **Cliquez** sur "Run"
4. **Vérifiez** : vous devez voir 3 lignes qui s'affichent

**✏️ PERSONNALISATION OBLIGATOIRE :**
- **Remplacez** "Alice" par **VOTRE VRAI PRÉNOM**
- **Cliquez** sur "Run" à nouveau
- **Résultat attendu** : l'ordinateur affiche VOTRE prénom !

---

**🌐 ÉTAPE 2 - JavaScript :**

1. **Dans votre onglet JavaScript**, effacez tout
2. **Tapez** ces 3 lignes :

```javascript
console.log("Je m'appelle Alice");
console.log("J'apprends la programmation");
console.log("C'est parti !");
```

3. **Remplacez** "Alice" par votre prénom
4. **Cliquez** sur "Run"
5. **Observez** : même résultat qu'en Python !

---

**☕ ÉTAPE 3 - Java :**

1. **Dans votre onglet Java**, remplacez tout par :

```java
public class Messages {
    public static void main(String[] args) {
        System.out.println("Je m'appelle Alice");
        System.out.println("J'apprends la programmation");
        System.out.println("C'est parti !");
    }
}
```

2. **Remplacez** "Alice" par votre prénom
3. **Cliquez** sur "Run"

**✅ VALIDATION :** Votre prénom s'affiche dans les 3 langages

**🤔 RÉFLEXION :** Quel langage vous semble le plus simple pour écrire plusieurs messages ?

---

### **👋 Exercice 1.3 : Messages Créatifs**

**🎯 Objectif :** S'amuser avec l'affichage de texte

**✏️ MISSION :** Créez votre carte de visite personnelle !

**🐍 Python - Exemple à adapter :**

```python
print("=== MA CARTE DE VISITE ===")
print("Prénom : Alice")
print("Âge : 18 ans")
print("Passion : Informatique")
print("=========================")
```

**🎨 À PERSONNALISER :**
1. **Remplacez** "Alice" par votre prénom
2. **Remplacez** "18" par votre âge réel
3. **Remplacez** "Informatique" par votre vraie passion
4. **Testez** en cliquant "Run"

**🌐 JavaScript - Faites pareil :**

```javascript
console.log("=== MA CARTE DE VISITE ===");
console.log("Prénom : Alice");
console.log("Âge : 18 ans");  
console.log("Passion : Informatique");
console.log("=========================");
```

**☕ Java - Version complète :**

```java
public class CarteVisite {
    public static void main(String[] args) {
        System.out.println("=== MA CARTE DE VISITE ===");
        System.out.println("Prénom : Alice");
        System.out.println("Âge : 18 ans");
        System.out.println("Passion : Informatique");
        System.out.println("=========================");
    }
}
```

**🎯 DÉFI BONUS :** Ajoutez une 4ème ligne avec votre ville !

**✅ VALIDATION :** Vous avez créé 3 cartes de visite personnalisées

---

## 📦 **ÉTAPE 2 : LES VARIABLES - MES PREMIÈRES BOÎTES (30 min)**

### **💡 EXPLICATION SIMPLE : Qu'est-ce qu'une Variable ?**

**Imaginez votre casier au lycée :**
- 🏷️ **Numéro du casier** = nom de la variable (exemple: `prenom`)
- 📦 **Ce qu'il y a dedans** = valeur de la variable (exemple: `"Alice"`)

**En programmation :**
- On **crée une boîte** avec un nom : `prenom`
- On **met quelque chose dedans** : `"Alice"`
- On **peut regarder ce qu'il y a dedans** : `print(prenom)`

---

### **📝 Exercice 2.1 : Ma Première Boîte (Variable)**

**🎯 Objectif :** Comprendre comment ranger une information

**🐍 ÉTAPE 1 - Python :**

1. **Effacez** votre ancien code Python
2. **Tapez EXACTEMENT** ces 2 lignes :

```python
prenom = "Alice"
print(prenom)
```

3. **Cliquez** "Run"
4. **Observez** : "Alice" s'affiche !
5. **Explication** :
   - Ligne 1 : on crée une boîte nommée `prenom` et on met "Alice" dedans
   - Ligne 2 : on demande d'afficher ce qu'il y a dans la boîte `prenom`

**✏️ PERSONNALISATION OBLIGATOIRE :**
1. **Remplacez** "Alice" par **VOTRE PRÉNOM** (gardez les guillemets !)
2. **Cliquez** "Run"  
3. **Magie** : l'ordinateur affiche VOTRE prénom !

---

**🌐 ÉTAPE 2 - JavaScript :**

1. **Dans JavaScript**, tapez :

```javascript
let prenom = "Alice";
console.log(prenom);
```

2. **Remplacez** "Alice" par votre prénom
3. **Testez** avec "Run"
4. **Différence observée** : on écrit `let prenom` au lieu de juste `prenom`

---

**☕ ÉTAPE 3 - Java :**

```java
public class Variable {
    public static void main(String[] args) {
        String prenom = "Alice";
        System.out.println(prenom);
    }
}
```

1. **Remplacez** "Alice" par votre prénom
2. **Testez**
3. **Différence** : on écrit `String prenom` (String = texte en Java)

**✅ VALIDATION :** Votre prénom s'affiche dans les 3 langages grâce aux variables

**🤔 COMPRÉHENSION :** Pouvez-vous expliquer avec vos mots ce qu'est une variable ?

---

### **📝 Exercice 2.2 : Plusieurs Boîtes**

**🎯 Objectif :** Créer plusieurs variables et les utiliser

**🐍 Python - Instructions détaillées :**

1. **Effacez** votre code Python
2. **Tapez** ces lignes **UNE PAR UNE** (en vérifiant chaque fois) :

```python
prenom = "Alice"
age = 18
ville = "Paris"
```

3. **Maintenant ajoutez** ces lignes d'affichage :

```python
print(prenom)
print(age)
print(ville)
```

4. **Cliquez** "Run"
5. **Résultat** : vous devez voir 3 lignes qui s'affichent

**✏️ PERSONNALISATION COMPLÈTE :**
- Remplacez "Alice" par votre prénom  
- Remplacez 18 par votre âge RÉEL (sans guillemets pour les nombres !)
- Remplacez "Paris" par votre vraie ville
- **Testez** le résultat

**📋 OBSERVATION IMPORTANTE :**
- **Texte** : avec guillemets → `"Alice"`, `"Paris"`
- **Nombres** : sans guillemets → `18`, `20`

---

**🌐 JavaScript :**

```javascript
let prenom = "Alice";
let age = 18;
let ville = "Paris";

console.log(prenom);
console.log(age);
console.log(ville);
```

**Personnalisez avec VOS vraies informations !**

---

**☕ Java :**

```java
public class PlusieursVariables {
    public static void main(String[] args) {
        String prenom = "Alice";
        int age = 18;
        String ville = "Paris";
        
        System.out.println(prenom);
        System.out.println(age);
        System.out.println(ville);
    }
}
```

**Personnalisez avec VOS informations !**

**✅ VALIDATION :** Vos vraies informations s'affichent dans les 3 langages

---

### **📝 Exercice 2.3 : Coller du Texte et des Variables**

**🎯 Objectif :** Combiner du texte fixe et des variables

**💡 CONCEPT :** On peut "coller" du texte et des variables avec le signe `+`

**🐍 Python - Étape par étape :**

1. **Commencez** par créer votre variable :

```python
prenom = "Alice"
```

2. **Ajoutez** cette ligne magique :

```python
print("Bonjour " + prenom)
```

3. **Testez** avec "Run"
4. **Résultat** : "Bonjour Alice"
5. **Remplacez** "Alice" par votre prénom et retestez

**✏️ EXPÉRIMENTEZ :** Essayez ces variations :

```python
prenom = "VotrePrenom"
print("Salut " + prenom + " !")
print("Comment ça va " + prenom + " ?")
print("À bientôt " + prenom + " !")
```

---

**🌐 JavaScript :**

```javascript
let prenom = "Alice";
console.log("Bonjour " + prenom);
console.log("Salut " + prenom + " !");
```

**☕ Java :**

```java
public class Combinaison {
    public static void main(String[] args) {
        String prenom = "Alice";
        System.out.println("Bonjour " + prenom);
        System.out.println("Salut " + prenom + " !");
    }
}
```

**🎯 MISSION CRÉATIVE :** Créez 3 messages différents avec votre prénom !

**✅ VALIDATION :** Vous savez combiner texte et variables

---

## ➕ **ÉTAPE 3 : MES PREMIERS CALCULS (30 min)**

### **💡 CONCEPT : L'Ordinateur = Super Calculatrice**

**L'ordinateur peut faire des calculs ET se souvenir du résultat !**
- `+` pour additionner
- `-` pour soustraire  
- `*` pour multiplier
- `/` pour diviser

---

### **➕ Exercice 3.1 : Addition Basique**

**🎯 Objectif :** Faire calculer 10 + 5 par l'ordinateur

**🐍 Python - Instructions détaillées :**

1. **Effacez** votre ancien code
2. **Tapez** ligne par ligne :

```python
nombre1 = 10
nombre2 = 5
resultat = nombre1 + nombre2
print(resultat)
```

3. **Cliquez** "Run"
4. **Résultat attendu :** 15
5. **Explication** :
   - Ligne 1 : on met 10 dans une boîte nommée `nombre1`
   - Ligne 2 : on met 5 dans une boîte nommée `nombre2`
   - Ligne 3 : on additionne les deux et on met le résultat dans `resultat`
   - Ligne 4 : on affiche le résultat

**✏️ EXPÉRIMENTEZ :**
- Changez 10 par 25
- Changez 5 par 17  
- Quelle est la nouvelle réponse ?

---

**🌐 JavaScript :**

```javascript
let nombre1 = 10;
let nombre2 = 5;
let resultat = nombre1 + nombre2;
console.log(resultat);
```

**☕ Java :**

```java
public class Addition {
    public static void main(String[] args) {
        int nombre1 = 10;
        int nombre2 = 5;
        int resultat = nombre1 + nombre2;
        System.out.println(resultat);
    }
}
```

**✅ VALIDATION :** Vous obtenez 15 dans les 3 langages

---

### **➖ Exercice 3.2 : Autres Opérations**

**🎯 Objectif :** Tester soustraction, multiplication, division

**🐍 Python - Testez chaque opération :**

**SOUSTRACTION :**

```python
nombre1 = 20
nombre2 = 8
resultat = nombre1 - nombre2
print("20 - 8 = " + str(resultat))
```

**MULTIPLICATION :**

```python
nombre1 = 6
nombre2 = 7
resultat = nombre1 * nombre2
print("6 × 7 = " + str(resultat))
```

**DIVISION :**

```python
nombre1 = 15
nombre2 = 3
resultat = nombre1 / nombre2
print("15 ÷ 3 = " + str(resultat))
```

**✏️ MISSION :** Testez chaque opération et vérifiez mentalement !

---

**🌐 JavaScript - Même principe :**

```javascript
let nombre1 = 20;
let nombre2 = 8;
let resultat = nombre1 - nombre2;
console.log("20 - 8 = " + resultat);
```

**☕ Java - Version complète :**

```java
public class Operations {
    public static void main(String[] args) {
        int nombre1 = 20;
        int nombre2 = 8;
        int resultat = nombre1 - nombre2;
        System.out.println("20 - 8 = " + resultat);
    }
}
```

**🧮 DÉFI :** Calculez votre âge dans 10 ans !

**✅ VALIDATION :** Vous maîtrisez les 4 opérations de base

---

### **💰 Exercice 3.3 : Calculateur de Prix**

**🎯 Objectif :** Créer un vrai calculateur utile !

**📋 MISSION :** Vous achetez 4 stylos à 2€ pièce. Combien payez-vous ?

**🐍 Python - Construction guidée :**

**ÉTAPE 1 :** Créez vos données

```python
prix_stylo = 2
nombre_stylos = 4
```

**ÉTAPE 2 :** Calculez le total

```python
total = prix_stylo * nombre_stylos
```

**ÉTAPE 3 :** Affichez joliment

```python
print("=== CALCULATEUR DE PRIX ===")
print("Prix d'un stylo : " + str(prix_stylo) + " euros")
print("Nombre de stylos : " + str(nombre_stylos))
print("Total à payer : " + str(total) + " euros")
```

**ÉTAPE 4 :** Testez avec "Run"

**✏️ EXPÉRIMENTEZ :**
- Changez le prix : 3€ le stylo
- Changez la quantité : 7 stylos
- Quel est le nouveau total ?

---

**🌐 JavaScript :**

```javascript
let prix_stylo = 2;
let nombre_stylos = 4;
let total = prix_stylo * nombre_stylos;

console.log("=== CALCULATEUR DE PRIX ===");
console.log("Prix d'un stylo : " + prix_stylo + " euros");
console.log("Nombre de stylos : " + nombre_stylos);
console.log("Total à payer : " + total + " euros");
```

**☕ Java :**

```java
public class CalculateurPrix {
    public static void main(String[] args) {
        int prix_stylo = 2;
        int nombre_stylos = 4;
        int total = prix_stylo * nombre_stylos;
        
        System.out.println("=== CALCULATEUR DE PRIX ===");
        System.out.println("Prix d'un stylo : " + prix_stylo + " euros");
        System.out.println("Nombre de stylos : " + nombre_stylos);
        System.out.println("Total à payer : " + total + " euros");
    }
}
```

**🎯 DÉFIS BONUS :**
- Calculateur pour des pizzas à 12€
- Calculateur pour des livres à 15€  
- Votre propre exemple !

**✅ VALIDATION :** Vous avez créé votre premier calculateur utile !

---

## 🧮 **ÉTAPE 4 : MINI-CALCULATRICES MÉTIER (30 min)**

### **💻 Exercice 4.1 : Calculateur SISR - Bande Passante**

**🎯 Mission :** Calculer la bande passante réseau nécessaire

**🐍 Python - Calculateur réseau :**

```python
print("=== CALCULATEUR BANDE PASSANTE SISR ===")

# Données d'entrée (à personnaliser !)
nombre_utilisateurs = 50
bande_par_utilisateur = 2  # Mbps par utilisateur

# Calculs
bande_totale = nombre_utilisateurs * bande_par_utilisateur

# Calculs avancés  
facteur_pic = 1.5  # pic de charge
bande_pic = bande_totale * facteur_pic

print("📊 RÉSULTATS :")
print("Utilisateurs : " + str(nombre_utilisateurs))
print("Bande par utilisateur : " + str(bande_par_utilisateur) + " Mbps")
print("Bande totale : " + str(bande_totale) + " Mbps")
print("Avec pics de charge : " + str(int(bande_pic)) + " Mbps")

# Recommandation
if bande_pic < 100:
    print("✅ Configuration standard suffisante")
else:
    print("⚠️ Infrastructure renforcée recommandée")
```

**✏️ EXPÉRIMENTEZ :**
- Changez le nombre d'utilisateurs : 100, 200
- Changez la bande par utilisateur : 5 Mbps
- Observez l'impact sur les recommandations

---

**🌐 JavaScript :**

```javascript
console.log("=== CALCULATEUR BANDE PASSANTE SISR ===");

// Données d'entrée
let nombre_utilisateurs = 50;
let bande_par_utilisateur = 2; // Mbps

// Calculs
let bande_totale = nombre_utilisateurs * bande_par_utilisateur;
let facteur_pic = 1.5;
let bande_pic = bande_totale * facteur_pic;

console.log("📊 RÉSULTATS :");
console.log("Utilisateurs : " + nombre_utilisateurs);
console.log("Bande par utilisateur : " + bande_par_utilisateur + " Mbps");
console.log("Bande totale : " + bande_totale + " Mbps");
console.log("Avec pics : " + Math.round(bande_pic) + " Mbps");

if (bande_pic < 100) {
    console.log("✅ Configuration standard suffisante");
} else {
    console.log("⚠️ Infrastructure renforcée recommandée");
}
```

**☕ Java :**

```java
public class CalculateurSISR {
    public static void main(String[] args) {
        System.out.println("=== CALCULATEUR BANDE PASSANTE SISR ===");
        
        // Données d'entrée
        int nombreUtilisateurs = 50;
        int bandeParUtilisateur = 2; // Mbps
        
        // Calculs
        int bandeTotale = nombreUtilisateurs * bandeParUtilisateur;
        double facteurPic = 1.5;
        double bandePic = bandeTotale * facteurPic;
        
        System.out.println("📊 RÉSULTATS :");
        System.out.println("Utilisateurs : " + nombreUtilisateurs);
        System.out.println("Bande par utilisateur : " + bandeParUtilisateur + " Mbps");
        System.out.println("Bande totale : " + bandeTotale + " Mbps");
        System.out.println("Avec pics : " + Math.round(bandePic) + " Mbps");
        
        if (bandePic < 100) {
            System.out.println("✅ Configuration standard suffisante");
        } else {
            System.out.println("⚠️ Infrastructure renforcée recommandée");
        }
    }
}
```

---

### **📱 Exercice 4.2 : Calculateur SLAM - Prix TTC**

**🎯 Mission :** Calculer des prix avec TVA et remises

**🐍 Python - Calculateur métier :**

```python
print("=== CALCULATEUR PRIX TTC SLAM ===")

# Données produit (à personnaliser !)
prix_ht = 100      # euros HT
quantite = 3       # articles
taux_tva = 0.20    # 20%

# Calculs de base
sous_total_ht = prix_ht * quantite

# Remise selon quantité
if quantite >= 5:
    taux_remise = 0.10  # 10%
    remise = sous_total_ht * taux_remise
    print("🎉 Remise de 10% appliquée !")
else:
    remise = 0

# Calculs finaux  
total_ht_apres_remise = sous_total_ht - remise
tva = total_ht_apres_remise * taux_tva
prix_ttc = total_ht_apres_remise + tva

print("💰 DÉTAIL DU CALCUL :")
print("Prix unitaire HT : " + str(prix_ht) + " €")
print("Quantité : " + str(quantite))
print("Sous-total HT : " + str(sous_total_ht) + " €")
print("Remise : " + str(remise) + " €")
print("Total HT après remise : " + str(total_ht_apres_remise) + " €")
print("TVA (20%) : " + str(tva) + " €")
print("═" * 30)
print("PRIX TTC FINAL : " + str(prix_ttc) + " €")
```

**✏️ EXPÉRIMENTEZ :**
- Changez la quantité à 6 pour voir la remise s'appliquer
- Testez avec différents prix unitaires
- Observez l'impact de la remise sur le prix final

---

**🌐 JavaScript :**

```javascript
console.log("=== CALCULATEUR PRIX TTC SLAM ===");

// Données produit
let prix_ht = 100;
let quantite = 3;
let taux_tva = 0.20;

// Calculs
let sous_total_ht = prix_ht * quantite;
let remise = 0;

if (quantite >= 5) {
    remise = sous_total_ht * 0.10;
    console.log("🎉 Remise de 10% appliquée !");
}

let total_ht_apres_remise = sous_total_ht - remise;
let tva = total_ht_apres_remise * taux_tva;
let prix_ttc = total_ht_apres_remise + tva;

console.log("💰 DÉTAIL DU CALCUL :");
console.log("Prix unitaire HT : " + prix_ht + " €");
console.log("Quantité : " + quantite);
console.log("Sous-total HT : " + sous_total_ht + " €");
console.log("Remise : " + remise + " €");
console.log("TVA (20%) : " + tva.toFixed(2) + " €");
console.log("PRIX TTC FINAL : " + prix_ttc.toFixed(2) + " €");
```

**☕ Java :**

```java
public class CalculateurSLAM {
    public static void main(String[] args) {
        System.out.println("=== CALCULATEUR PRIX TTC SLAM ===");
        
        // Données produit
        double prixHT = 100.0;
        int quantite = 3;
        double tauxTVA = 0.20;
        
        // Calculs
        double sousTotalHT = prixHT * quantite;
        double remise = 0;
        
        if (quantite >= 5) {
            remise = sousTotalHT * 0.10;
            System.out.println("🎉 Remise de 10% appliquée !");
        }
        
        double totalHTApresRemise = sousTotalHT - remise;
        double tva = totalHTApresRemise * tauxTVA;
        double prixTTC = totalHTApresRemise + tva;
        
        System.out.println("💰 DÉTAIL DU CALCUL :");
        System.out.println("Prix unitaire HT : " + prixHT + " €");
        System.out.println("Quantité : " + quantite);
        System.out.println("Sous-total HT : " + sousTotalHT + " €");
        System.out.println("Remise : " + remise + " €");
        System.out.printf("TVA (20%%) : %.2f €%n", tva);
        System.out.printf("PRIX TTC FINAL : %.2f €%n", prixTTC);
    }
}
```

---

## 🔍 **ÉTAPE 5 : COMPARAISON ET BILAN (15 min)**

### **📊 Mon Tableau de Comparaison Personnel**

**Complétez selon VOTRE expérience :**

| **Critère** | **🐍 Python** | **🌐 JavaScript** | **☕ Java** | **Mon Préféré** |
|-------------|---------------|------------------|-------------|-----------------|
| **Facilité d'écriture** | Facile/Moyen/Dur | Facile/Moyen/Dur | Facile/Moyen/Dur | _______ |
| **Lisibilité du code** | Claire/Moyenne/Confuse | Claire/Moyenne/Confuse | Claire/Moyenne/Confuse | _______ |
| **Longueur du code** | Court/Moyen/Long | Court/Moyen/Long | Court/Moyen/Long | _______ |
| **Plaisir à utiliser** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | _______ |

### **🤔 Mes Réflexions Personnelles**

**Complétez ces phrases honnêtement :**

1. **Le langage le plus SIMPLE pour moi :** ________________  
   **Pourquoi ?** ________________________________________________

2. **Le langage le plus COMPLIQUÉ :** ________________  
   **Pourquoi ?** ________________________________________________

3. **Pour un site web, je choisirais :** ________________  
   **Pourquoi ?** ________________________________________________

4. **Pour un script rapide, je choisirais :** ________________  
   **Pourquoi ?** ________________________________________________

5. **Mon erreur la plus fréquente :** ________________________________________________

6. **Ce que j'ai trouvé le plus cool :** ________________________________________________

### **✅ Ce que JE Sais Faire Maintenant**

**Cochez HONNÊTEMENT vos acquis :**

#### **🎯 Compétences de Base**
- [ ] Je sais afficher du texte dans les 3 langages
- [ ] Je sais créer une variable avec mon prénom  
- [ ] Je sais faire des calculs simples (+, -, ×, ÷)
- [ ] Je sais combiner du texte et des nombres
- [ ] Je comprends le principe des variables

#### **🔧 Compétences Techniques**
- [ ] Je sais corriger une erreur de guillemets
- [ ] Je sais corriger une erreur de parenthèses
- [ ] Je peux expliquer ce que fait mon programme
- [ ] Je peux modifier les valeurs dans mon programme
- [ ] Je peux personnaliser un programme existant

#### **🎨 Compétences Créatives**
- [ ] J'ai créé au moins 1 programme personnalisé
- [ ] J'ai testé des variantes de mes programmes
- [ ] J'ai aidé un camarade avec son code
- [ ] J'ai eu des idées d'améliorations
- [ ] J'ai pris plaisir à programmer

### **🏆 Mon Programme Favori du Jour**

**Copiez ici le programme que vous avez préféré créer :**

```
(Votre programme favori)
```

**Pourquoi ce programme vous a plu ?**
________________________________________________
________________________________________________

### **🎯 Mes Objectifs pour la Suite**

**Qu'aimeriez-vous apprendre la semaine prochaine ?**

- [ ] Comment poser de vraies questions à l'utilisateur
- [ ] Comment faire des choix ("si... alors...")
- [ ] Comment répéter une action plusieurs fois
- [ ] Comment gérer une liste de données
- [ ] Comment créer de jolies interfaces
- [ ] Autre : ________________________________

### **📈 Mes Statistiques du Jour**

**Comptez et notez :**
- **Programmes écrits au total :** _____ programmes
- **Erreurs corrigées avec succès :** _____ erreurs
- **Fois où j'ai aidé quelqu'un :** _____ fois
- **Fois où j'ai été aidé(e) :** _____ fois  
- **Programmes entièrement personnalisés :** _____ programmes

### **💪 Mon Engagement Personnel**

**Complétez :**  
*"Cette semaine, je m'engage à programmer _____ minutes par jour pour améliorer _________________."*

---

## 🎉 **FÉLICITATIONS ! Votre Premier Jour Tri-linguistique !**

### **🏆 Ce Que Vous Avez Accompli**

- **15+ programmes fonctionnels** dans 3 langages différents
- **Concepts maîtrisés** : variables, calculs, affichage, personnalisation
- **Applications créées** : calculatrices, analyseurs, gestionnaires personnels
- **Première expérience** du débogage et correction d'erreurs
- **Vision comparative** des langages de programmation

### **🌟 Vous Êtes Maintenant...**

- **💻 Développeurs tri-linguistiques** : vous codez en Python, JavaScript ET Java !
- **🔧 Créateurs d'applications** : vos calculatrices sont vraiment utiles
- **🧠 Penseurs algorithmiques** : vous décomposez les problèmes en étapes
- **🐛 Chasseurs de bugs** : vous savez identifier et corriger les erreurs
- **🎨 Innovateurs créatifs** : vous personnalisez et améliorez vos créations

### **🚀 Pour Continuer à Progresser**

**Cette semaine :**
- **Expérimentez** 10-15 minutes par jour sur Glot.io
- **Modifiez** vos programmes avec de nouvelles valeurs
- **Créez** vos propres calculatrices personnelles
- **Montrez** à vos amis/famille ce que vous savez faire

**La semaine prochaine (TP 2) :**
- **GitHub Codespaces** avec VS Code professionnel
- **Python approfondi** avec un environnement complet
- **Conditions intelligentes** ("si... alors... sinon...")
- **Interactions réelles** avec l'utilisateur
- **Debugging avancé** avec les outils professionnels

### **💝 Message Final**

*"La programmation s'apprend en programmant. N'ayez jamais peur d'essayer, de modifier, de 'casser' vos programmes pour comprendre. C'est exactement comme ça que progressent tous les développeurs du monde ! Vous avez franchi la barrière la plus difficile : le premier pas. Désormais, vous savez que vous POUVEZ programmer dans 3 langages différents !"*

---

## 🆘 **AIDE-MÉMOIRE DE SURVIE**

### **🐛 Si ça ne marche pas...**

**🐍 Python :**
```python
# ❌ Erreur fréquente
print(Bonjour)  # Oubli des guillemets

# ✅ Correct  
print("Bonjour")  # Avec les guillemets
```

**🌐 JavaScript :**
```javascript
// ❌ Erreur fréquente
console.log(Bonjour)  // Oubli des guillemets

// ✅ Correct
console.log("Bonjour");  // Avec guillemets
```

**☕ Java :**
```java
// ❌ Erreur fréquente
public class test {  // Minuscule = erreur

// ✅ Correct
public class Test {  // Majuscule obligatoire
```

### **🔑 Mots-clés à Retenir**

- **Variable** : boîte pour ranger une information
- **Print/console.log** : afficher à l'écran
- **String/texte** : avec guillemets `"Alice"`
- **Number/int** : nombre sans guillemets `18`
- **Calcul** : `+` `-` `*` `/` pour les opérations

### **📚 Ressources pour Continuer**

- **Glot.io** : https://glot.io/ (pour continuer à coder)
- **Prochaine séance** : GitHub Codespaces + Python approfondi
- **Objectif** : devenir autonome dans les 3 langages !

---

## 📖 **LEXIQUE & AIDE-MÉMOIRE**

### **Lexique des concepts**
- **Variable** : boîte pour stocker une information (ex : prénom, âge)
- **Affichage** : commande pour montrer un message à l'écran (print, console.log)  
- **Concaténation** : coller du texte et des variables pour former une phrase
- **Opérateur arithmétique** : symbole pour calculer (+, -, *, /)
- **Instruction** : ligne de code qui donne un ordre à l'ordinateur
- **Programme** : suite d'instructions qui réalisent une tâche

### **Syntaxes de base**

**🐍 Python :**
```python
# Affichage
print("message")

# Variable
nom = "valeur"

# Calcul
resultat = nombre1 + nombre2
```

**🌐 JavaScript :**
```javascript
// Affichage
console.log("message");

// Variable  
let nom = "valeur";

// Calcul
let resultat = nombre1 + nombre2;
```

**☕ Java :**
```java
public class MonProgramme {
    public static void main(String[] args) {
        // Affichage
        System.out.println("message");
        
        // Variable
        String nom = "valeur";
        int nombre = 42;
        
        // Calcul
        int resultat = nombre1 + nombre2;
    }
}
```

---

**Keep Coding! 🚀💻✨**
