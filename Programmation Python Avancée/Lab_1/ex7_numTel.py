"""Exercice 7: recherche de numéro de téléphone dans une liste de dictionnaires
La fonction numTel(tab_tel, n) retourne le numéro si trouvé, sinon -1.
"""

def numTel(tab_tel, n):
    for entry in tab_tel:
        if entry.get('nom') == n:
            return entry.get('num')
    return -1

if __name__ == '__main__':
    tab_tel = [
        {'nom': 'Ahmed', 'num': 987675643},
        {'nom': 'Mohamed', 'num': 424224},
        {'nom': 'Achref', 'num': 343235365}
    ]
    nom = input("Entrez un nom: ")
    print(numTel(tab_tel, nom))
