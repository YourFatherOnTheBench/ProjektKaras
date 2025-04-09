
def silnia(x):
    if x > 0:
        return x * silnia(x-1)
    return 1


def wypisz(x):
    if len(x) == 3:
        print(x)
    else:
        wypisz(x + 'a')
        wypisz(x + 'b')
        wypisz(x + 'c')




def depesze():
    x = int(input())
    lista = []
    suma = 0
    lista = input().split()
    for i in lista:
        if i >= '0' and i <= '9':
            suma += int(i)
    print(suma)
    
depesze()