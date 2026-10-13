"""Exercice 9: partitionner le dictionnaire d'étudiants en admis / non admis
Admis: moyenne >= 10
Non admis: moyenne < 10
"""

def partition_students(etudiants):
    admis = {}
    non_admis = {}
    for nom, moy in etudiants.items():
        if moy >= 10:
            admis[nom] = moy
        else:
            non_admis[nom] = moy
    return admis, non_admis

if __name__ == '__main__':
    etudiants = {
        "étudiant_1": 13, "étudiant_2": 17, "étudiant_3": 9, "étudiant_4": 15,
        "étudiant_5": 8, "étudiant_6": 14, "étudiant_7": 16, "étudiant_8": 12,
        "étudiant_9": 13, "étudiant_10": 15, "étudiant_11": 14, "étudiant_12": 9,
        "étudiant_13": 10, "étudiant_14": 12, "étudiant_15": 13, "étudiant_16": 7,
        "étudiant_17": 12, "étudiant_18": 15, "étudiant_19": 9, "étudiant_20": 17
    }
    admis, non_admis = partition_students(etudiants)
    print("Admis:", admis)
    print("Non admis:", non_admis)
