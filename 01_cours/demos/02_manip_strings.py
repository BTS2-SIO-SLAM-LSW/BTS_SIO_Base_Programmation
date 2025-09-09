# Concaténation de chaines de caractères
un_nombre = 25
un_texte = "Teste de texte"
un_resultat = un_texte + str(un_nombre)

# Ajout de variables dans les chaines de caractère
mon_genre = 'Garçon'
mon_age = 14

# Chaines formatées classiques
ma_chaine_formatee = "Je suis un {0} et j'ai {1} ans !".format(mon_genre, mon_age)
ma_chaine_formatee2 = f"Je suis un {mon_genre} et j'ai {mon_age} ans !"

# Formatage et modification du nombre de caractère après la virgule (arrondi automatique)
ma_chaine_formatee3 = "Ma moyenne est est de {0:.2f} / 20".format(14.4999)
ma_chaine_formatee4 = f"Ma moyenne est est de {14.5:.2f} / 20"

# Formatage et modification du nombre de caractère que doit prendre horizontalement la variable
ma_chaine_formatee5 = f"{25:6} | {4.99:15.1f}"
ma_chaine_formatee6 = f"{512:6} | {15.37:15.1f}"
ma_chaine_formatee7 = f"{1024:6} | {2.8754:15.1f}"

# Rogner un mot
mon_mot = 'Pierre'
print(f"{mon_mot:.3s}")
print(f"{mon_mot[2:4]}")

print(ma_chaine_formatee)
print(ma_chaine_formatee2)
print(ma_chaine_formatee3)
print(ma_chaine_formatee4)

# Formatage du string et modification de son alignement horizontal avec ajout d'un nombre choisi
# de caractère en fin, sur les côtés ou au début de la chaine de caractère
print(f"{'Somme':6} | {'Valeur en %':<15}")
print(f"{'Somme':6} | {'Valeur en %':^15}")
print(f"{'Somme':6} | {'Valeur en %':>15}")

print(ma_chaine_formatee5)
print(ma_chaine_formatee6)
print(ma_chaine_formatee7)
