f = lambda p: bool(not((p+2)%3))
g = lambda p: bool(not((p+4)%3))


def prime(n):
    val, primes = 5, [] 
    for e, p in enumerate(range(5, n+1)):
        if val > n: break
        elif not(e%2): i = 2
        else: i = 4
        val += i
        if val not in (5*5, 7*5, 7*7, 11*5, 13*5, 11*7, 17*5, 13*7, 19*5):
            #false positives# 25, 35, 49, 55, 65, 77, 85, 91, 95
            primes.append(val)
    return primes



def prime(n):
    val, primes = 5, [] 
    for e, p in enumerate(range(5, n+1)):
        if val > n: break
        elif not(e%2): i = 2
        else: i = 4
        val += i
        if (val == 5 val == 7 or val == 11 or val == 13
        ) or (val%5 and val%7 and val%11 and val%13):
            primes.append(val)
    return primes
