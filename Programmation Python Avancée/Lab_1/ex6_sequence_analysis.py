"""Exercice 6: analyse d'une séquence
Fonctions fournies:
- freq_chars(s) -> list of [char, count] sorted by count descending
- substrings_k(s, k) -> list of unique substrings of length k in order of first appearance
- find_motif_positions(s, motif) -> list of start indices of motif occurrences
- rle_compress(s) -> run-length encoding like A1T1C2...
"""

def freq_chars(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    # return list sorted by count descending
    return [[ch, counts[ch]] for ch in sorted(counts, key=lambda c: (-counts[c], c))]


def substrings_k(s, k):
    seen = set()
    out = []
    if k <= 0:
        return out
    for i in range(len(s) - k + 1):
        sub = s[i:i+k]
        if sub not in seen:
            seen.add(sub)
            out.append(sub)
    return out


def find_motif_positions(s, motif):
    positions = []
    if motif == "":
        return positions
    i = s.find(motif)
    while i != -1:
        positions.append(i)
        i = s.find(motif, i+1)
    return positions


def rle_compress(s):
    if not s:
        return ''
    out = []
    cur = s[0]
    cnt = 1
    for ch in s[1:]:
        if ch == cur:
            cnt += 1
        else:
            out.append(f"{cur}{cnt}")
            cur = ch
            cnt = 1
    out.append(f"{cur}{cnt}")
    return ''.join(out)

if __name__ == '__main__':
    seq = input("Entrez la sequence: ")
    print("Freq:", freq_chars(seq))
    k = int(input("k pour sous-chaines: "))
    print("Sous-chaines k uniques:", substrings_k(seq, k))
    motif = input("Motif a chercher: ")
    print("Positions:", find_motif_positions(seq, motif))
    print("RLE:", rle_compress(seq))
