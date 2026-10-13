"""Exercice 8: convertir un texte en dictionnaire mot->longueur
Les mots sont séparés par espaces; on conserve l'ordre d'apparition si vous voulez une OrderedDict.
"""

def words_length_dict(text):
    words = text.split()
    return {w: len(w) for w in words}

if __name__ == '__main__':
    T = input("Entrez le texte: ")
    print(words_length_dict(T))
