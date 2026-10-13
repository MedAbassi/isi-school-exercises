"""Exercice 1: valeur absolue de la différence de deux entiers
Corrections of the provided (buggy) program.
"""

def valeur_absolue_diff():
    x = int(input("Donner un entier : "))
    y = int(input("Donner un entier : "))
    z = x - y
    if z < 0:
        resultat = -z
    else:
        resultat = z
    print("valeur absolue :", resultat)


if __name__ == '__main__':
    valeur_absolue_diff()
