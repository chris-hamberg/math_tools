import operator, sys, time
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce
from math import ceil, sqrt

#primes = []

def prime(n):
    numbers = np.arange(2, n+1)
    primes = gen_primes(ceil(sqrt(n)))
    for p in primes:
        numbers = numbers[numbers%p!=0]
    primes.extend(numbers)
    return np.array(primes)

def gen_primes(n):
    #global primes
    primes = []
    search_space = np.arange(1, ceil(sqrt(n))+1)
    for num in search_space[1:]:
        if sum(num/search_space == np.int16(num/search_space)) <=2:
            primes.append(num)
    search_space = np.arange(1, n+1)
    boolean_masks = []
    for prime in primes:
        x = search_space%prime
        x = x.astype(np.bool)
        boolean_masks.append(x)
    mask = np.array(list(reduce(operator.mul, boolean_masks)))
    search_space = search_space[mask]
    primes.extend(list(search_space))
    primes.sort()
    return primes[1:]

def test(n):
    st = time.time()
    gen_primes(n)
    time_delta = time.time() - st
    return n, time_delta

def plot(x, y):
    plt.plot(x, y)
    plt.title('Run Time Complexity of Prime Number Generation Algorithm')
    plt.grid()
    plt.xlabel('Problem Size')
    plt.ylabel('Run Time (in seconds)')
    plt.show()

def analyze(n):
    st = time.time()
    xaxis, yaxis = [], []
    for run in range(2, n+1):
        x, y = test(run)
        xaxis.append(x); yaxis.append(y)
    time_delta = time.time() - st
    print('test time: %f' % time_delta)
    print('run time for n: %f' % y)
    print(primes)
    plot(xaxis, yaxis)

if __name__ == '__main__':
    n = int(sys.argv[1])
    try:
        if sys.argv[2].lower() == 'analyze':
            analyze(n)
        else:
            raise IndexError
    except IndexError:
        print(test(n))
