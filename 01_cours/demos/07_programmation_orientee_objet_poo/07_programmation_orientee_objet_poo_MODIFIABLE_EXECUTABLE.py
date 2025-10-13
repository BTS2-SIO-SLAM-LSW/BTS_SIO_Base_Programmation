# Pour créer une classe, il nous faut utiliser le mot-clé 'class'
# Par convention, les classes commencent par des majuscules
class Dog():

    # Pour créer un objet à partir de notre classe, il faudra passer par
    # son constructeur, qui est défini par la méthode __init__(self):
    # En passant des paramètres à cette méthode, on peut les placer dans notre objet
    def __init__(self, name, breed, age):

        # On crée la propriété d'instance self.nom_prop et on lui donne une valeur
        # par l'affectation des paramètres du constructeur
        self.name = name
        self.breed = breed
        self.age = age
        self.blabla = True

    # Pour créer des Getter (des nom de proprietés personnalisés qui
    # permettent d'avoir un contrôle sur la syntaxe ou le type de nos propriétés
    def __getattr__(self, item):
        if item == "age_str":
            return f"{self.age} ans"
        elif item == "test":
            return "Toutou"
        elif item == "is_adult":
            if self.age >= 1:
                return True
            else:
                return False
        raise AttributeError(item)

    # Pour les getters, il existe une syntaxe plus moderne d'en créer
    @property
    def color(self):
        return f"{self.name} is Blue"

    @property
    def double_age(self):
        return self.age * 2

    # Pour créer des Setter (des contrôles potentiels sur nos affectations de variables,
    # on se sert de la surcharge de la méthode dunder __setattr__()
    def __setattr__(self, key, value):
        if key == "human_age":
            self.age = int(value / 7)
        else:
            super().__setattr__(key, value)  # Ne pas oublier ceci sous peine de ne plus pouvoir setter de propriétés
        pass

    # Pour les setters, cette syntaxe est disponible
    # (Attention, il nous faut le getter @property pour pouvoir avoir son setter)
    @double_age.setter
    def double_age(self, value):
        self.age = int(value / 2)

    # Pour faire une méthode, il nous faut faire une fonction dans notre classe
    # qui possède comme premier paramètre le mot-clé self (ce qui l'attachera à notre instance)
    #
    # Via ce mot clé, il nous est également possible d'accéder à toutes les propriétés et méthodes de notre instance
    def aboyer(self, text):
        print(f"{self.name} says : {text}")


# Pour créer une instance de notre classe Dog, il nous faut faire appel au constructeur nom_class(params)
# qui va nous renvoyer une variable du type de la classe
mon_chien = Dog("Bernie", "Labrador", 7)

# Afficher l'objet en faisant appel à la méthode __str__()
print(mon_chien)

# Pour accéder aux propriétés de l'objet,
# on se sert de la notation nom_instance.nom_prop
print(mon_chien.age)

mon_chien.age = 21
print(mon_chien.age)
print(mon_chien.age_str)
print(mon_chien.test)
print(mon_chien.is_adult)

mon_chien.human_age = 21
print(mon_chien.age)

print(mon_chien.color)

# mon_chien.double_age = 18
# print(mon_chien.age)
