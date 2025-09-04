# 📖 MÉMENTO PYTHON - TP 1 & TP 2
**Instructions Python Essentielles - Module B1.1**  
**Couverture :** TP 1.1 (Glot.io) + TP 2.1 (GitHub Codespaces)  
**Concepts :** Variables, Affichage, Saisie, Conditions, Formatage

---

## 🎯 **À PROPOS DE CE MÉMENTO**

### **📚 Objectif**
Référence rapide des **instructions Python vues dans les TP 1 et TP 2** :
- 📖 Retrouver une syntaxe rapidement
- 🔍 Aide-mémoire pendant les exercices  
- 💡 Inspiration pour nouveaux programmes
- 🎯 Révision avant évaluations

### **✅ Concepts Couverts**
- **TP 1.1** : Variables, print(), calculs, chaînes de base
- **TP 2.1** : input(), conditions if/elif/else, f-strings, try/except

---

## 🎯 **AFFICHAGE ET SAISIE**

### **📝 Afficher du Contenu (print)**
```python
# Affichage simple
print("Hello World")                    # Texte fixe
print("Bonjour le monde !")

# Afficher une variable
nom = "Alice"
print(nom)                              # Affiche : Alice

# Afficher texte + variable
print("Bonjour", nom)                   # Affiche : Bonjour Alice
print("Âge :", 25)                      # Affiche : Âge : 25

# Afficher un calcul
print("Résultat :", 15 + 3)            # Affiche : Résultat : 18
print(10 * 5)                           # Affiche : 50
```

### **🗣️ Saisie Utilisateur (input)**
```python
# Saisie de texte (défaut = chaîne de caractères)
nom = input("Votre nom ? ")
ville = input("Votre ville ? ")

# Saisie avec conversion en nombre
age = int(input("Votre âge ? "))        # Conversion en entier
prix = float(input("Prix ? "))          # Conversion en décimal

# Exemples d'utilisation
print(f"Bonjour {nom} de {ville}")
print(f"L'année prochaine, vous aurez {age + 1} ans")
```

---

## 📦 **VARIABLES ET TYPES**

### **🏷️ Déclaration de Variables**
```python
# Types de base rencontrés dans les TP
nom = "Alice"                           # str (texte)
age = 18                               # int (nombre entier)
taille = 1.75                          # float (nombre décimal)
majeur = True                          # bool (vrai/faux)

# Modification de variables
age = age + 1                          # Nouvelle valeur : 19
age += 1                               # Raccourci équivalent
```

### **🔄 Conversions de Types**
```python
# Conversions utilisées dans les TP
age_str = str(25)                      # 25 → "25"
nombre = int("18")                     # "18" → 18
prix = float("12.99")                  # "12.99" → 12.99

# Exemple concret des TP
age = int(input("Âge : "))             # Saisie → conversion
annee_naissance = 2024 - age           # Calcul avec le nombre
print("Né en " + str(annee_naissance)) # Conversion pour affichage
```

---

## 🔤 **MANIPULATION DES CHAÎNES**

### **🎨 Méthodes de Chaînes (TP 1)**
```python
nom = "alice"

# Modification de casse
nom.upper()                            # "ALICE"
nom.lower()                            # "alice"  
nom.title()                            # "Alice"
nom.capitalize()                       # "Alice"

# Exemple des TP
prenom = input("Prénom : ")
print(f"Bonjour {prenom.title()} !")   # Première lettre majuscule
```

### **✨ Formatage avec f-strings (TP 2)**
```python
# F-strings modernes (Python 3.6+)
nom = "Alice"
age = 20

# Syntaxe de base
print(f"Je m'appelle {nom}")           # "Je m'appelle Alice"
print(f"J'ai {age} ans")               # "J'ai 20 ans"

# Avec calculs
print(f"Dans 10 ans : {age + 10} ans") # "Dans 10 ans : 30 ans"

# Formatage numérique (TP 2)
prix = 12.6789
print(f"Prix : {prix:.2f} €")          # "Prix : 12.68 €" (2 décimales)
```

### **➕ Concaténation Classique (TP 1)**
```python
# Coller des chaînes avec +
prenom = "Alice"
nom = "Martin"
nom_complet = prenom + " " + nom        # "Alice Martin"

# Coller texte et variables
age = 20
message = "J'ai " + str(age) + " ans"   # "J'ai 20 ans"
# Note : str() nécessaire pour convertir le nombre
```

---

## 🧮 **CALCULS ET OPÉRATEURS**

### **📊 Opérateurs Arithmétiques**
```python
# Opérations de base utilisées dans les TP
a = 15
b = 4

a + b          # 19 (addition)
a - b          # 11 (soustraction)  
a * b          # 60 (multiplication)
a / b          # 3.75 (division)

# Exemples concrets des TP
prix_ht = 100
tva = prix_ht * 0.20              # 20.0 (calcul de TVA)
prix_ttc = prix_ht + tva          # 120.0 (prix final)

# Calculatrice des TP
nombre1 = float(input("Premier nombre : "))
nombre2 = float(input("Deuxième nombre : "))
resultat = nombre1 + nombre2
print(f"{nombre1} + {nombre2} = {resultat}")
```

### **🔄 Opérateurs d'Assignation**
```python
# Raccourcis utilisés dans les TP
score = 10
score += 5     # Équivaut à : score = score + 5  (résultat : 15)
score -= 2     # Équivaut à : score = score - 2  (résultat : 13)
score *= 2     # Équivaut à : score = score * 2  (résultat : 26)
```

---

## 🤔 **CONDITIONS (IF/ELIF/ELSE)**

### **⚖️ Opérateurs de Comparaison**
```python
# Comparaisons utilisées dans les TP
age = 18
note = 15

age >= 18      # True (majeur)
note < 10      # False (note correcte)
note != 20     # True (pas parfait)
nom == "Alice" # True si nom exactement "Alice"
```

### **🔗 Opérateurs Logiques**
```python
# Combinaisons logiques des TP
age >= 18 and note >= 10           # Majeur ET note correcte
jour == "samedi" or jour == "dimanche"  # Week-end
not (age < 18)                     # Équivaut à age >= 18
```

### **🎯 Structure IF simple**
```python
# Condition simple (TP 1 & 2)
if age >= 18:
    print("Vous êtes majeur")

# Avec alternative
if note >= 10:
    print("Admis")
else:
    print("Recalé")
```

### **📊 Structure IF/ELIF/ELSE (TP 2)**
```python
# Conditions en cascade (analyseur de notes TP 2)
note = float(input("Votre note /20 : "))

if note >= 16:
    mention = "Très bien"
    emoji = "🏆"
elif note >= 14:
    mention = "Bien"
    emoji = "💪"
elif note >= 12:
    mention = "Assez bien"
    emoji = "👍"
elif note >= 10:
    mention = "Passable"
    emoji = "✅"
else:
    mention = "Insuffisant"
    emoji = "❌"

print(f"Note : {note}/20 - {mention} {emoji}")
```

### **🧮 Calculatrice avec Conditions (TP 2)**
```python
# Structure de choix multiple
print("1. Addition (+)")
print("2. Soustraction (-)")
print("3. Multiplication (×)")
print("4. Division (÷)")

choix = input("Votre choix (1-4) : ")
nombre1 = float(input("Premier nombre : "))
nombre2 = float(input("Deuxième nombre : "))

if choix == "1":
    resultat = nombre1 + nombre2
    print(f"{nombre1} + {nombre2} = {resultat}")
elif choix == "2":
    resultat = nombre1 - nombre2
    print(f"{nombre1} - {nombre2} = {resultat}")
elif choix == "3":
    resultat = nombre1 * nombre2
    print(f"{nombre1} × {nombre2} = {resultat}")
elif choix == "4":
    if nombre2 != 0:  # Éviter division par zéro
        resultat = nombre1 / nombre2
        print(f"{nombre1} ÷ {nombre2} = {resultat}")
    else:
        print("❌ Division par zéro impossible !")
else:
    print("❌ Choix invalide !")
```

---

## 🛡️ **GESTION D'ERREURS SIMPLE**

### **⚠️ Try/Except de Base (TP 2)**
```python
# Gestion d'erreur pour saisie numérique
try:
    age = int(input("Votre âge : "))
    print(f"Vous avez {age} ans")
except ValueError:
    print("❌ Erreur : veuillez entrer un nombre")

# Validation avec conditions
try:
    note = float(input("Note /20 : "))
    if note < 0 or note > 20:
        print("❌ Note invalide (doit être entre 0 et 20)")
    else:
        print(f"✅ Note valide : {note}/20")
except ValueError:
    print("❌ Veuillez entrer un nombre")
```

---

## 🎯 **PATTERNS CONCRETS DES TP**

### **🎯 Présentation Interactive (TP 2)**
```python
# Pattern du TP 2.1 - Présentation
print("🎯 CRÉATEUR DE PRÉSENTATION")
print("=" * 30)

prenom = input("👤 Votre prénom : ")
age = int(input("🎂 Votre âge : "))
ville = input("🏠 Votre ville : ")

# Calculs automatiques
annee_naissance = 2024 - age
age_dans_10_ans = age + 10

# Affichage formaté
print(f"\n✨ VOTRE PRÉSENTATION :")
print(f"👋 Salut ! Je m'appelle {prenom.title()}")
print(f"🎂 J'ai {age} ans (né en {annee_naissance})")
print(f"🏠 Je vis à {ville.title()}")
print(f"🔮 Dans 10 ans, j'aurai {age_dans_10_ans} ans !")
```

### **💰 Calculateur de Prix (TP 1)**
```python
# Pattern du TP 1.1 - Calculateur
print("=== CALCULATEUR DE PRIX ===")

prix_stylo = 2
nombre_stylos = 4
total = prix_stylo * nombre_stylos

print("Prix d'un stylo : " + str(prix_stylo) + " euros")
print("Nombre de stylos : " + str(nombre_stylos))
print("Total à payer : " + str(total) + " euros")
```

### **🎓 Analyseur de Notes Intelligent (TP 2)**
```python
# Pattern du TP 2.1 - Analyse avec intelligence
print("🎓 ANALYSEUR DE NOTES")

try:
    note = float(input("📝 Votre note /20 : "))
    
    if note < 0 or note > 20:
        print("❌ Note invalide !")
    else:
        # Classification
        if note >= 16:
            print("🏆 Mention : TRÈS BIEN !")
            print("⭐ Excellent travail !")
        elif note >= 14:
            print("💪 Mention : BIEN")
            print("👍 Très bon niveau !")
        elif note >= 12:
            print("👌 Mention : ASSEZ BIEN")
            print("📚 Continuez vos efforts !")
        elif note >= 10:
            print("✅ Mention : PASSABLE")
            print("⚠️ Travaillez encore !")
        else:
            print("❌ Mention : INSUFFISANT")
            print("💪 Courage, reprenez les bases !")
        
        # Calcul bonus
        points_manquants = 20 - note
        if points_manquants > 0:
            print(f"🎯 Il vous manque {points_manquants} points pour 20/20")
            
except ValueError:
    print("❌ Veuillez entrer un nombre valide")
```

---

## 🔧 **AIDE-MÉMOIRE SYNTAXE**

### **🐍 Python Essentiel TP 1-2**
```python
# Variables
nom = "valeur"                    # Chaîne
nombre = 42                       # Entier  
decimal = 3.14                    # Décimal

# Affichage
print("texte")                    # Texte simple
print(variable)                   # Variable
print(f"Texte {variable}")        # F-string (TP 2)
print("Texte " + str(nombre))     # Concaténation (TP 1)

# Saisie
texte = input("Question ? ")      # Texte
nombre = int(input("Nombre ? "))  # Entier
decimal = float(input("Prix ? ")) # Décimal

# Conditions
if condition:
    print("Action")
elif autre_condition:
    print("Autre action")
else:
    print("Action par défaut")

# Gestion d'erreur
try:
    nombre = int(input("Nombre : "))
except ValueError:
    print("Erreur de saisie")
```

### **🎨 Applications Types**
```python
# 1. Calculatrice simple
a = float(input("Premier nombre : "))
b = float(input("Deuxième nombre : "))
print(f"Résultat : {a + b}")

# 2. Validation d'âge
age = int(input("Âge : "))
if age >= 18:
    print("Majeur")
else:
    print("Mineur")

# 3. Analyseur de note
note = float(input("Note : "))
if note >= 10:
    print("✅ Admis")
else:
    print("❌ Recalé")
```

---

## 🏆 **BONNES PRATIQUES TP 1-2**

### **✅ À Faire**
- **Noms clairs** : `age`, `prix_total`, `nom_utilisateur`
- **f-strings** : `f"Bonjour {nom}"` (TP 2)
- **Try/except** : Pour les saisies numériques (TP 2)
- **Conditions claires** : `if age >= 18:` plutôt que `if age > 17:`

### **❌ À Éviter**
- **Variables floues** : `a`, `x`, `truc`
- **Pas de validation** : `int(input())` sans try/except
- **Concaténation lourde** : `"J'ai " + str(age) + " ans"` 
  → Préférer : `f"J'ai {age} ans"`

---

## 🎯 **APPLICATIONS CRÉÉES DANS LES TP**

### **📋 TP 1.1 - Glot.io**
1. **Hello World tri-linguistique** 
2. **Carte de visite personnelle**
3. **Calculateur de prix simple**
4. **Présentation avec variables**

### **📋 TP 2.1 - Codespaces**
1. **Présentation interactive complète**
2. **Calculatrice intelligente 4 opérations**  
3. **Analyseur de notes avec mentions**
4. **Applications avec validation d'erreurs**

---

**📚 Ce mémento couvre TOUS les concepts Python des TP 1 et 2. Gardez-le à portée de main pour vos prochains développements ! 🚀**