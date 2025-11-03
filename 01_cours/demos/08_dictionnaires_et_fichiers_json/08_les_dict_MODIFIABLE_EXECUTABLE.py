# Pour créer un dictionnaire
mon_dict = {}

mon_dict_a = {'test': 'Texte de test', 1: 25, 'test': True}  # Pas de doublons de clé possible
print(mon_dict_a)

# Pour accéder à la valeur liée à la clé d'un dictionnaire,
# on se sert de la syntaxe ci-dessous
print(mon_dict_a[1])
print(mon_dict_a['test'])

# Pour ajouter un élément dans un dictionnaire,
# on crée une clé et on lui donne sa valeur
mon_dict_a['blabla'] = 'Texte lié à blabla'
print(mon_dict_a)

# Ici , on re-affecte la valeur de 'blabla' à autre chose
mon_dict_a['blabla'] = 247
print(mon_dict_a)

# Pour obtenir la liste des clés de notre dictionnaire, il existe la méthode .keys()
print(mon_dict_a.keys())
for k in mon_dict_a.keys():
    print(k)

# Pour obtenir les valeurs de notre dictionnaire, il existe la méthode .values()
print(mon_dict_a.values())

# Pour obtenir à la fois les clés et les valeurs de notre dictionnaire, on a la méthode .items()
print(mon_dict_a.items())
for key, value in mon_dict_a.items():
    print(f"Key coucou : {key} - Value : {value}")

# Permet de supprimer un élément de notre dictionnaire
# Attention : Exception si la clé n'existe pas !
del mon_dict_a['test']

# Il existe aussi la méthode .pop() dans laquelle il va falloir renseigner la clé
mon_dict_a.pop(1)
print(mon_dict_a)

# Pour fusionner deux dictionnaires ensemble, il existe la méthode .update()
mon_dict_a.update({2: "Valeur de clé 2"})
print(mon_dict_a)
