import random

# Erzeugen von Zufallszahlen
random.seed(0)
L_size = 20000 
L = [random.random() for _ in range(L_size)]  # List comprehension für effizientere Erzeugung

def find_duplicates(lst):
    # Verwendung eines Satzes, um duplizierte Werte effizient zu erkennen
    seen = set()
    duplicates = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)  # Rückgabewert als Liste, falls erforderlich

duplicates = find_duplicates(L)


