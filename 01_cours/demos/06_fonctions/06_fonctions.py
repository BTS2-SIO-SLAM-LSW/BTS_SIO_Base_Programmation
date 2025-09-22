# ================================================================
# COURS : LES FONCTIONS EN PYTHON
# ================================================================
# Une fonction permet de regrouper des instructions réutilisables.
# On peut l’appeler plusieurs fois sans réécrire le code.
# ================================================================

# 1) Définir une fonction simple
# ------------------------------------------------
# - On utilise le mot-clé def
# - On doit respecter l'indentation (très importante en Python !)
def fonction_basic():
    print("Hello World")

fonction_basic()  # appel de la fonction


# 2) Fonctions avec paramètres
# ------------------------------------------------
# - On peut passer des valeurs à une fonction
# - On peut donner une valeur par défaut
def afficher_message(number=5):  # ici number vaut 5 par défaut
    for _ in range(0, number):
        print("Hello World")

afficher_message()       # utilisera la valeur par défaut (5)
afficher_message(3)      # affichera 3 fois


# 3) Retourner une valeur avec return
# ------------------------------------------------
# - return renvoie un résultat que l’on peut stocker
def addition(a, b):
    return a + b

resultat = addition(2, 8)
print("Résultat de l’addition :", resultat)


# 4) Typage des fonctions
# ------------------------------------------------
# Python est faiblement typé : inutile de préciser les types.
# MAIS on peut donner des indications (annotations).
def multiplication(a: int, b: int) -> int:
    return a * b

print(multiplication(4, 6))  # fonctionne normalement


# 5) Variables locales et globales
# ------------------------------------------------
# - Variables locales : créées dans la fonction, visibles uniquement dedans
# - Variables globales : définies hors des fonctions, visibles partout
def increment(a, b):
    a += 1
    b += 1
    print("Dans la fonction :", a, b)

nombre_a = 5
nombre_b = 8
print("Avant appel :", nombre_a, nombre_b)
increment(nombre_a, nombre_b)
print("Après appel :", nombre_a, nombre_b)  # pas modifiés (locales)


# 6) Modifier des variables globales dans une fonction
# ------------------------------------------------
# - Il faut utiliser le mot-clé global
def increment_global():
    global nombre_c
    nombre_c += 1

nombre_c = 10
increment_global()
print("Valeur globale après appel :", nombre_c)


# 7) Déclarer une variable globale à l’intérieur d’une fonction
def nouvelle_fonction():
    global ma_variable
    ma_variable = "Créée dans la fonction"

nouvelle_fonction()
print(ma_variable)  # existe maintenant partout








# 8) Arguments positionnels , Arguments nommés , Arguments variables (*args et **kwargs)
# ---------------------------------------------------------------------------------------

# Arguments POSITIONNELS
# -> La correspondance se fait par l'ORDRE des paramètres.
def addition(a, b):
    return a + b

print("1) Positionnels :", addition(5, 3))  # 5 -> a, 3 -> b

# Arguments NOMMÉS (a.k.a. "arguments mot-clé")
# -> On précise param=valeur, l'ordre n'a plus d'importance.
def presentation(nom, age):
    print(f"2) Nommés : Je m'appelle {nom} et j'ai {age} ans.")

presentation(nom="Alice", age=25)
presentation(age=40, nom="Bob")  # ordre inversé possible car on nomme

# VALEURS PAR DÉFAUT
# -> Utile pour rendre des paramètres optionnels
def facture(numero, montant, devise="€"):
    print(f"3) Facture {numero} : {montant} {devise}")

facture(101, 250)                 # devise prend "€" par défaut
facture(102, 120, "$")            # on remplace la valeur par défaut
facture(numero=103, montant=500)  # mélange avec arguments nommés

# MÉLANGE positionnels + nommés
# RÈGLE: les positionnels DOIVENT venir AVANT les nommés.
def email(destinataire, sujet, corps, signature="-- Équipe Support"):
    print("4) Email ->", destinataire, "|", sujet, "|", corps, "|", signature)

email("client@ex.com", "Bienvenue", "Merci de votre inscription.")
email("client@ex.com", "Info", corps="Votre facture est prête.")  # nommer après les 2 premiers
email("client@ex.com", sujet="Relance", corps="Pense-bête", signature="-- Service Facturation")

# ⚠ ERREUR à éviter :
# email(destinataire="x@y.com", "Sujet", "Corps")  # <-- nommés avant positionnels (INTERDIT)

# *args — Arguments positionnels variables (nombre illimité)
# -> On capte les arguments SUPPLÉMENTAIRES dans un tuple.
def somme(*args):
    total = 0
    for x in args:
        total += x
    print("5) somme(*args) =", total)

somme(1, 2, 3)
somme(10, 20, 30, 40)



# COMBINER paramètres classiques + *args + **kwargs (ordre strict)
# ordre des paramètres: positionnels -> *args -> nommés -> **kwargs
def notifier(type_evenement, *destinataires, urgent=False, **options):
    print(f"7) {type_evenement=}, {destinataires=}, {urgent=}, {options=}")

notifier("ALERTE", "alice@ex.com", "bob@ex.com", urgent=True, canal="email", copie_manager=True)









# 9) Point d’entrée d’un programme Python
# ------------------------------------------------
# __name__ est une variable spéciale :
# - vaut "__main__" si le fichier est exécuté directement
# - vaut le nom du module si le fichier est importé ailleurs
def ma_fonction_test():
    print("Ceci est un test")

if __name__ == "__main__":
    ma_fonction_test()
    print("Exécuté directement (mode principal)")
else:
    print("Importé comme module")

# Autre exemple :
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

# Partie exécutée seulement si le fichier est lancé directement
if __name__ == "__main__":
    print("Exécution directe de main.py")
    print(addition(10, 5))
    print(soustraction(10, 5))



# 10) Modules et imports
# ------------------------------------------------
# - Un module = un fichier Python (.py) contenant des fonctions
# - On peut importer de plusieurs façons :
#   import module
#   from module import fonction
#   from module import *   (⚠ peut réduire la lisibilité)
# - Exemple : math est un module standard
import math
print("Racine carrée de 16 :", math.sqrt(16))


# 11) Paquets Python
# ------------------------------------------------
# - Un paquet = un dossier contenant plusieurs modules
# - Il doit contenir un fichier __init__.py
# Exemple d’arborescence :
# mon_projet/
# ├── main.py
# ├── mon_module.py
# └── mon_paquet/
#     ├── __init__.py
#     ├── module1.py
#     └── module2.py
#
# Import possible :
# from mon_paquet import module1
# from mon_paquet.module2 import ma_fonction
#
# Avantage : organiser proprement le code d’un projet
# ================================================================
