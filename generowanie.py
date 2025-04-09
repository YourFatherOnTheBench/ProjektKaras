
global wynik
wynik = 0
lista = []
n = int(input(''))
def generuj(word):
    global wynik
    if len(word) == n:
        wynik += 1
        lista.append(word)
    else:
        if len(word) == 0:
            generuj(word + 'a',)
            generuj(word + 'b')
            generuj(word + 'c')
        elif word[-1] == 'a':
            generuj(word + 'b')
            generuj(word + 'c')
        elif word[-1] == 'b':
            generuj(word + 'a')
            generuj(word + 'c')
        elif word[-1] == 'c':
            generuj(word + 'a')
            generuj(word + 'b')




generuj("")
print(f"{wynik}")
print(*lista, sep="\n")