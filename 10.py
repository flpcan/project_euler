# The next code works but it is too slow.

# numbers = []

# for i in range(2,2000000):
#     x = list(map(lambda y: i % y ==0 , range(2,i)))
#     if sum(x) == False:
#         numbers.append(i)
        
# print(sum(numbers))


# This code works and it is from https://www.youtube.com/watch?v=JA_YrFwE1hc

from math import isqrt

def primes_less_than(n: int) -> list[int]:
    if n<= 2:
        return []

    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(n)+1):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]


print(sum(primes_less_than(20)))
