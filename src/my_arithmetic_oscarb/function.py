def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def return_42():
    return 42