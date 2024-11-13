def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def fonction2(a):
    return a + 1