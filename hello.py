from math import sqrt
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) +1 ):
        if n % 2 == 0:
            return False
        return True
print('Hello world')
prrint('Neymar will be the champion of World Cup 2026')
