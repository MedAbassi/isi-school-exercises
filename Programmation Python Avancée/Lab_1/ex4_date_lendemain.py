"""Exercice 4: afficher la date du lendemain à partir de J, M, A
Handles leap years and end-of-month/year transitions.
"""

def est_bissextile(a):
    return (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)


def lendemain(j, m, a):
    if m < 1 or m > 12:
        raise ValueError("Mois invalide")
    if j < 1:
        raise ValueError("Jour invalide")
    jours_par_mois = [31, 29 if est_bissextile(a) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if j > jours_par_mois[m-1]:
        raise ValueError("Jour invalide pour le mois donné")
    j += 1
    if j > jours_par_mois[m-1]:
        j = 1
        m += 1
        if m > 12:
            m = 1
            a += 1
    return j, m, a

if __name__ == '__main__':
    j = int(input("Jour (J): "))
    m = int(input("Mois (M): "))
    a = int(input("Année (A): "))
    j2, m2, a2 = lendemain(j, m, a)
    print(f"Le lendemain est : {j2:02d}/{m2:02d}/{a2}")
