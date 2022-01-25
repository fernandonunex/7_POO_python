import time
import sys

#Changing the limits of recursion
sys.setrecursionlimit(220000)
#print(sys.getrecursionlimit())


def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial_r( n - 1)

if __name__ == '__main__':
    n = 200000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(f"Factorial function 1 took: {final - comienzo}")

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(f"Factorial function 2 took: {final - comienzo}")
    
    


