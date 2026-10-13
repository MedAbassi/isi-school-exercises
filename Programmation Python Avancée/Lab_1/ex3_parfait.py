"""Exercice 3: déterminer si un entier N est parfait
A perfect number equals the sum of its proper divisors (excluding the number itself).
"""

def est_parfait(n):
    if n <= 1:
        return False
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            j = n // i
            if j != i:
                total += j
        i += 1
    return total == n

if __name__ == '__main__':
    N = int(input("Entrez un entier: "))
    print("Parfait" if est_parfait(N) else "Non parfait")
