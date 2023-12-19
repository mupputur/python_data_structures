import sys


resp = sys.getrecursionlimit()

sys.setrecursionlimit(5000)


def recursion_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursion_factorial(n-1)

print(recursion_factorial(1000))