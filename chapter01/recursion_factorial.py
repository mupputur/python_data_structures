'''
factorial of 5

5! = 5 * 4 * 3 * 2 * 1

5! = 5 * 4!(4*3!(3*2!(2*1!)))
'''


def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result = result * i
    return result

#resp = factorial(5)
#print(resp)

def recursion_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursion_factorial(n-1)

print(recursion_factorial(5000))





