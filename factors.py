'''
Contains functions for the following operations:
    
    - finding the factors of n
    - finding the common factors for any set of numbers in n, n+1,...,m
    - finding the greatest common factor for any set of numbers in n, n+1,...,m
    - finding the least common multiple for any set of numbers in n, n+1,...,m
    - finding the prime factorization of n
'''
from random import randint # used for testing
#from primes import gen_primes
import numpy as np
import functools, sys, os

np.seterr(divide='ignore')

# begin set of math functions

def factors(n):
    array = np.arange(n)
    return (list(array[n%array == 0]) + [n])[1:] # a[0] is zero

def common_factors(*args):
    command = ''
    for value in args:
        command += 'set({}) & '.format(factors(int(value)))
    command = command.strip(' & ')
    return sorted(list(eval(command)))

def greatest_common_factor(*args):
    common = common_factors(*args)
    return np.array(common).max()

def least_common_multiple(*args):
    args, command = list(map(int, args)), ''
    while 0 in args: 
        args.remove(0)
    try:
        array_limit = functools.reduce(lambda x, y: x*y, args)
        array = np.arange(1, array_limit + 1)
    except TypeError as e:
        return None
    else:
        for arg in args:
            command += 'set(array[array%{} == 0]) & '.format(arg)
        return min(eval(command[:-3]))

def prime_factorization(n):
    global primes
    primes = np.array(gen_primes(n))
    try:
        return recursion(n)
    finally:
        del primes

def recursion(n, data=''):
    array = primes[n%primes == 0]
    try:
        data += str(array[0]) + ' '
    except IndexError as e:
        data = data.split()
        if len(data) == 1:
            return '{} is prime'.format(int(float(data[0])))
        return sorted(list(map(int, map(float, data))))
    else:
        return recursion(n/array[0], data)

# end set of math functions

# convience functions for testing, and stand-alone use of module

def display(data, length=3): 
    os.system('clear')
    print('\ngenerated simulated data: {values}\n'.format(**data))
    for i in range(1, length+1):
        i_target, f_target = '{{i{}}}'.format(i), '{{f{}}}'.format(i)
        template = 'factors for {}: {}'.format(i_target, f_target)
        print(template.format(**data))
    print('''
common factors for {values}: {cf}
GCF: {gcf}
LCM: {lcm}
'''.format(**data))
    for i in range(1, length+1):
        i_target, pf_target = '{{i{}}}'.format(i), '{{pf{}}}'.format(i)
        template = 'prime factorization for {}: {}'.format(
                i_target, pf_target)
        print(template.format(**data))
    print()

if __name__ == '__main__':

    data = dict()

    if sys.argv[1].lower() == 'test':
    
        data['cf'] = []

        while len(data['cf']) < 2:
            i1, i2, i3 = randint(0, 50), randint(0, 50), randint(0, 50)
            data['cf'] = common_factors(i1, i2, i3)
        data['i1']  = i1
        data['i2']  = i2
        data['i3']  = i3
        data['values'] = args = [i1, i2, i3]
        data['f1']  = factors(i1)
        data['f2']  = factors(i2)
        data['f3']  = factors(i3)
        data['pf1'] = prime_factorization(i1)
        data['pf2'] = prime_factorization(i2)
        data['pf3'] = prime_factorization(i3)    
        data['gcf'] = greatest_common_factor(i1, i2, i3)
        data['lcm'] = least_common_multiple(i1, i2, i3)
    
    else:
        # exceeding a length of 3 command args is not recommended.
        # It may crash the system. Command args support is provided 
        # only as a convience method, but is not the intended end-user 
        # use case for this module.
        args, data_string = sys.argv[1:], ''
        data['values'] = list(map(int, args))

        for i in range(len(args)):    
            name  = 'i{}'.format(i+1)
            fname = 'f{}'.format(i+1)
            pname = 'pf{}'.format(i+1)
            data[name]  = int(args[i])
            data[fname] = factors(data[name])
            data[pname] = prime_factorization(data[name])
            data_string += args[i] + ', ' 
        data['cf'] = common_factors(*args)
        data['gcf'] = greatest_common_factor(*args)
        data['lcm'] = least_common_multiple(*args)
    display(data, len(args))
