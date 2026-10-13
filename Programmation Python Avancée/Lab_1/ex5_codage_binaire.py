"""Exercice 5:
- Codage binaire d'une chaîne composée de deux caractères (le premier -> 0, l'autre -> 1)
- Généralisation: coder une chaîne composée de n caractères distincts (n <= 10) en entiers 0..n-1
"""

def coder_2_chars(s):
    if not s:
        return ''
    uniques = []
    for ch in s:
        if ch not in uniques:
            uniques.append(ch)
            if len(uniques) > 2:
                return -1
    if len(uniques) == 1:
        # all same char -> all zeros
        return '0' * len(s)
    a, b = uniques
    return ''.join('0' if ch == a else '1' for ch in s)


def coder_n_chars(s):
    """Map up to 10 distinct characters to digits 0..n-1 and return string of digits separated by no space.
    Returns -1 if more than 10 distinct chars.
    """
    mapping = {}
    next_code = 0
    out = []
    for ch in s:
        if ch not in mapping:
            if next_code >= 10:
                return -1
            mapping[ch] = str(next_code)
            next_code += 1
        out.append(mapping[ch])
    return ''.join(out)

if __name__ == '__main__':
    s = input("Entrez la chaine: ")
    print("Codage 2-chars:", coder_2_chars(s))
    print("Codage n-chars:", coder_n_chars(s))
