'''
n! = 1 * 2 * 3 * ... * n

If n is even, then n! = (1 * 3 * 5 * ... * n-1) * (2 * 4 * 6 * ... * n).
If n is odd,  then n! = (1 * 3 * 5 * ... * n) * (2 * 4 * 6 * ... * n-1).

Let n! = (1 * 3 * ... * n-1) * (2 * 4 * ... * n). 
Then, n! = (1 * 3 * ... * n-1) * 2(1 * 2 * ... * (n/2))
         = (1 * 3 * ... * n-1) *  (1 * 3 * ... * (n/2) or (n/2)-1) * 2**2
         .
         .
         .
         = ((1**x1) * (3**x2) * ... ((n/2)**x3) * (n/2)+1 * ... * (n-1)) * 2**x

So we can calculate n! by finding no more than the product of the odd factors.
Cutting the number of required multiplications in approximately half.
'''
import functools, operator

def factorial(n):
    exponent = n-1 if n%2 else n
    if n <= 2:
        return n
    # TODO functools.reduce needs to be optimized
    # Multiply the odd factors of n!
    product = functools.reduce(operator.mul, range(1, n+1, 2))
    # Get rid of the remaining even factors of n! after factoring 2 out
    # and multiply any remaining odd factors
    product *= factorial(exponent//2)
    # Multiply all the powers of 2 back into n!
    return product * 2**(exponent//2)

if __name__ == '__main__':
    import math
    for n in range(1, 15):
        assert math.factorial(n) == factorial(n)
