from math import ceil, sqrt
from functools import reduce
from primes import gen_primes
import matplotlib.pyplot as plt
import numpy as np
import operator, time

prime_numbers = gen_primes(1000000)

def prime_factorization(n):
    if n in prime_numbers:
        return '%s is prime' % n
    primes, gen, number = [], iter(generate(n)), n
    while True:
        try:
            prime = next(gen)
        except StopIteration:
            return primes if primes else '%s is prime' % number
        else:
            while n/prime == int(n/prime):
                n = n/prime
                primes.append(prime)
                if n in prime_numbers:
                    n = int(n)
                    primes.append(n)
                    return primes
        try:
            if reduce(operator.mul, primes) == number:
                return primes
        except Exception:
            pass

def generate(n):
    search_space = np.arange(prime_numbers[-1], n)
    for i in prime_numbers:
        yield i
    for i in search_space:
        if n - sum((i%search_space).astype(np.bool).astype(np.int16)) == 3:
            yield i

def test(n, func):
    st = time.time()
    result = func(n)
    time_delta = time.time() - st
    return n, time_delta, result

def plot(x, y, func):
    plt.plot(x, y)
    plt.title('Complexity Analysis for [%s] Function' % func.__name__)
    plt.xlabel('Problem Size')
    plt.ylabel('Run Time (in seconds)')
    plt.grid()
    plt.show()

def analyze(n, func, results=True):
    st, trials = time.time(), 0
    xaxis, yaxis = [], []
    for problem_size in range(1, n+1):
        x, y, result = test(problem_size, func)
        xaxis.append(x); yaxis.append(y)
        trials += 1
    time_delta = time.time() - st
    print('\n%s\n[Test Time]: %s'%('='*80, time_delta))
    print('[Number of Trials]: %s'%(trials))
    print('[Run Time for Problem Size %s]: %s'%(n, y))
    if results:
        print('[Resultant Data from %s, for n=%s]: %s'%(func.__name__, n, result))
    print('%s\n'%('='*80))
    plot(xaxis, yaxis, func)
