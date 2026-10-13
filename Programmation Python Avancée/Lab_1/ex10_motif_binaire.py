"""Exercice 10: retourner entiers dont représentation binaire contient un motif
La fonction motif(lst, pattern) -> dict {n: binary_string}
"""

def motif(lst, pattern):
    out = {}
    if pattern == '':
        return out
    for n in lst:
        b = bin(n)[2:]
        if pattern in b:
            out[n] = b
    return out

if __name__ == '__main__':
    arr = [5, 6, 7, 10]
    pat = input("Motif binaire: ")
    print(motif(arr, pat))
