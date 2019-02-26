import functools, operator, itertools, datetime, math, sys

class SystemLinearCongruence:

    '''
    Fast Arithmetic using a unique tuple representation of an integer modulo 
    relatively prime moduli.
    '''

    #TODO only addition is currently defined.

    def __init__(self, m1=33554431, m2=4194303, m3=8388607):
        '''
        elstablishes a system of linear congruences
        '''
        self.test(m1, m2, m3)
        self.m1, self.m2, self.m3 = m1, m2, m3
        self.m = functools.reduce(operator.mul, [self.m1, self.m2, self.m3])
        
        self.M1 = int(self.m / self.m1)
        self.M2 = int(self.m / self.m2)
        self.M3 = int(self.m / self.m3)
        
        # get modular inverses
        self.y1 = self.inverse(self.m1, self.M1)
        self.y2 = self.inverse(self.m2, self.M2)
        self.y3 = self.inverse(self.m3, self.M3)
       
        # make sure y is the modular inverse of M modulo m
        if not (self.M1 * self.y1 % self.m1 == 1 and 
                self.M2 * self.y2 % self.m2 == 1 and 
                self.M3 * self.y3 % self.m3 == 1):
            raise AssertionError

    def test(self, m1, m2, m3):
        '''
        make sure the moduli are pairwise relatively prime
        '''
        for a, b in list(itertools.combinations([m1, m2, m3], 2)):
            if not math.gcd(a, b) == 1:
                raise AssertionError

    def inverse(self, a, b):
        '''
        The Extended Euclidean Algorithm

        Returns the Bezout coefficent for M
        '''
        try:
            if not math.gcd(a, b) == 1:
                raise AssertionError
        except AssertionError:
            print(a)
            print([self.m1, self.m2, self.m3])

        s0, s1 = (1, 0)
        t0, t1 = (0, 1)
        while b != 0:
            q, r = a // b, a % b
            a, b = b, r
            s0, s1 = s1, s0 - q * s1
            t0, t1 = t1, t0 - q * t1

        return t0

    def solve(self, n):
        '''
        Use the Chinese Remainder Theorem to solve the system.
        '''
        a1, a2, a3 = n[0], n[1], n[2]
        return (a1 * self.M1 * self.y1 + 
                a2 * self.M2 * self.y2 + 
                a3 * self.M3 * self.y3) % self.m

    def reduce(self, n):
        '''
        Used to convert a large integer to a unique 3-tuple representation
        modulo the relatively prime moduli of the system.
        '''
        return (
         n % self.m1, n % self.m2, n % self.m3)

    def add(self, a, b):
        '''
        Component-wise addition of the tuple representation of an integer
        under the system.
        '''
        return (
         a[0] + b[0], a[1] + b[1], a[2] + b[2])


def base2_pseudoprimes(n):
    epoch, trial, pseudoprimes = datetime.datetime.utcnow(), 0, 0
    msg = '[SECONDS] {delta} :: {pseudoprimes} out of {trial} base-2 pseudoprimes found'
    for number in range(5, n + 1, 2):
        trial += 2
        try:
            if not (math.gcd(number, 2) == 1 and 
                    2 ** (number - 1) % number == 1 % number):
                raise AssertionError
            pseudoprimes += 1
        except AssertionError:
            pass
        finally:
            delta = int((datetime.datetime.utcnow() - epoch).total_seconds())
            print(msg.format_map(vars()), end='\r')

    print()
    input('complete')


if __name__ == '__main__':
    import random
    count = 0
    for i in range(1000):
        a, b = random.randrange(7, 1000), random.randrange(7, 1000)
        if math.gcd(a, b) == 1:
            euclid(max(a, b), min(a, b))
            count += 1

    print(count)
