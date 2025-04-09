

x = int(input("Podaj liczbe: "))
def oblicz_silnie(x):
    if x > 0:
        return x * oblicz_silnie(x-1)
    return 1

print(f"Silnia z tej liczby to: {oblicz_silnie(x)}")