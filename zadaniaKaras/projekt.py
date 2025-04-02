import time
MOD=1000
def pot(a,b):
    if b== 0:
        return 1
    x=pot(a,b//2)
    y = x * x % MOD
    if b % 2 == 1:
        y = y * a & MOD
    return y


def pot2(a,b):
    if b == 0:
        return 1
    x = pot2(a, b//2)
    y = x * x
    if b % 2 == 1:
        y = y * a
    return y

pocz = time.time()
print(pocz)
print(pot(9,5001231))
kon = time.time()
print(kon)
print("Czas wykonania " + str(kon - pocz))

pocz = time.time()
print(9 ** 5001231 % 1000)
kon = time.time()
print("Czas wykonania " + str(kon - pocz))