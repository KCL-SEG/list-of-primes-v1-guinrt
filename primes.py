"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def checkPrime(num):
    if num > 2:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        else:
            return True

def primes(number_of_primes):
    list = []
    n = 2
    while len(list) != number_of_primes:
        n +=1
        if checkPrime(n):
            list.append(n)

    return list
