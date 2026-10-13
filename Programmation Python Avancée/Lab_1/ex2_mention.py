"""Exercice 2: afficher la mention à partir de la moyenne
Mapping used (typical French scale):
- >=16: Très bien
- 14-15.99: Bien
- 12-13.99: Assez bien
- 10-11.99: Passable
- <10: Ajourné
"""

def mention(moyenne):
    try:
        m = float(moyenne)
    except ValueError:
        raise ValueError("La moyenne doit être un nombre")
    if m >= 16:
        return "Très bien"
    elif m >= 14:
        return "Bien"
    elif m >= 12:
        return "Assez bien"
    elif m >= 10:
        return "Passable"
    else:
        return "Ajourné"

if __name__ == '__main__':
    m = input("Entrez la moyenne: ")
    print(mention(m))
